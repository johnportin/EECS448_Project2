from time import sleep
import pygame
import glob
import os

from pygame import event

pygame.init()

class Piece(pygame.sprite.Sprite):
	def __init__(self,png,pos):
		super(Piece,self).__init__() # What does this do - Joshua
		self.surf = pygame.image.load(png)
		self.rect = self.surf.get_rect()
		self.rect.center = pos
		pygame.Surface.set_colorkey(self.surf,[0,0,0])

	def update(self,move):
		self.rect.center = move

class Board:
	# Put new board stuff here

	def __init__(self, screen):
		self.screen = screen
		self.sprites = []
		self.ships = [] # Locations of intact ships
		self.boardSize = pygame.Rect(50, 50, 750, 750)

		self.letters = ["A","B","C","D","E","F","G","H","I","J"]
		self.numbers = ["1","2","3","4","5","6","7","8","9","10"]
		
		# initialization stuff tbd, might go in game
		# Retrieve Assets
		self.assetNameKeys = ["BS 1","BS 2","BS 3","BS 4","BS 5","BS 6","hit","miss"]
		dir_path = os.path.dirname(os.path.realpath(__file__))
		#with my key in a dictionary. 

		assetsFolder = glob.glob(dir_path + "/Assets/" + "*")
		self.assetsList = {}
		for asset in assetsFolder:
			# idk if this part even works
			for key in self.assetNameKeys:
				if(asset.find(key) != -1):
					self.assetsList[key] = asset
		
	### ======================================== ###
	### Carryover functions, not fully implemented ###
	### ======================================== ###

	#Used to draw the initial board           
	def drawBoard(self):
		# Draws the screen
		#self.screen.fill((128,128,128)) # Background color
		pygame.draw.rect(self.screen,(83,209,212),self.boardSize) # Board itself

		# Gridlines and labels
		for x in range(0,11):
			xPos = 50+(x)*75
			pygame.draw.line(self.screen, (0,0,0), (xPos,50), (xPos,800))

		for x in range(0,11):
			yPos = 50+(x)*75
			pygame.draw.line(self.screen, (0,0,0), (50,yPos), (800,yPos))

		textType = pygame.font.Font('freesansbold.ttf', 20)
		for letter in self.letters:
			textSurf, textRect = self.text_objects(letter, textType)
			x = ord(letter) - 65
			pos = x*75 + 87
			textRect.center = (pos, 825)
			self.screen.blit(textSurf,textRect)

		for number in self.numbers:
			textSurf, textRect = self.text_objects(number, textType)
			x = int(number) - 1
			pos = 760- x*75
			textRect.center = (25, pos)
			self.screen.blit(textSurf,textRect)

	#Creates a sprite at coordinate to represent hit or miss
	def addShot(self, mark, coord):
		print(str(mark) + " at " + str(coord))
		if (mark == "hit"):
			png = self.assetsList["hit"]
		else:
			png = self.assetsList["miss"]
		pos = self.coordToBoard(coord)
		
		sprite = Piece(png, pos)
		self.screen.blit(sprite.surf, sprite.rect)
		#self.sprites.append()

	# Places ships on board
	def placeShips(self,ships,player):
		pass

	# Hides ships
	def hideShips(self,ships,player):
		pass

	#Used to place text on screen
	def text_objects(self,text,font):
		textSurface = font.render(text,True,(0,0,0))
		return textSurface, textSurface.get_rect()

	#Quick helper function for getting board coordinates
	def coordToBoard(self,coord):
		x = 87.5 + coord[0]*75
		y = 770 - coord[1]*75
		return((x,y))
		


