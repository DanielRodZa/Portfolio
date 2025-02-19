import cv2
import torch
import numpy as np
import os
from tqdm import tqdm

class DepthEstimator:
    def __init__(self, model_type="DPT_Large"):
        """
        Constructor
        Args:
            model_type(str): Tipo de modelo MiDas a utilizar.
                            Opciones: "DPT_Large", "MiDas_Small", "DPT_Hybrid"
        """

        self.model_type = model_type
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.load_model()

    def load_model(self):
        """
        Carga el modelo MiDas y lo mueve al dispositivo (CPU o GPU)
        """
        model_path = torch.hub.get_dir() + f"/isl-org_MiDaS_{self.model_type.lower()}-f6b98070.pt"

        if not os.path.exists(model_path):
            print(f"Descargando modelo MiDas: ({self.model_type})...")

        self.model = torch.hub.load("intel-isl/MiDas", self.model_type)
        self.model.to(self.device)
        self.model.eval()

        midas_transforms = torch.hub.load("intel-isl/MiDas", "transforms")

        if self.model_type == "DPT_Large" or self.model_type == "DPT_Hybrid":
            self.transforms = midas_transforms.dpt_transform
        else:
            self.transforms = midas_transforms.small_transform

    def predict_depth(self, image):
        """
        Predice el mapa de profundidad para una imagen

        Args:
            image(np.array): Imagen de entrada

        Returns:
            np.ndarray: Mapa de profundidad predicho
        """
        input_batch = self.transforms(image).to(self.device)
        with torch.no_grad():
            prediction = self.model(input_batch)

            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=image.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()

        depth_map = prediction.squeeze().cpu().numpy()
        return depth_map

    def process_image(self, input_dir, output_dir):
        """
        Procesa todas las imágenes en un directorio y guarda los mapas de profundidad en otro directorio.

        Args:
            input_dir (str): Directorio de entrada con las imágenes.
            output_dir (str): Directorio de salida para guardar los mapas de profundidad.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        image_file = [
            f for f in os.listdir(input_dir) if os.path.isfile(
                os.path.join(input_dir, f)
            ) and f.lower().endswith(
                ('.png', '.jpg', '.jpeg')
            )
        ]

        for image_file in tqdm(image_file, desc="Procesando imagenes"):
            image_path = os.path.join(input_dir, image_file)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Advertencia: No se pudo cargar la imagen '{image_path}'. Saltando archivo...")

            depth_map = self.predict_depth(image)

            depth_map_normalized = cv2.normalize(depth_map, depth_map, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

            output_filename = os.path.splitext(image_file)[0] + "_depth.png"
            output_path = os.path.join(output_dir, output_filename)
            cv2.imwrite(output_path, depth_map_normalized)