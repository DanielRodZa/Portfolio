import random

from const import *
from utils import cargar_imagen

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_path, altura_piso):
        super().__init__()
        self.image = cargar_imagen(imagen_path)  # Superficie transparente
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidad_x = random.choice([-2, 2]) # Velocidad del enemigo aleatoria
        self.tiempo_vida = 0 # Tiempo de vida en segundos
        self.altura_piso = altura_piso

        self.rect.bottom = altura_piso - (self.rect.height)

    def update(self, dt): # Movimiento del enemigo
        self.rect.x += self.velocidad_x
        # Rebote en los bordes de la pantalla (opcional)
        if self.rect.left < 0 or self.rect.right > ANCHO_VENTANA:
            self.velocidad_x *= -1
            self.rect.x += self.velocidad_x

        self.tiempo_vida += dt # Incrementa el tiempo de vida
        if self.tiempo_vida >= TIEMPO_VIDA_ENEMIGO:
            self.reaparecer()

    def reaparecer(self):
        self.rect.x = random.randint(50, ANCHO_VENTANA - 50)
        self.rect.y = random.randint(50, self.altura_piso - 50) # Usa altura_piso
        self.tiempo_vida = 0 # Reinicia el tiempo
        self.velocidad_x = random.choice([-2, 2])