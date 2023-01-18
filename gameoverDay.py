import sys
from Menu import *
import pygame
from button import *
import Menu
from mainpy import *

def gameover1(score):
    GAME_SOUNDS['gameover1'].play()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    SCREEN.blit(GAME_SPRITES['gameover1'], (-310,-150))
    b1 = button(screen, (100, 550), "Quit",70,"black on sky blue")
    b2 = button(screen, (400, 550), "Retry",70,"black on sky blue")
    running = True

    while running:


        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                #pygame.quit()
                running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    GAME_SOUNDS['button'].play()
                    running = False
                    #pygame.quit()
                    sys.exit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    GAME_SOUNDS['button'].play()
                    GAME_SOUNDS['gameover1'].stop()
                    Menu.menu()
        pygame.display.update()
    pygame.quit()