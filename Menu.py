import random  # For generating random numbers
import sys  # We will use sys.exit to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports
from levelNight import *

from maingameNight import *
from levelDay import *
from maingameDay import *
from welcomeDay import *
from pygame import *
from button import *
from welcomeNight import *
from mainpy import *
import levelNight





def modescreen():
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    SCREEN.blit(GAME_SPRITES['mode'], (-20, 0))
    b1 = button(screen, (125, 250), "   Day Mode  ", 70, "black on pink")
    b2 = button(screen, (125, 350), " Night Mode ", 70, "black on sky blue")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                #pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     levelscreen1()
                     welcomeScreen1(40)
                     mainGame1(40)

                elif b2.collidepoint(pygame.mouse.get_pos()):
                     GAME_SOUNDS['button'].play()
                     levelNight.levelscreen()
                     welcomeScreen(50)
                     mainGame(40)
        pygame.display.update()


def start():

    modescreen()

def menu():

    GAME_SOUNDS['Welcome'].play()
    # Initialise a window or screen for display
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    # to set a image for back ground of screen
    SCREEN.blit(GAME_SPRITES['start'], (-25, -30))
    b1 = button(screen, (100, 500), "Quit",70,"black on pink")
    b2 = button(screen, (400, 500), "Start",70,"black on pink")


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                sys.exit()



            if event.type == pygame.MOUSEBUTTONDOWN:
                if b2.collidepoint(pygame.mouse.get_pos()):
                    GAME_SOUNDS['button'].play()
                    start()
                elif b1.collidepoint(pygame.mouse.get_pos()):
                    GAME_SOUNDS['button'].play()
                    running = False
                    # for the termination of game
                    sys.exit()


            # If the user presses space or up key, start the game for them
        #it will update the  display screen
        pygame.display.update()
    #pygame.quit()




if __name__ == "__main__":
    pygame.init()  # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()  # it is a count for no of blit per seconds

    #title of the window
    pygame.display.set_caption('Flappy Bird Game')

    while True:
        menu()



