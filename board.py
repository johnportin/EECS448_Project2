from time import sleep
import pygame
import glob
import os

from pygame import event

pygame.init()

class Piece(pygame.sprite.Sprite):
	def __init__(self,png,pos):
		super(Piece,self).__init__()
		self.image = pygame.image.load(png)
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		pygame.Surface.set_colorkey(self.image,[0,0,0])

	def update(self,move):
		self.rect.topleft = move

class Board:
	def __init__(self, screen, pos):
		self.screen = screen
		self.surface = pygame.Surface((750, 750))
		self.markers = pygame.sprite.Group() # Array of hit/miss markers
		self.ships = pygame.sprite.Group() # Array of ship sprites
		self.pos = pos

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

		self.surface.fill((83,209,212))

	#Used to draw the initial board           
	def drawBoard(self):
		# Gridlines and labels
		for x in range(0,11):
			xPos = (x)*750/10
			pygame.draw.line(self.surface, (0,0,0), (xPos,0), (xPos,750))

		for y in range(0,11):
			yPos = (y)*750/10
			pygame.draw.line(self.surface, (0,0,0), (0,yPos), (750,yPos))

		textType = pygame.font.Font('freesansbold.ttf', 20)
		for letter in self.letters:
			textSurf, textRect = self.text_objects(letter, textType)
			x = ord(letter) - 65
			xpos = x*750/10 + self.pos[0] + 37.5
			textRect.center = (xpos, 825) # Make this flexible
			self.screen.blit(textSurf,textRect)

		for number in self.numbers:
			textSurf, textRect = self.text_objects(number, textType)
			x = int(number) - 1
			ypos = 760- x*750/10 # Make this flexible
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
		pos = self.coordToBoard(coord)
		
		self.markers.add(Piece(png, pos))
		self.drawBoard()

	def addShips(self, length, pos, orientation, hover):
		asset = "BS_V " if orientation == "vertical" else "BS "
		asset += str(length)
		ship = Piece(self.assetsList[asset], self.coordToBoard(pos))

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

	# Hides ships
	def hideShips(self):
		self.drawShips = False
		bg = pygame.Surface((750, 750))
		bg.fill((83,209,212))
		self.ships.clear(self.surface, bg)
		self.drawBoard()

	#Used to place text on screen
	def text_objects(self,text,font):
		textSurface = font.render(text,True,(0,0,0))
		return textSurface, textSurface.get_rect()

	#Quick helper function for getting board coordinates
	def coordToBoard(self,coord):
		x = coord[0]*75 # 87.5 + coord[0]*75
		y = self.surface.get_height() - (coord[1]+1)*75 # 770 - coord[1]*75
		return((x,y))
		
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
