import sys
import pygame
import random
from utils import *
from const import *
from plataforma import Plataforma
from personaje import Personaje
from enemigo import Enemigo
from fondo import Fondo
from piso import Piso

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Juego de Plataformas")
    reloj = pygame.time.Clock()

    # Carga de imágenes
    personaje_imagen = cargar_imagen(RUTA_PERSONAJE)
    plataforma_imagen = cargar_imagen(RUTA_PLATAFORMA)
    piso_imagen = cargar_imagen(RUTA_PISO)
    fondo_imagen = cargar_imagen(RUTA_FONDO)
    enemigo_fondo = cargar_imagen(RUTA_ENEMIGO)

    # Creación de objetos del juego
    personaje = Personaje(50, ALTO_VENTANA - 200, RUTA_PERSONAJE)

    # Grupo de sprites
    todos_los_sprites = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    piso_grupo = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    todos_los_sprites.add(personaje)

    # Plataformas de ejemplo
    plataforma1 = Plataforma(0, ALTO_VENTANA - 150, RUTA_PLATAFORMA)
    plataforma2 = Plataforma(200, ALTO_VENTANA -220, RUTA_PLATAFORMA)
    plataforma3 = Plataforma(400, ALTO_VENTANA -290, RUTA_PLATAFORMA)
    plataformas.add(plataforma1, plataforma2, plataforma3)
    todos_los_sprites.add(plataforma1, plataforma2, plataforma3)

    # Piso
    altura_piso = ALTO_VENTANA - piso_imagen.get_height()
    ancho_piso = piso_imagen.get_height()
    for x in range(0, ANCHO_VENTANA, ancho_piso):
        piso_seccion = Piso(x, altura_piso, RUTA_PISO)
        piso_grupo.add(piso_seccion)
        todos_los_sprites.add(piso_seccion)

    # Enemigos
    for _ in range(3):
        x = random.randint(50, ALTO_VENTANA - 50)
        y = random.randint(50, altura_piso - 50) # Evita que aparezcan dentro del piso.
        enemigo = Enemigo(x, y, RUTA_ENEMIGO, altura_piso)
        enemigos.add(enemigo)
        todos_los_sprites.add(enemigo)

    fondo = Fondo(RUTA_FONDO, escala=0.7)

    # Mostrar menú
    mostrar_menu(pantalla)

    # Altura del piso
    altura_piso = ALTO_VENTANA - piso_imagen.get_height()

    # Bucle principal del juego
    jugando = True
    while jugando:
        dt = reloj.tick(FPS) / 1000
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            # controles
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    personaje.velocidad_x = -5
                if evento.key == pygame.K_d:
                    personaje.velocidad_x = 5
                if evento.key == pygame.K_SPACE:
                    personaje.saltar()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_a and personaje.velocidad_x < 0:
                    personaje.detener_x()
                if evento.key == pygame.K_d and personaje.velocidad_x > 0:
                    personaje.detener_x()

        # Actualizaciones
        personaje.update()
        personaje.colisionar_plataforma(plataformas)
        personaje.colisionar_enemigo(enemigos)
        personaje.colisionar_piso(altura_piso)
        enemigos.update(dt)

        # Dibujar
        pantalla.fill(COLOR_FONDO_DIA)
        dibujar_piso(pantalla, piso_imagen, altura_piso)
        todos_los_sprites.draw(pantalla)

        mostrar_dano(pantalla, personaje.dano_recibido)

        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
