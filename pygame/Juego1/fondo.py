from utils import *


class Fondo:
    def __init__(self, imagen_path, escala=1.0):
        self.imagen = cargar_imagen(imagen_path)
        self.imagen = pygame.transform.scale(
            self.imagen,
            (
                int(self.imagen.get_width() * escala),
                int(self.imagen.get_height() * escala),
            )
        )
        self.rect = self.imagen.get_rect()
        self.rect.bottom = ANCHO_VENTANA # Lo posicionamos en la parte inferior

    def dibujar(self, pantalla):
        # Dibujar la imagen, ajustando para que quede centrada si es más pequeña que la pantalla
        x = (ANCHO_VENTANA - self.rect.width) // 2
        pantalla.blit(self.imagen, (x, self.rect.top))
