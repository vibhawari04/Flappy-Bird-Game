from Randompipe import *
from Menu import *
import pygame
from mainpy import *


def isCollide(playerx, playery, upperPipes, lowerPipes):
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()  # height of the rotated pipe
        if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < \
                GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False