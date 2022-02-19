import pygame
from configuracion import *

class Suelo(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("data/suelo.png").convert()
        self.image.set_colorkey(COLOR_BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = ALTO-30