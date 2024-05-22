import os
import cv2
import math
from rembg import remove

DIRECTORIO = ""
DIRECTORIO_DESTINO = ""
RELACION_DESEADA = 3 / 4
RELACION_DESEADA_HORIZONTAL = 1 / RELACION_DESEADA

class IMGTreatment:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def isVertical(self, image):
        return image.shape[1] > image.shape[0]

    def relacionImg(self, image):
        return image.shape[1] / image.shape[0]

    def cropImg(self, image, relacion):
        if image.shape[0] < 1168:
            image = self.resizeImg(image, relacion)
        height = image.shape[0]
        width = relacion * height
        width = math.floor(width)
        dif_row = image.shape[1] - width
        start_row = math.floor(dif_row / 2)

        new_image = image[0:height, int(start_row):int(image.shape[1]) - int(start_row)]
        return new_image

    def resizeImg(self, image, relacion):
        if self.isVertical(image):
            height = 1168
        else:
            height = 876
        width = math.floor(relacion * height)
        image = cv2.resize(image, (width, height))
        return image

    @staticmethod
    def remove_background(input, output):
        try:
            with open(input, 'rb') as inp, open(output, 'wb') as outp:
                background_output = remove(inp.read())
                outp.write(background_output)
        except Exception as e:
            print(f"Error removing background: {e}")

    @staticmethod
    def image_greyscale(image):
        try:
            imagen_grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            print(f"Error converting image to grayscale: {e}")
            return None
        return imagen_grises

    def complete_treatment(self):
        contador = 1
        print(f"\033[34m >>> Starting Treatment ...\033[0m")
        print(f"\033[34m >>> Cropping Images ...\033[0m")
        file_list = os.listdir(self.input_path)
        for file in file_list:
            if file.endswith((".jpg", ".jpeg", "png")):
                try:
                    image = cv2.imread(os.path.join(self.input_path, file))
                except Exception as e:
                    print(f"Error reading file: {file}. Skipping...")
                    continue
                if self.isVertical(image):
                    relacion = RELACION_DESEADA_HORIZONTAL
                else:
                    relacion = RELACION_DESEADA

                new_image = self.cropImg(image, relacion)
                try:
                    cv2.imwrite(DIRECTORIO_DESTINO + "\\Recortadas\\" + file.replace("jpg", "png")
                                .replace("jpeg", "png"), new_image)
                except Exception as e:
                    print(f"Error writing file: {file}. Skipping...")
                contador += 1
                self.print_progress_bar(contador, len(file_list), 'Cropping images')

        print(f"\033[34m >>> Removing Background ...\033[0m")
        contador = 1
        file_list_output = os.listdir(self.output_path + '\\Recortadas\\')
        for file in file_list_output:
            self.remove_background(DIRECTORIO_DESTINO + "\\Recortadas\\" + file, DIRECTORIO_DESTINO + "\\SinFondo\\sinFondo_" +
                                   file.replace("jpg", "png").replace("jpeg", "png"))
            self.print_progress_bar(contador, len(file_list_output), 'Removing background')
            contador += 1

        print(f"\033[34m >>> Treatment Completed ...\033[0m")

    def print_progress_bar(self, current, total, message: str = None):
        percentage = (current / total) * 100
        bar_length = 50
        num_bars = int(percentage / (100 / bar_length))
        progress_bar = "\033[32m\u2588\033[0m" * num_bars + "\033[37m\u2592\033[0m" * (
                bar_length - num_bars)  # █ and ▒ characters
        if percentage < 100:
            if message:
                formatted_message = f"\033[94m \033[33m-{message}- \033[37mIn progress\033[0m"
                print(
                    f"{formatted_message}[{progress_bar}] {current}/{total} \033[36m{percentage:.2f}%\033[0m")
            else:
                formatted_message = f"\033[94m \033[37mIn progress\033[0m"
                print(
                    f"{formatted_message}[{progress_bar}] {current}/{total} \033[36m{percentage:.2f}%\033[0m")
        else:
            if message:
                formatted_message = f"\033[94;1m \033[93;1m-{message}- \033[92;1m Complete  \033[0m"
                print(
                    f"{formatted_message}[{progress_bar}] \033[32;1m{current}/{total} {percentage:.2f}%\033[0m")
            else:
                formatted_message = f"\033[94;1m \033[92;1m Complete  \033[0m"
                print(
                    f"{formatted_message}[{progress_bar}] \033[32;1m{current}/{total} {percentage:.2f}%\033[0m")


def main():
    imagen = IMGTreatment(DIRECTORIO, DIRECTORIO_DESTINO)
    imagen.complete_treatment()

if __name__ == "__main__":
    main()