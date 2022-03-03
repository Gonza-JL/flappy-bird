import pygame
pygame.init()
pygame.font.init()

ANCHO = 400
ALTO = 600
VELOCIDAD_CAMARA = 4

COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

FUENTE_MEDIANA = pygame.font.Font("data/fuente.ttf", 30)
FUENTE_GRANDE = pygame.font.Font("data/fuente.ttf", 40)

SONIDO_AVE = pygame.mixer.Sound("data/sonido de aleteo.ogg")
SONIDO_GAMEOVER = pygame.mixer.Sound("data/sonido de game over.ogg")
SONIDO_PUNTAJE = pygame.mixer.Sound("data/sonido de puntaje.ogg")