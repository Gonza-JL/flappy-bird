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
    sueloY= ALTO-30
    suelo = pygame.image.load("data/suelo.png").convert()
    fondo = pygame.image.load("data/fondo.png").convert()
    tuberias = inicializarTuberias()
    # MIN -150 MAX 150

    sprites = pygame.sprite.Group()
    for i in range(tuberias.__len__()):
        sprites.add(tuberias[i])
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

            for i in range(tuberias.__len__()):
                tuberias[i].movimiento()

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

def inicializarTuberias():
    tuberias = []
    for i in range(0, 4, 2):
        tuberias.append(Tuberia("data/tuberia superior.png"))
        tuberias.append(Tuberia("data/tuberia inferior.png"))
        tuberias[i].rect.bottom = ALTO//2.55
        tuberias[i+1].rect.bottom = ALTO * 1.55
        tuberias[i].rect.centerx += i * 150
        tuberias[i+1].rect.centerx += i * 150
        #if(i != 0):
            #tuberias[i].rect.bottom += 
            #tuberias[i+1].rect.bottom += 
    return tuberias

if __name__ == "__main__":
    iniciarPygame()
    main()