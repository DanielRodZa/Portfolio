import pygame
import sys
import os

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
FPS = 60
COLOR_FONDO_DIA = (135, 206, 235)
COLOR_ENEMIGO = (255, 0, 0)
COLOR_TEXTO = (255, 255, 255)
TIEMPO_VIDA_ENEMIGO = 5


RUTA_IMAGENES = "imagenes"
RUTA_PERSONAJE = os.path.join(RUTA_IMAGENES, "personaje.png")
RUTA_PLATAFORMA = os.path.join(RUTA_IMAGENES, "plataforma.png")
RUTA_PISO = os.path.join(RUTA_IMAGENES, "piso.png")
RUTA_FONDO = os.path.join(RUTA_IMAGENES, "fondo.png")
RUTA_ENEMIGO = os.path.join(RUTA_IMAGENES, "enemigo1.png")