# Old board class
class pyBoard:
	assetNameKeys = ["BS 1","BS 2","BS 3","BS 4","BS 5","BS 6","hit","miss"]
	ships = ["x1","x2","x3","x4","x5","x6"]
	
	def __init__(self,assetsFolderPath = "/Assets/",screen = (850,850)):
		#PNG Info. Basically, I'm just digging through the provided assets folder and seeing if
		#it gives me anything containing my assetNameKeys, if it finds them, it stores that path
		dir_path = os.path.dirname(os.path.realpath(__file__))
		#with my key in a dictionary. 
		print(dir_path)
		print(assetsFolderPath)

		assetsFolder = glob.glob(dir_path + assetsFolderPath + "*")
		self.assetsList = {}
		for asset in assetsFolder:
			for key in self.assetNameKeys:
				if(asset.find(key) != -1):
					self.assetsList[key] = asset
		
		for ass in self.assetsList.keys():
			print(ass)

		#CleanPlate info. Basically, this will be what I use to draw an empty board each frame.
		#I May make this customizable later
		self.screenDim = screen
		self.boardDim = p.Rect(50,50,screen[0]-100, screen[1]-100)
		self.lineSpace = screen[0]/10
		self.letters = ["A","B","C","D","E","F","G","H","I","J"]
		self.numbers = ["1","2","3","4","5","6","7","8","9","10"]

		#Live Info
		self.spriteDictP1 = {}
		self.spritePosP1 = {}
		self.spriteDictP2 = {}
		self.spritePosP2 = {}
		self.coordDict = {}
		self.gameBegin = 1#1 = game setup, 0 = game ready
		self.turn = 0 

		#creates an empty dictionary for checking whats at a given coordinate, used with piece dictionary
		for x in range(10):
			for y in range(10):
				c = str(x) + "," + str(y)
				self.coordDict[c] = ""
	

	#Used to place text on screen
	def text_objects(self,text,font):
		textSurface = font.render(text,True,(0,0,0))
		return textSurface, textSurface.get_rect()

	#Quick helper function for getting board coordinates
	def coordToBoard(self,coord):
		x = 87.5 + coord[0]*75
		y = 770 - coord[1]*75
		return((x,y))

	# #Unused for time being :(
	# def createPieceDicts(self, player):
	# 	for piece in self.ships:
	# 		for x in range(8):
	# 			key = str(piece) + str(player)
	# 			if piece == "pW":
	# 				coordX = x
	# 				coordY = 6
	# 				pos = (coordX,coordY)
	# 			if piece == "pG":
	# 				coordX = x
	# 				coordY = 1
	# 				pos = (coordX,coordY)
	# 			self.spritePos[key] = pos
	# 			cKey = str(pos[0]) + "," + str(pos[1])
	# 			self.coordDict[cKey] = key


	

	# #Function used to redraw the board per frame of game
	# def createCleanPlate(self):
	# 	self.drawBoard()
	# 	self.placeGridLabels()
		

	#Function used to update the board per game interraction
	def __updateBoard(self,player):
		self.screen.fill((0,0,0))
		self.createCleanPlate()
		if(player):
			for x in self.spritePosP1:
				self.screen.blit(self.spriteDictP1[x].surf, self.spriteDictP1[x].rect)
		else:
			for x in self.spritePosP2:
				self.screen.blit(self.spriteDictP2[x].surf, self.spriteDictP2[x].rect)


	#Prints current game info
	def printInfo(self):
		print(self.coordDict)
		print(self.spritePos)

		
	#Called on start of game, contains info from setup.txt
	def beginGame(self,packet):
		self.screen = p.display.set_mode(size = (850,850))
		gameName = packet[0]
		p.display.set_caption(gameName)
		icon = p.image.load(packet[1])
		p.display.set_icon(icon)
		self.gameBegin = 1
		self.createCleanPlate()
		p.display.flip()

	

	#prompts user to exit
	def quitGame(self):
		run = True
		print("X out of the window now")
		while run:
			for event in p.event.get():
				if event.type == p.QUIT:
					print("trying to quit")
					run = False
		p.quit()

	#Bublic facing update call, will eventually use extra info 
	def updateBoard(self,mark,player,coord):
		self.addShot(mark,coord,player)
		self.__updateBoard(player)
		p.display.flip()

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
