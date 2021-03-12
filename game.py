import pygame
import sys
import pygame.freetype
from pygame.sprite import RenderUpdates
from pygame.sprite import Sprite

from button import *
from aux import *


from menu import Menu

from button import Button


pygame.freetype.init()


BLUE = (106, 159, 181)
DARKBLUE = (0, 0, 55)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BTNHEIGHT = 50
BTNWIDTH = 100


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.currentMenu = None # Use this to switch between menus




    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            mainMenu.game = self
            mainMenu.update()
            pygame.display.flip()
            self.clock.tick(60)

game = Game()

mainMenu = Menu(game = game,
                title = 'Main Menu',
                bgColor = BLUE,
                btnTextArray = ['start', 'options', 'quit'],
                fontSize = 20,
                textColorArray = [WHITE] * 3,
                plainColorArray = [DARKBLUE] * 3,
                highlightedColorArray = [RED] * 3,
                centeredPositionArray = [(400, 300), (400, 400), (400, 500)],
                actionArray = [None] * 3)

game.gameLoop()
