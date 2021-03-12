import pygame
#from game import *
from button import *

class Menu():
    def __init__(self, game, title, bgColor, btnTextArray, fontSize, textColorArray,
        plainColorArray, highlightedColorArray, centeredPositionArray, actionArray):
        self.buttons = pygame.sprite.Group()
        for t, tc, pc, hc, cp, a in zip(btnTextArray, textColorArray, plainColorArray,
                                        highlightedColorArray, centeredPositionArray, actionArray):
            print(t, tc, pc, hc, cp, a)
            self.buttons.add(Button(t, fontSize, tc, pc, hc, cp, a))
        self.bgColor = bgColor
        self.game = game





    def update(self):
        self.game.screen.fill(self.bgColor)
        self.buttons.update(pygame.mouse.get_pos())
        self.buttons.draw(self.game.screen)
