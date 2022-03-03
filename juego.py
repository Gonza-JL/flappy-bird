import pygame, sys, random
from ave import *
from tuberia import *
from fondo import *
from suelo import *
from configuracion import *

class Juego():
    def __init__(self):
        self.finalizado = False
        self.gravedad = 0.9
        self.velocidadGravedad = 0
        self.puntaje = 0
        self.repSonidoGameOver = 0
        self.ave = Ave()

        # Inicializa listas de fondo y suelo
        self.fondo = [Fondo(0), Fondo(ANCHO)]
        self.suelo = [Suelo(0), Suelo(ANCHO)]
        
        # Inicializa las tuberias
        tuberias = []
        for i in range(0, 4, 2):
            tuberias.append(Tuberia("data/tuberia superior.png"))
            tuberias.append(Tuberia("data/tuberia inferior.png"))
            tuberias[i].rect.bottom = ALTO//2.55 #235
            tuberias[i+1].rect.bottom = ALTO * 1.55 #930
            tuberias[i].rect.centerx += i * 150
            tuberias[i+1].rect.centerx += i * 150
        self.tuberias = tuberias

        # Agrega los sprites
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.fondo)
        for i in range(self.tuberias.__len__()):
            self.sprites.add(self.tuberias[i])
            self.sprites.add(self.suelo)
            self.sprites.add(self.ave)
    
def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption("Flappy bird")

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    fps = pygame.time.Clock()
    juego = Juego()
    
    while(True):
        fps.tick(60)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not juego.finalizado):
                juego.velocidadGravedad = juego.ave.vuelo
                SONIDO_AVE.play()
            elif(event.type == pygame.KEYDOWN and event.key == pygame.K_r and juego.finalizado):
                juego = Juego()
        
        if(not juego.finalizado):

            # Actualiza la gravedad y el vuelo del ave
            juego.velocidadGravedad += juego.gravedad
            juego.ave.rect.bottom += juego.velocidadGravedad
            juego.ave.actualizar()

            # Actualiza el puntaje a mostrar y el mensaje de game over
            puntajeTXT = FUENTE_MEDIANA.render(str(int(juego.puntaje)), True, COLOR_BLANCO)
            gameOver = FUENTE_GRANDE.render("Game Over", True, COLOR_BLANCO)
            reinicioTXT = FUENTE_MEDIANA.render("presione R para", True, COLOR_BLANCO)
            reinicioTXT2 = FUENTE_MEDIANA.render("volver a jugar", True, COLOR_BLANCO)

            # Suma 1 punto cuando el ave pasa una tuberia
            for i in range(juego.tuberias.__len__()):
                if(juego.ave.rect.right == juego.tuberias[i].rect.right):
                    juego.puntaje += 0.5
                    SONIDO_PUNTAJE.play()

            # Simula el movimiento del ave
            for i in range(juego.tuberias.__len__()):
                juego.tuberias[i].movimiento()

            # Mueve en el eje Y, al azar, a las tuberias
            for i in range(0, juego.tuberias.__len__(), 2):
                if(juego.tuberias[i].rect.centerx < -100):
                    randomSup = random.randint(85, 385)
                    randomInf = randomSup + 695
                    juego.tuberias[i].rect.bottom = randomSup
                    juego.tuberias[i+1].rect.bottom = randomInf

            # Verifica si el ave choco con el suelo o si salio de la pantalla
            for i in range(juego.suelo.__len__()):
                if(juego.ave.rect.bottom >= juego.suelo[i].rect.y):
                    juego.ave.rect.bottom = juego.suelo[i].rect.y
                    juego.finalizado = True 
            if(juego.ave.rect.bottom <= 0):
                juego.finalizado = True

            # Verifica si el ave choco con alguna tuberia
            for i in range(juego.tuberias.__len__()):
                if(juego.ave.colisionConTuberia(juego.tuberias[i])):
                    juego.finalizado = True

            # Mover fondo y suelo
            moverListSprites(juego.fondo)
            moverListSprites(juego.suelo)

            juego.sprites.update()
            juego.sprites.draw(ventana) # Dibuja los sprites
            ventana.blit(puntajeTXT, [10, 2]) # Dibuja el puntaje
        else:
            # Reproduce el sonido de game over
            if(juego.repSonidoGameOver == 0):
                SONIDO_GAMEOVER.play()
                juego.repSonidoGameOver += 1

            # Dibuja el mensaje de game over
            pygame.draw.rect(ventana, COLOR_NEGRO, [0, ALTO/3, ANCHO, 120], 0)
            ventana.blit(gameOver, [30, ALTO/3])
            ventana.blit(reinicioTXT, [15, ALTO/3 + 50])
            ventana.blit(reinicioTXT2, [20, ALTO/3 + 80])
        pygame.display.flip()

def moverListSprites(list):
        for i in range(list.__len__()):
            if(list[i].rect.x + list[i].rect.width <= 0):
                list[i].rect.x = ANCHO-4
            else:
                list[i].rect.x -= VELOCIDAD_CAMARA

if __name__ == "__main__":
    main()