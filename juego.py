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
    juegoFinalizado = False

    ave = Ave()
    suelo = pygame.image.load("data/suelo.png").convert()
    sueloY= ALTO-30
    fondo = pygame.image.load("data/fondo.png").convert()
    tuberiaSup = Tuberia("data/tuberia superior.png")
    tuberiaInf = Tuberia("data/tuberia inferior.png")
    tuberiaSup.rect.bottom = ALTO//2.55
    tuberiaInf.rect.bottom = ALTO * 1.55

    sprites = pygame.sprite.Group()
    sprites.add(tuberiaSup)
    sprites.add(tuberiaInf)
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
        
        if(juegoFinalizado == False):
            velocidadGravedad += gravedad
            ave.rect.bottom += velocidadGravedad

            if(ave.rect.bottom >= sueloY + 5):
                ave.rect.bottom = sueloY + 5
                juegoFinalizado = True
            elif(ave.rect.bottom <= 0):
                juegoFinalizado = True

            sprites.update()
            ventana.blit(fondo, [0, 0])
            sprites.draw(ventana)
            ventana.blit(suelo, [0, sueloY])
            pygame.display.flip()

if __name__ == "__main__":
    iniciarPygame()
    main()