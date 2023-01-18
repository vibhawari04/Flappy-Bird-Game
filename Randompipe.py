from Menu import *
import pygame
from mainpy import *

def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT / 3

    y2 = offset + random.randrange(0, int(SCREENHEIGHT - 1.2 * offset))

    pipeX = SCREENWIDTH + 10  # distance between pipes
    y1 = pipeHeight - y2 + offset

    # pipe is a list and this get random pipe function return the list of upper pipe and lower pipe
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper Pipe
        {'x': pipeX, 'y': y2}  # lower Pipe
    ]
    return pipe