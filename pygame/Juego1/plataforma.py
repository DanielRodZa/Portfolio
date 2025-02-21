import pygame


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_path):
        super().__init__()
        self.image = pygame.image.load(imagen_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
