import pygame
from Menu import *
import sys
from welcomeDay import *
from maingameDay import *
import Menu
from button import *
from mainpy import *



def levelscreen1():
    #screen initiallize
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    # draw the surface of the window / bilt the image on the creen
    SCREEN.blit(GAME_SPRITES['daymode'], (0, 0))
    b1 = button(screen, (200, 100), "level 1",80,"black on gray")
    b2 = button(screen, (200, 300), "level 2",80,"black on sky blue")
    b3 = button(screen, (200, 500), "level 3",80,"black on pink")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     welcomeScreen1(40)
                     mainGame1(40)
                elif b2.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     welcomeScreen1(50)
                     mainGame1(50)
                elif b3.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     welcomeScreen1(70)
                     mainGame1(70)

        pygame.display.update()



