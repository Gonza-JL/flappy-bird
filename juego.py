import pygame, sys
from bird import *
from configuracion import *

pygame.init
pygame.mixer.init()
pygame.display.set_caption("Flappy bird")
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

sprites = pygame.sprite.Group()
bird = Bird()
sprites.add(bird)

while(True):
    reloj.tick(60)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()

    sprites.update()
    ventana.fill(COLOR_NEGRO)
    sprites.draw(ventana)
    pygame.display.flip()