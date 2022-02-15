import pygame, sys, random
from ave import *
from tuberia import *
from configuracion import *

def iniciarPygame():
    pygame.init
    pygame.mixer.init()
    pygame.display.set_caption("Flappy bird")
    
def main():
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    fps = pygame.time.Clock()

    ave = Ave()
    tuberia = Tuberia()

    sprites = pygame.sprite.Group()
    sprites.add(tuberia)
    sprites.add(ave)
    
    gravedad = 0.9
    velocidadGravedad = 0

    while(True):
        fps.tick(60)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                velocidadGravedad = ave.vuelo
            
        velocidadGravedad += gravedad
        ave.rect.bottom += velocidadGravedad

        if(ave.rect.bottom >= ALTO):
            ave.rect.bottom = ALTO
            gravedad = 0
        elif(ave.rect.bottom <= 0):
            ave.rect.bottom = 0
            gravedad = 0

        sprites.update()
        ventana.fill(COLOR_NEGRO)
        sprites.draw(ventana)
        pygame.display.flip()

if __name__ == "__main__":
    iniciarPygame()
    main()