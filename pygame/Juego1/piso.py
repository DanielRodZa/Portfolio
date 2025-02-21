import pygame
from utils import *

class Piso(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_path):
        super().__init__()
        self.image = cargar_imagen(imagen_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
