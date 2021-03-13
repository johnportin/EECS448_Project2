from time import sleep
import pygame
import glob
import os

from pygame import event

pygame.init()

info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
WINDOWWIDTH = screen_width-100
WINDOWHEIGHT = screen_height-100
boardSize = (WINDOWWIDTH/2) - 100

#Quick helper function for getting board coordinates
def coordToBoard(coord):
	# print('coord = ' + str(coord))
	# print(type(coord), 'x = ', type(coord[0]), 'y = ', type(coord[1]))
	x = coord[0] * (boardSize/10)
	y = boardSize - (coord[1] + 1) * (boardSize/10)
	# x = coord[0]*75 # 87.5 + coord[0]*75
	# y = boardSize - (int(coord[1])+1)*75 # 770 - coord[1]*75
	return((x,y))

class Marker(pygame.sprite.Sprite):
	def __init__(self,png,pos):
		super(Marker,self).__init__()
		self.image = pygame.image.load(png)
		self.rect = self.image.get_rect()
		self.rect.topleft = coordToBoard(pos[0])
		pygame.Surface.set_colorkey(self.image,[0,0,0])

class Ship(pygame.sprite.Sprite):
	def __init__(self,png,pos):
		super(Ship,self).__init__()
		self.image = pygame.image.load(png)
		self.rect = self.image.get_rect()
		self.rect.topleft = coordToBoard(pos[0])
		pygame.Surface.set_colorkey(self.image,[0,0,0])
		self.pos = pos

class Board:
	def __init__(self, screen, pos):
		self.screen = screen
		self.surface = pygame.Surface((boardSize, boardSize))

		self.markers = pygame.sprite.Group() # Array of hit/miss markers
		self.ships = pygame.sprite.Group() # Array of ship sprites
		self.pos = pos
		self.rect = self.surface.get_rect(topleft = self.pos)

		self.drawShips = True
		self.letters = ["A","B","C","D","E","F","G","H","I","J"]
		self.numbers = ["1","2","3","4","5","6","7","8","9","10"]

		# Retrieve Assets
		self.assetsList = {}
		self.assetNameKeys = ["BS 1","BS 2","BS 3","BS 4","BS 5","BS 6", "BS_V 1","BS_V 2","BS_V 3","BS_V 4","BS_V 5","BS_V 6","hit","miss"]
		dir_path = os.path.dirname(os.path.realpath(__file__))
		assetsFolder = glob.glob(dir_path + "/Assets/" + "*")
		for asset in assetsFolder:
			# print(asset)
			for key in self.assetNameKeys:
				if(asset.find(key) != -1):
					self.assetsList[key] = asset

		self.surface.fill((83,209,212)) #what is this ah oops -katelyn

	#Used to draw the initial board
	def drawBoard(self):
		# Gridlines and labels
		for x in range(0,11):
			xPos = (x)*boardSize/10
			pygame.draw.line(self.surface, (0,0,0), (xPos,0), (xPos,boardSize))

		for y in range(0,11):
			yPos = (y)*boardSize/10
			pygame.draw.line(self.surface, (0,0,0), (0,yPos), (boardSize,yPos))

		textType = pygame.font.Font('freesansbold.ttf', 20)
		#Drawing the letters on axis
		for letter in self.letters:
			textSurf, textRect = self.text_objects(letter, textType)
			x = ord(letter) - 65
			#xpos = x*boardSize/10 + self.pos[0] + 37.5
			xpos = x*boardSize/10 + self.pos[0] + (boardSize*.05)
			#textRect.center = (xpos, 825) # Make this flexible
			textRect.center = (xpos, 25) # Make this flexible
			self.screen.blit(textSurf,textRect)

		#Drawing the numbers on axis
		for number in self.numbers:
			textSurf, textRect = self.text_objects(number, textType)
			x = int(number) - 1
			#ypos = 760 - x*boardSize/10 # Make this flexible
			ypos = boardSize + (boardSize*.05) - x*boardSize/10 # Make this flexible
			textRect.center = (self.pos[0]-25, ypos) # Make this flexible
			self.screen.blit(textSurf,textRect)

		if self.drawShips:
			self.ships.draw(self.surface)
		self.markers.draw(self.surface)
		self.screen.blit(self.surface, self.pos)

	#Creates a sprite at coordinate to represent hit or miss
	def addShot(self, mark, coord):
		print(str(mark) + " at " + str(coord))
		if (mark == "hit"):
			png = self.assetsList["hit"]
		else:
			png = self.assetsList["miss"]

		self.markers.add(Marker(png, coord))
		self.drawBoard()

	def addShips(self, length, positions, orientation, hover):
		asset = "BS_V " if orientation == "vertical" else "BS "
		asset += str(length)
		ship = Ship(self.assetsList[asset], positions)

		if hover:
			# Transparency
			ship.image.set_alpha(100)

			# offset position
			ship.rect[0] += self.pos[0]
			ship.rect[1] += self.pos[1]
			self.screen.blit(ship.image, ship.rect)
		else:
			self.ships.add(ship)


	# Shows ships on board
	def showShips(self):
		self.drawShips = True
		self.drawBoard()
		pygame.display.flip()

	# Hides ships
	def hideShips(self):
		self.drawShips = False
		bg = pygame.Surface((boardSize, boardSize))
		bg.fill((83,209,212))
		self.ships.clear(self.surface, bg)
		self.drawBoard()
		pygame.display.flip()

	#Used to place text on screen
	def text_objects(self,text,font):
		textSurface = font.render(text,True,(0,0,0))
		return textSurface, textSurface.get_rect()

def getMouse():
	"""
	getMouse
			* @pre: That the window has been clicked on
			* @post: gets and returns proper X and Y values for corresponding
				//row and column
			* @param: None
			* @description: creates game loop and event listener the checks for
				//mousebuttondown then gets mouse x and y position and uses board
				//dimentions to create proper number of rows and columns according
				//to x and y set  and returns proper values for xVal and yVal
	"""
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				# Checks if the left mouse button is clicked
				if pygame.mouse.get_pressed()[0]:
					# assigns x & y with the current position of the mouse.
					x = pygame.mouse.get_pos()[0]
					y = pygame.mouse.get_pos()[1]

					running = False
					#print((x, y))
					return (x, y)
