import random

import pygame

from const import *


class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_path):
        super().__init__()
        self.image = pygame.image.load(imagen_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.en_salto = False
        self.vida = 100
        self.dano_recibido = 0

    def update(self):
        # Gravedad
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10

        # Guardar la posición anterior (IMPORTANTE para colisión)
        posicion_anterior = self.rect.copy()

        # Movimiento y colisiones (Se mejorará)
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Límites de pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO_VENTANA:
            self.rect.right = ANCHO_VENTANA

    def saltar(self):
        if not self.en_salto:
            self.velocidad_y = -15
            self.en_salto = True

    def colisionar_plataforma(self, plataformas):
        # Chequeo básico de colisiones con plataformas
        colisiones = pygame.sprite.spritecollide(self, plataformas, False)
        for plataforma in colisiones:
            # Si estamos cayendo y chocamos con una plataforma
            # Colisión desde arriba
            if self.velocidad_y > 0 and self.rect.bottom - self.velocidad_y <= plataforma.rect.top: # Cayendo
                self.rect.bottom = plataforma.rect.top
                self.velocidad_y = 0
                self.en_salto = False # Permite saltar de nuevo

            # Colisión desde abajo
            elif self.velocidad_y < 0 and self.rect.top - self.velocidad_y >= plataforma.rect.bottom: # Saltando
                self.rect.top = plataforma.rect.bottom
                self.velocidad_y = 0

            # Colisión lateral (derecha)
            elif self.velocidad_x > 0 and self.rect.right - self.velocidad_x <= plataforma.rect.left:
                self.rect.right = plataforma.rect.left
                self.velocidad_x = 0

            # Colisión lateral (izquierda)
            elif self.velocidad_x < 0 and self.rect.left - self.velocidad_x >= plataforma.rect.right:
                self.rect.left = plataforma.rect.right
                self.velocidad_x = 0

    def colisionar_enemigo(self, enemigos):
        colisiones = pygame.sprite.spritecollide(self, enemigos, False)
        for _ in colisiones:
            self.recibir_dano(10)

    def colisionar_piso(self, altura_piso):
        # Colisión con el piso (solo si estamos cayendo)
        if self.rect.bottom >= altura_piso and self.velocidad_y > 0:
            self.rect.bottom = altura_piso
            self.velocidad_y = 0
            self.en_salto = False

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.morir()

    def morir(self):
        # Recibir el nivel o mostrar una pantalla de Game Over, etc.
        # Por ahora, lo reiniciamos a la posición inicial:
        self.rect.x = 50
        self.rect.y = ALTO_VENTANA - 200
        self.vida = 100
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.en_salto = False
        self.dano_recibido = 0

    def detener_x(self):
        self.velocidad_x = 0
