import pygame
from button import *
from auxx import *

info = pygame.display.Info()

class Menu():
    def __init__(self, title, bgColor, btnTextArray, fontSize, textColorArray,
        plainColorArray, highlightedColorArray, centeredPositionArray, dim, actionArray):
        self.buttons = pygame.sprite.Group()
        for t, tc, f, pc, hc, cp, d, a in zip(btnTextArray, textColorArray,
                                              fontSize, plainColorArray,
                                              highlightedColorArray, centeredPositionArray,
                                              dim, actionArray):
            self.buttons.add(Button(t, f, tc, pc, hc, cp, d, a))
        self.title = createText(title, FONTSIZE * 4, WHITE, BLUE)
        _, _, self.titlex, self.titley = self.title.get_rect()
        #self.titleCoords = ((800 - self.titlex) // 2, 600 * 0.1)
        self.titleCoords = ((WINDOWWIDTH - self.titlex) / 2, 50)
        self.bgColor = bgColor

    def update(self, screen):
        screen.fill(self.bgColor)
        self.buttons.update(screen)

    def draw(self, surface):
        surface.blit(self.title, self.titleCoords)
