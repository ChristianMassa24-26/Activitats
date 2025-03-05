import pygame, sys
from pygame.locals import *

AMPLE = 1000
ALT = 1000
TAMANY = (AMPLE,ALT)

ACER = (172,178,180) # Color acero
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
BLAU = (0,0,255)
VERD = (0,255,0)
GROC = (255,255,0)

pygame.init()
font = pygame.font.SysFont(None,280)
img = font.render("STOP", True, BLANC)

pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('SENYAL DE STOP')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    rectangle1 = pygame.Rect(400, 600, 200, 400)
    pygame.draw.rect(pantalla, ACER, rectangle1)
    pygame.draw.polygon(pantalla, VERMELL, ((355,150),(645,150),(850,355),(850,645),(645,850),(355,850),(150,645),(150,355),(355,150)))
    pygame.draw.polygon(pantalla, BLANC, ((365,160),(635,160),(840,365),(840,635),(635,840),(365,840),(160,635),(160,365),(365,160)))
    pygame.draw.polygon(pantalla, VERMELL, ((375, 170), (625, 170), (830, 375), (830, 625), (625, 830), (375, 830), (170, 625), (170, 375), (375, 170)))
    pantalla.blit(img, (250, 410)) # TEXTO "STOP"

    pygame.display.update()
