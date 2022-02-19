from time import sleep
import pygame, sys, random
from ave import *
from tuberia import *
from fondo import *
from suelo import *
from configuracion import *

def iniciarPygame():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption("Flappy bird")
    
def main():
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    fps = pygame.time.Clock()
    fuente = pygame.font.Font("data/Flappy-Bird.ttf", 40)
    juegoFinalizado = False
    gravedad = 0.9
    velocidadGravedad = 0
    puntaje = 0

    ave = Ave()
    fondo = [Fondo(0), Fondo(ANCHO)]
    suelo = [Suelo(0), Suelo(ANCHO)]
    tuberias = inicializarTuberias()

    # Agrego los sprites
    sprites = pygame.sprite.Group()
    sprites.add(fondo)
    for i in range(tuberias.__len__()):
        sprites.add(tuberias[i])
    sprites.add(suelo)
    sprites.add(ave)
    
    while(True):
        fps.tick(60)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                velocidadGravedad = ave.vuelo
                ave.image = pygame.image.load("data/ave2.png")
        
        if(not juegoFinalizado):
            velocidadGravedad += gravedad
            ave.rect.bottom += velocidadGravedad

            # Actualizo el puntaje a mostrar
            texto = fuente.render(str(int(puntaje)), True, COLOR_BLANCO)

            # Suma 1 punto cuando el ave pasa una tuberia
            for i in range(tuberias.__len__()):
                if(ave.rect.right == tuberias[i].rect.right):
                    puntaje += 0.5

            # Simula el movimiento del ave
            for i in range(tuberias.__len__()):
                tuberias[i].movimiento()

            # Mueve en el eje Y, al azar, a las tuberias
            for i in range(0, tuberias.__len__(), 2):
                if(tuberias[i].rect.centerx < -100):
                    randomSup = random.randint(85, 385)
                    randomInf = randomSup + 695
                    tuberias[i].rect.bottom = randomSup
                    tuberias[i+1].rect.bottom = randomInf

            # Verifica si el ave choco con el suelo o si salio de la pantalla
            for i in range(suelo.__len__()):
                if(ave.rect.bottom >= suelo[i].rect.y):
                    ave.rect.bottom = suelo[i].rect.y
                    juegoFinalizado = True 
            if(ave.rect.bottom <= 0):
                juegoFinalizado = True

            # Verifica si el ave choco con alguna tuberia
            for i in range(tuberias.__len__()):
                if(ave.colisionConTuberia(tuberias[i])):
                    juegoFinalizado = True

            # Mover fondo y suelo
            moverListSprites(fondo)
            moverListSprites(suelo)

            ave.actualizar()
            sprites.update()
            sprites.draw(ventana) # Dibuja los sprites
            ventana.blit(texto, [10, 10]) # Dibuja el puntaje
            pygame.display.flip()

def inicializarTuberias():
    tuberias = []
    for i in range(0, 4, 2):
        tuberias.append(Tuberia("data/tuberia superior.png"))
        tuberias.append(Tuberia("data/tuberia inferior.png"))
        tuberias[i].rect.bottom = ALTO//2.55 #235
        tuberias[i+1].rect.bottom = ALTO * 1.55 #930
        tuberias[i].rect.centerx += i * 150
        tuberias[i+1].rect.centerx += i * 150
    return tuberias

def moverListSprites(list):
    for i in range(list.__len__()):
        if(list[i].rect.x + list[i].rect.width <= 0):
            list[i].rect.x = ANCHO-4
        else:
            list[i].rect.x -= VELOCIDAD_CAMARA

if __name__ == "__main__":
    iniciarPygame()
    main()