import pygame
from configuracion import *

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/bird.png").convert()
        self.image.set_colorkey(COLOR_BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO//3
        self.rect.bottom = ALTO//2
        self.velocidad_y = 0
        self.tiempo_volando = 0
        self.tiempo_cayendo = 0

    def update(self):
        self.velocidad_y = 0
        keystate = pygame.key.get_pressed()
        if(keystate[pygame.K_SPACE] and self.tiempo_volando < 5):
            self.velocidad_y += 10
            self.tiempo_volando += 1
        else:
            self.velocidad_y -= 5
            if(self.tiempo_cayendo > 3):
                self.tiempo_volando = 0
                self.tiempo_cayendo = 0
            self.tiempo_cayendo += 1
        self.rect.y -= self.velocidad_y

