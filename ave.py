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
        self.tiempoImagen = 0

    def actualizar(self):
        if(self.image.__eq__(pygame.image.load("data/ave2.png"))):
                self.tiempoImagen += 1
        if(self.tiempoImagen > 20):
            self.image = pygame.image.load("data/ave.png")
            self.tiempoImagen = 0

    def colisionConTuberia(self, tuberia):
        if(self.rect.right - 20 >= tuberia.rect.left and self.rect.left <= tuberia.rect.right and
        self.rect.bottom - 2 >= tuberia.rect.y and self.rect.y + 20 <= tuberia.rect.bottom):
            return True
        return False
