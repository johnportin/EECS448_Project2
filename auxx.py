import sys
import pygame.freetype

# setup game parameters and global variables

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

# Determine height and width of game given actual screen resolution
# and desired aspect ratio
if info.current_w / info.current_h < ASPECTRATIO:
	WINDOWWIDTH = info.current_w - 100
	WINDOWHEIGHT = int(info.current_w  / ASPECTRATIO) - 100
else:
	WINDOWHEIGHT = info.current_h-100 # 1670
	WINDOWWIDTH =  int(ASPECTRATIO * WINDOWHEIGHT)

# Determine size for larger buttons
BTNHEIGHT = int(WINDOWHEIGHT / 15)
BTNWIDTH = BTNHEIGHT * 6
BTNSPACING = 1.5
FONTSIZE = int(BTNHEIGHT / 2.5)

# Determine size for small buttons (3 for every 1 large button)
BTNWIDTH_SMALL = int(BTNHEIGHT * 1)
BTNHEIGHT_SMALL = int(BTNHEIGHT * 1)
FONTSIZE_SMALL = int(BTNHEIGHT_SMALL / 2.5)

difficultyDict = {0: 'Easy', 1: 'Medium', 2: 'Hard'}
playerAI = {0: 'Player', 1: 'AI'}


#850
boardSize = (WINDOWWIDTH/2) - 100 # 750

FAQ_SIZE = None
FAQ_FONTSIZE = int(FONTSIZE * 0.55)
FAQ	= 	"""Welcome to battleship! Prepare for war!
\n    How To Play \n
In this game, each player can place up to six ships on their board.\n
Players take turns attacking enemy vessels. \n
The game is over when someone loses their whole fleet.\n
\n    GameSetup \n
Select to play against a human or computer with the Player button.\n
Select the number of ships to place with the '# of Ships' button.\n
If playing against the computer, change the difficulty with 'Difficulty' button. \n
You can change the volume with the two 'BGM' and 'SFX' buttons.\n
\n
Good luck sardine, you're going to need it!"""



def createParagraph(text, fontSize, textcolor, bgcolor, paragraphSize):
	font = pygame.freetype.SysFont("Courier", fontSize, bold = True)

	# Create surface for faq, and set background to transparent
	paragraphSurf = pygame.Surface(paragraphSize)
	paragraphSurf.set_colorkey((0, 0, 0))

	splitLines = text.splitlines()

	# Calculate offset for lines
	offSet = (paragraphSize[1] - len(splitLines) * (fontSize + 1)) // 2

	# Iterate over splitLines and blit rendered line onto paragraph surface
	for idx, line in enumerate(splitLines):
		currentTextline, _ = font.render(text=line, fgcolor=WHITE, bgcolor=BLUE)
		currentPosition = ((paragraphSize[0] - currentTextline.get_width()) // 2, #x-coordinate
                  idx * fontSize + offSet) #y-coordinate
		paragraphSurf.blit(currentTextline, currentPosition)

	return paragraphSurf, paragraphSize


def createText(text, fontSize, textcolor, bgcolor):
    font = pygame.freetype.SysFont("Courier", fontSize, bold=True)
    surface, rect = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface

def quitGame():
    pygame.quit()
    sys.exit()

def defaultAction():
    print('no action defined')
