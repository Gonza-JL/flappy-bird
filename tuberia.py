from cmath import rect
import pygame
from configuracion import *

class Tuberia(pygame.sprite.Sprite):
    def __init__(self, directorio):
        super().__init__()
        self.image = pygame.image.load(directorio).convert()
        self.image.set_colorkey(COLOR_BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO + 200

    def movimiento(self):
        if(self.rect.centerx < -100):
            self.rect.centerx = ANCHO + 100
        self.rect.centerx -= 4
