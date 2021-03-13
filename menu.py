import pygame
#from game import *
from button import *

info = pygame.display.Info()
WINDOWWIDTH = info.current_w-100 # 1670
WINDOWHEIGHT =  info.current_h-100 #850

class Menu():
    def __init__(self, title, bgColor, btnTextArray, fontSize, textColorArray,
        plainColorArray, highlightedColorArray, centeredPositionArray, actionArray):
        self.buttons = pygame.sprite.Group()
        for t, tc, pc, hc, cp, a in zip(btnTextArray, textColorArray, plainColorArray,
                                        highlightedColorArray, centeredPositionArray, actionArray):
            self.buttons.add(Button(t, fontSize, tc, pc, hc, cp, a
                                    ))
        self.title = createText(title, fontSize * 4, WHITE, BLUE)
        _, _, self.titlex, self.titley = self.title.get_rect()
        #self.titleCoords = ((800 - self.titlex) // 2, 600 * 0.1)
        self.titleCoords = ((WINDOWWIDTH - self.titlex) / 2, 50)
        self.bgColor = bgColor

    def draw(self, surface):
        surface.blit(self.title, self.titleCoords)
        # self.buttons.draw(surface)

    def update(self, screen):
        screen.fill(self.bgColor)
        self.buttons.update(screen)
        # self.buttons.draw(self.game.screen)
        # self.game.screen.blit(self.title, self.titleCoords)
