import sys
import pygame.freetype

# I stole this function from (somewhere) GIVE CREDIT

def createText(text, fontSize, textcolor, bgcolor):
    font = pygame.freetype.SysFont("Courier", fontSize, bold=True)
    surface, rect = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface.convert_alpha()

def quitGame():
    pygame.quit()
    sys.exit()

def startAction():
    print('start')
