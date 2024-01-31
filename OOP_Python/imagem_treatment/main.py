import os
import cv2
import math
from rembg import remove

DIRECTORIO = r""
DIRECTORIO_DESTINO = r""
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
        height = image.shape[0]
        width = relacion * height
        width = math.floor(width)
        dif_row = image.shape[1] - width
        start_row = math.floor(dif_row / 2)

        new_image = image[0:height, int(start_row):int(image.shape[1]) - int(start_row)]
        return new_image

    def resizeImg(self, image, relacion, is_vertical):
        if is_vertical:
            height = 1168
        else:
            height = 876
        width = math.floor(relacion * height)
        image = cv2.resize(image, (width, height))
        return image

    @staticmethod
    def remove_background(input, output):
        with open(input, 'rb') as inp, open(output, 'wb') as outp:
            background_output = remove(inp.read())
            outp.write(background_output)
            print('Background eliminado')

    @staticmethod
    def image_greyscale(image):
        imagen_grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return imagen_grises

    def complete_treatment(self):
        for file in os.listdir(self.input_path):
            if file.endswith((".jpg", ".jpeg", "png")):
                image = cv2.imread(os.path.join(self.input_path, file))
                if self.isVertical(image):
                    relacion = RELACION_DESEADA_HORIZONTAL

                else:
                    relacion = RELACION_DESEADA
                image = self.resizeImg(image, relacion, self.isVertical(image))
                new_image = self.cropImg(image, relacion)
                imagen_grises = self.image_greyscale(new_image)
                cv2.imwrite(DIRECTORIO_DESTINO + "\\" + file.replace("jpg", "png")
                            .replace("jpeg", "png"), new_image)
                cv2.imwrite(DIRECTORIO_DESTINO + "\\gris" + file.replace("jpg", "png")
                            .replace("jpeg", "png"), imagen_grises)

        for file in os.listdir(self.output_path):
            self.remove_background(DIRECTORIO_DESTINO + "\\" + file, DIRECTORIO_DESTINO + "\\sinFondo_" +
                                   file.replace("jpg", "png").replace("jpeg", "png"))

def main():
    imagen = IMGTreatment(DIRECTORIO, DIRECTORIO_DESTINO)
    imagen.complete_treatment()

if __name__ == "__main__":
    main()