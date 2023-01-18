from Menu import *
import pygame
from pygame.locals import *
import sys
from mainpy import *




def welcomeScreen1(FPS):
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH / 5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message1'].get_width())+280)

    messagey = int(SCREENHEIGHT * -0.15)#0.18

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
               # pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['daymode'], (0, 0))#daymode==message1
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message1'], (messagex, messagey))
                pygame.display.update()
                FPSCLOCK.tick(FPS)