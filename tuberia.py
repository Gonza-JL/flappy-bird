import pygame
from configuracion import *

class Tuberia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/tuberia.png").convert()
        self.image.set_colorkey(COLOR_BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO//2
        self.rect.bottom = ALTO
