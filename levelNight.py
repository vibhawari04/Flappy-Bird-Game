from pygame import *
import pygame
from button import *
from welcomeNight import *
from maingameNight import *
from Menu import *
from mainpy import *



#****************************************************************************************************************



#****************************************************************************************************************


def levelscreen():
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))
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
                     welcomeScreen(40)
                     mainGame(40)
                elif b2.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     welcomeScreen(50)
                     mainGame(50)
                elif b3.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     welcomeScreen(70)
                     mainGame(70)

        pygame.display.update()