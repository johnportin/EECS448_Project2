import pygame
import sys
import pygame.freetype
from pygame.sprite import RenderUpdates
from pygame.sprite import Sprite

from auxx import *

# BLUE = (106, 159, 181)
# DARKBLUE = (0, 0, 55)
# RED = (255, 50, 50)
# WHITE = (255, 255, 255)
# GREEN = (0, 200, 0)
# BTNHEIGHT = 50
# BTNWIDTH = 300

class Button(Sprite):
    def __init__(self, text, fontSize, textColor, plainColor, highlightedColor,
                  centeredPosition, dim, action = None):
        Sprite.__init__(self)
        # Can we deal with tons of attributes better?
        self.name = text
        self.font = pygame.font.SysFont("Courier", fontSize, bold=True)
        self.text = text
        self.plainText = text
        self.renderedText = None
        self.dim = dim
        self.fontSize = fontSize
        self.textColor = DARKBLUE
        self.plainColor = WHITE
        self.hoverColor = LIGHTGREY
        self.clickedColor = DARKGREY
        self.mouseOver = False
        self.clicked = False
        self.centeredPosition = centeredPosition
        self.clickedText = None # Maybe use to change the text upon clicking?
        self.rect = pygame.Rect((centeredPosition, self.dim))
        self.rect.center = self.centeredPosition
        self.action = action # implement a callback feature
        self.hoverText = None # renders a aslightly larger version of the normal text
        self.renderText()

    # Render and assign text & hoverText (& maybe clickedText?) for button
    def renderText(self):
        if self.text:
            self.text = self.font.render(self.text, 1, self.textColor)
            x, y= self.text.get_rect()[2], self.text.get_rect()[3]
            self.hoverText = pygame.transform.scale(self.text, (int(x * 1.2), int(y * 1.2)))

    # Checks whether button has been clicked
    def checkEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.onClick(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.onRelease(event)

    def onClick(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True

    def onRelease(self, event):
        if self.rect.collidepoint(event.pos) and self.clicked:
            self.action()
        self.clicked = False

    def checkMouseOver(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.mouseOver = True
        else:
            self.mouseOver = False

    # Update the button depending on its current state
    def update(self, surface):
        text = self.text
        self.checkMouseOver()
        color = self.plainColor
        if self.clicked:
            color = self.clickedColor
            text = self.hoverText # self.clickedText
        elif self.mouseOver:
            color = self.hoverColor
            text = self.hoverText

        # Create button surface and give it an outline
        surface.fill(pygame.Color(DARKBLUE), self.rect)
        surface.fill(color, self.rect.inflate(-4, -4))
        if self.text:
            # Center text and blit onto screen
            textRect = text.get_rect(center = self.rect.center)
            surface.blit(text, textRect)
