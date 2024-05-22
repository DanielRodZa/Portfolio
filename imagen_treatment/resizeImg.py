import os
import cv2
import math
from rembg import remove

DIRECTORIO = ""
DIRECTORIO_DESTINO = ""
RELACION_DESEADA = 3 / 4


def isHorizontal(image):
    return image.shape[1] > image.shape[0]


def relacionImg(image):
    return image.shape[1] / image.shape[0]


def cropImg(image):
    height = image.shape[0]
    width = RELACION_DESEADA * height
    width = math.floor(width)
    dif_row = image.shape[1] - width
    start_row = dif_row / 2

    # new_image = cv2.resize(image, (width, height))
    new_image = image[0:height, int(start_row):int(image.shape[1]) - int(start_row)]
    print(new_image.shape)
    return new_image

def remove_background(input, output):
    with open(input, 'rb') as inp, open(output, 'wb') as outp:
        background_output = remove(inp.read())
        outp.write(background_output)
def image_grises(image):
    imagen_grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return imagen_grises


def main():
    for file in os.listdir(DIRECTORIO):
        if file.endswith((".jpg",".jpeg","png")):
            image = cv2.imread(os.path.join(DIRECTORIO, file))
            dimensions = image.shape
            is_horizontal = isHorizontal(image)
            print(f"la imagen {file} tiene las siguientes dimensiones: {dimensions} y es horizontal: {is_horizontal}")
            if not is_horizontal:
                relacion = relacionImg(image)
                if relacion > RELACION_DESEADA:
                    new_image = cropImg(image)
                    imagen_gris = image_grises(new_image)
                    cv2.imwrite(DIRECTORIO_DESTINO + "\\" + file.replace("jpg", "png")
                                .replace("jpeg", "png"), new_image)
                    cv2.imwrite(DIRECTORIO_DESTINO + "\\gris" + file.replace("jpg", "png")
                                .replace("jpeg", "png"), imagen_gris)
                    remove_background(DIRECTORIO_DESTINO + "\\" + file, DIRECTORIO_DESTINO + "\\sinFondo_" +
                                        file.replace("jpg", "png").replace("jpeg", "png"))
                elif relacion < RELACION_DESEADA:
                    print(f"la imagen {file} no tiene la relacion deseada 3:4: {relacion:.2f}")
                else:
                    print(f"la imagen {file} tiene la relacion deseada 3:4: {relacion:.2f}")


if __name__ == "__main__":
    main()
