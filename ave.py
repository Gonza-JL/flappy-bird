import pygame
from configuracion import *

class Ave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/ave.png").convert()
        self.image.set_colorkey(COLOR_BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO//3
        self.rect.bottom = ALTO//2
        self.vuelo = -10
