from operator import truediv
import pygame
from configuracion import *

class Ave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/ave.png")
        self.image.set_colorkey(COLOR_BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO//3
        self.rect.bottom = ALTO//2
        self.vuelo = -10
        self.cambioImagenes = 0
        self.imagenActual = 1

    def actualizar(self):
        if(self.cambioImagenes % 10 == 0):
            if(self.imagenActual == 1):
                self.image = pygame.image.load("data/ave2.png")
                self.imagenActual = 2
            else:
                self.image = pygame.image.load("data/ave.png")
                self.imagenActual = 1
        self.cambioImagenes += 1

    def colisionConTuberia(self, tuberia):
        if(self.rect.right - 20 >= tuberia.rect.left and self.rect.left + 20 <= tuberia.rect.right and
        self.rect.bottom - 2 >= tuberia.rect.y and self.rect.y + 20 <= tuberia.rect.bottom):
            return True
        return False
