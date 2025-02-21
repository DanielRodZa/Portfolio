import random
from const import *

def cargar_imagen(ruta):
    try:
        imagen = pygame.image.load(ruta)
    except pygame.error as message:
        print(f"No se pudo cargar la imagen: {ruta}")
        raise SystemExit(message)
    return imagen

def dibujar_piso(pantalla, imagen_piso, altura_piso):
    ancho_imagen = imagen_piso.get_width()
    for x in range(0, ANCHO_VENTANA, ancho_imagen):
        pantalla.blit(imagen_piso, (x, altura_piso))

def mostrar_dano(pantalla, dano):
    font = pygame.font.Font(None, 36)
    texto = font.render(f"Daño: {dano}", True, COLOR_TEXTO)
    pantalla.blit(texto, (10, 10)) # Posición: arriba a la izquierda

def mostrar_menu(pantalla):
    # Un menú muy simple.
    font = pygame.font.Font(None, 48)
    texto_titulo = font.render("Mi juego de Plataformas", True, (255, 255, 255))
    texto_iniciar = font.render("Presiona ESPACIO para Iniciar", True, (255, 255, 255))
    texto_salir = font.render("Presiona ESC para Salir", True, (255, 255, 255))

    titulo_rect = texto_titulo.get_rect(center=(ANCHO_VENTANA // 2, 150))
    iniciar_rect = texto_iniciar.get_rect(center=(ANCHO_VENTANA // 2, 300))
    salir_rect = texto_salir.get_rect(center=(ANCHO_VENTANA // 2, 400))

    pantalla.blit(texto_titulo, titulo_rect)
    pantalla.blit(texto_iniciar, iniciar_rect)
    pantalla.blit(texto_salir, salir_rect)

    pygame.display.flip()

    esperando_tecla = True
    while esperando_tecla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando_tecla = False
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()