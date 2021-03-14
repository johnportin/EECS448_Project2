import sys
import pygame.freetype

BLUE = (106, 159, 181)
DARKBLUE = (0, 0, 55)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
LIGHTGREY = (197, 212, 219)
DARKGREY = (145, 157, 163)

ASPECTRATIO = 16 / 9

pygame.init()

info = pygame.display.Info()

if info.current_w / info.current_h < ASPECTRATIO:
	WINDOWWIDTH = info.current_w - 100
	WINDOWHEIGHT = int(info.current_w  / ASPECTRATIO) - 100
else:
	WINDOWHEIGHT = info.current_h-100 # 1670
	WINDOWWIDTH =  int(ASPECTRATIO * WINDOWHEIGHT)


BTNHEIGHT = int(WINDOWHEIGHT / 15)
BTNWIDTH = BTNHEIGHT * 6
BTNSPACING = 1.5
FONTSIZE = int(BTNHEIGHT / 2.5)

BTNWIDTH_SMALL = int(BTNHEIGHT * 1)
BTNHEIGHT_SMALL = int(BTNHEIGHT * 1)
FONTSIZE_SMALL = int(BTNHEIGHT_SMALL / 2.5)




#850
boardSize = (WINDOWWIDTH/2) - 100 # 750

# I stole this function from (somewhere) GIVE CREDIT

def createText(text, fontSize, textcolor, bgcolor):
    font = pygame.freetype.SysFont("Courier", fontSize, bold=True)
    surface, rect = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface
    # return surface.convert_alpha()

def quitGame():
    pygame.quit()
    sys.exit()



def defaultAction():
    print('no action defined')
