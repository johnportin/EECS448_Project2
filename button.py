import pygame
import sys
import pygame.freetype
from pygame.sprite import RenderUpdates
from pygame.sprite import Sprite

from aux import createText

BLUE = (106, 159, 181)
DARKBLUE = (0, 0, 55)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BTNHEIGHT = 50
BTNWIDTH = 100

class Button(Sprite):
    def __init__(self, text, fontSize, textColor, plainColor, highlightedColor, centeredPosition, action = None):
        Sprite.__init__(self)
        self.mouseOver = False
        # self.textSurf = create_surface_with_text('text', fontSize, textColor, bgColor)
        # self.bgSurf = pygame.Surface((BTNWIDTH, BTNHEIGHT))
        # self.bgSurf.fill(DARKBLUE)
        # self.bgSurf.blit(self.textSurf, (25, 25)) # need to calculate center of button
        # self.image = self.bgSurf
        self.centeredPosition = centeredPosition

        plainText = createText(text, fontSize, textColor, plainColor)
        highlightedText = createText(text, fontSize, textColor, highlightedColor)

        plainSurf = pygame.Surface((BTNWIDTH, BTNHEIGHT))
        highlightedSurf = pygame.Surface((BTNWIDTH, BTNHEIGHT))

        plainSurf.fill(DARKBLUE)
        highlightedSurf.fill(RED)

        plainSurf.blit(plainText, (25, 25))
        highlightedSurf.blit(highlightedText, (25, 25))

        self.plainSurf = plainSurf
        self.highlightedSurf = highlightedSurf
        self.image = plainSurf
        self.pos = self.image.get_rect(center = centeredPosition)
        self.rect = self.pos
        self.action = action # implement a callback feature



    def update(self, mousePos):
        if self.pos.collidepoint(mousePos):
            self.image = self.highlightedSurf
        else:
            self.image = self.plainSurf


    def draw(self, surface):
        self.image.convert()
        surface.blit(self.image, self.pos)
