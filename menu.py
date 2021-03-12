import pygame
#from game import *
from button import *

class Menu():
    def __init__(self, game, title, bgColor, btnTextArray, fontSize, textColorArray,
        plainColorArray, highlightedColorArray, centeredPositionArray, actionArray):
        self.game = game
        self.buttons = pygame.sprite.Group()
        for t, tc, pc, hc, cp, a in zip(btnTextArray, textColorArray, plainColorArray,
                                        highlightedColorArray, centeredPositionArray, actionArray):
            self.buttons.add(Button(t, fontSize, tc, pc, hc, cp, a, self.game))

        self.title = createText(title, fontSize * 4, WHITE, BLUE)
        _, _, self.titlex, self.titley = self.title.get_rect()
        self.titleCoords = ((self.game.width - self.titlex) // 2, self.game.height * 0.1)
        self.bgColor = bgColor

    def draw(self, surface):
        surface.blit(self.title, self.titleCoords)
        # self.buttons.draw(surface)

    def update(self, event):
        self.game.screen.fill(self.bgColor)
        self.buttons.update(event)
        # self.buttons.draw(self.game.screen)
        # self.game.screen.blit(self.title, self.titleCoords)

    
