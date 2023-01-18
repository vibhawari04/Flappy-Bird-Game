from pygame import *
import pygame
from Menu import *


pygame.init()
FPSCLOCK = pygame.time.Clock()
SCREENWIDTH = 600
SCREENHEIGHT = 700
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.jpg'
BACKGROUND1 = 'gallery/sprites/daymode.png'
PIPE = 'gallery/sprites/pipe.png'
START = 'gallery/sprites/start.png'
GAMEOVER1 = 'gallery/sprites/gameover1.png'
GAMEOVER = 'gallery/sprites/gameover.png'
MODE = 'gallery/sprites/mode.png'

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 1
GAME_SPRITES = {'numbers':(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    ),
    'message':pygame.image.load('gallery/sprites/message.png').convert_alpha() ,
    'message1':pygame.image.load('gallery/sprites/message1.png').convert_alpha(),
    'pipe': (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha()) , # 180 -> angle
'background':pygame.image.load(BACKGROUND).convert_alpha(),
'start':pygame.image.load(START).convert_alpha(),
'daymode' : pygame.image.load(BACKGROUND1).convert_alpha(),
'gameover1': pygame.image.load(GAMEOVER1).convert_alpha(),
'gameover': pygame.image.load(GAMEOVER).convert_alpha(),
'mode': pygame.image.load(MODE).convert_alpha(),
'player': pygame.image.load(PLAYER).convert_alpha()
}
GAME_SOUNDS = {'gameover1' : pygame.mixer.Sound('gallery/audio/gameover1.wav'),
    'Welcome' : pygame.mixer.Sound('gallery/audio/Welcome.wav'),
   'button' : pygame.mixer.Sound('gallery/audio/button.wav'),
'die':pygame.mixer.Sound('gallery/audio/die.wav'),
'hit':pygame.mixer.Sound('gallery/audio/hit.wav'),
'point':pygame.mixer.Sound('gallery/audio/point.wav'),
'swoosh':pygame.mixer.Sound('gallery/audio/swoosh.wav'),
'wing':pygame.mixer.Sound('gallery/audio/wing.wav')
               }


