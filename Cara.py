import pygame, sys
from pygame.locals import *

AMPLE = 1000
ALT = 1000
TAMANY = (AMPLE,ALT)

NOM_FINESTRA = "Dibuix"
TAMANY = (AMPLE,ALT)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLUE_DORAEMON = (0,161,254)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
VIOLET = (148,0,211)
GREY = (128,128,128)
MARRON = (128,0,0)
BLACK = (0,0,0)
OLIVE = (134,139,73)
CYAN = (0,255,255)
PINK = (255,153,204)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)
WHITE = (255,255,255)

pygame.init()
font = pygame.font.SysFont(None,280)
img = font.render("STOP", True, WHITE)

pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption(NOM_FINESTRA)
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)
    pygame.draw.circle(pantalla,BLUE_DORAEMON, (500,500),200)
    pygame.draw.ellipse(pantalla, BLUE_DORAEMON, (350, 400, 300, 300))
    pygame.draw.circle(pantalla, WHITE, (500,550), 150)
    pygame.draw.circle(pantalla, WHITE, (450, 480), 30)
    pygame.draw.circle(pantalla, WHITE, (550, 480), 30)
    pygame.draw.circle(pantalla, BLUE_DORAEMON, (450, 480), 15)
    pygame.draw.circle(pantalla, BLUE_DORAEMON, (550, 480), 15)
    pygame.draw.circle(pantalla, RED, (500, 530), 20)
    pygame.draw.rect(pantalla, WHITE, (450, 550, 100, 30))
    pygame.draw.rect(pantalla, WHITE, (460, 560, 80, 10))
    pygame.draw.rect(pantalla, RED, (400, 650, 200, 30))
    pygame.draw.rect(pantalla, YELLOW, (420, 660, 160, 10))

    pygame.display.update()
