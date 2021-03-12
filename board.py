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

		self.letters = ["A","B","C","D","E","F","G","H","I","J"]
		self.numbers = ["1","2","3","4","5","6","7","8","9","10"]
		
		# Retrieve Assets
		self.assetsList = {}
		self.assetNameKeys = ["BS 1","BS 2","BS 3","BS 4","BS 5","BS 6","hit","miss"]
		dir_path = os.path.dirname(os.path.realpath(__file__))
		assetsFolder = glob.glob(dir_path + "/Assets/" + "*")
		for asset in assetsFolder:
			print(asset)
			for key in self.assetNameKeys:
				if(asset.find(key) != -1):
					self.assetsList[key] = asset

		self.surface.fill((83,209,212))

		# For testing
		png = self.assetsList["BS 2"]
		pos = self.coordToBoard((8,1))
		self.ships.add(Piece(png, pos))

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

	def addShips():
		pass

	# Shows ships on board
	def showShips(self):
		self.ships.draw(self.surface)
		self.drawBoard()

	# Hides ships
	def hideShips(self):
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
		y = self.surface.get_height() -coord[1]*75 # 770 - coord[1]*75
		return((x,y))
		
# We may need to use this
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

					x = x / (pygame.display.get_window_size()[0] / 10)
					y = y / (pygame.display.get_window_size()[1] / 10)

					if x >= 0:
						if x <= 1:
							xVal = "A"
						elif x <= 2:
							xVal = "B"
						elif x <= 3:
							xVal = "C"
						elif x <= 4:
							xVal = "D"
						elif x <= 5:
							xVal = "E"
						elif x <= 6:
							xVal = "F"
						elif x <= 7:
							xVal = "G"
						elif x <= 8:
							xVal = "H"
						elif x <= 9:
							xVal = "I"
						elif x <= 10:
							xVal = "J"
						else:
							print("x click out of screen")
					else:
						print("x click out of screen")

					if y >= 0:
						if y <= 1:
							yVal = "1"
						elif y <= 2:
							yVal = "2"
						elif y <= 3:
							yVal = "3"
						elif y <= 4:
							yVal = "4"
						elif y <= 5:
							yVal = "5"
						elif y <= 6:
							yVal = "6"
						elif y <= 7:
							yVal = "7"
						elif y <= 8:
							yVal = "8"
						elif y <= 9:
							yVal = "9"
						elif y <= 10:
							yVal = "10"
						else:
							print("y click out of screen")
					else:
						print("y click out of screen")

					running = False
					return (xVal, yVal)
