import pygame
import sys
import pygame.freetype
from pygame.sprite import RenderUpdates
from pygame.sprite import Sprite
from board import *

from button import *
from aux import *


from menu import Menu
from button import Button


pygame.freetype.init()

BLUE = (106, 159, 181)
DARKBLUE = (0, 0, 55)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BTNHEIGHT = 50
BTNWIDTH = 100
MAX_SHIPS = 3

WINDOWWIDTH = 800
WINDOWHEIGHT = 600




class Game:
	def __init__(self, width, height):
		pygame.init()
		self.width = width
		self.height = height
		#self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #(850, 850)
		self.screen = pygame.display.set_mode((1870, 850)) #(800, 600)
		self.screen.fill((128,128,128)) # Background color
		self.clock = pygame.time.Clock()

		# Might not keep these.
		self.board1 = Board(self.screen, (50, 50))
		self.board2 = Board(self.screen, (1100, 50))
		self.boards = {
			"board1": self.board1,
			"board2": self.board2
		}
		self.currentPlayer = 'board1'
		self.otherPlayer = 'board2'
		self.maxShips = MA
		self.bannedPositions = []
		self.allowedLengths = list(range(1, MAX_SHIPS+1))

		# Set icon and app window title
		pygame.display.set_caption("Battleship")
		pygame.display.set_icon(pygame.image.load("Assets/icon.png"))

		# Options
		self.mute = False
		self.difficulty = 0

		gameStates = {
			'mainMenu'	: 	Menu(
								title = 'Main Menu',
								bgColor = BLUE,
								btnTextArray = ['start', 'options', 'quit'],
								fontSize = 20,
								textColorArray = [WHITE] * 3,
								plainColorArray = [DARKBLUE] * 3,
								highlightedColorArray = [RED] * 3,
								centeredPositionArray = [(400, 300), (400, 400), (400, 500)],
								actionArray = [self.startAction, self.optionAction, quitGame]),

			'optionsMenu' : Menu(
								title = 'Options',
								bgColor = BLUE,
								btnTextArray = ['# ships', 'diff:' + difficultyDict[0], 'Return', 'Mute'],
								fontSize = 20,
								textColorArray = [WHITE] * 4,
								plainColorArray = [DARKBLUE] * 4,
								highlightedColorArray = [RED] * 4,
								centeredPositionArray = [(400, 200), (400, 300), (400, 400), (400, 500)],
								actionArray = [self.shipcountAction, self.difficultyAction, self.returnAction, self.muteAction]),
			'start'	:	None,
			'guessing'	:	None,
			'victory'	:	None,
			'shipSelect'	:	None,
			'turn'	:	None


		}

		self.gameStates = gameStates
		self.stateName = 'mainMenu'
		self.state = self.gameStates[self.stateName]
		self.done = False


	def changeState(self):
		self.state = self.gameStates[self.stateName]

	def gameLoop(self):
		while True:
			if self.stateName == 'mainMenu' or self.stateName == 'optionsMenu':
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					for button in self.state.buttons:
						button.checkEvent(event)
						print(self.state)
						# self.state.buttons.checkEvent(event)
				self.changeState()

			if self.stateName == 'start':
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
				self.board1.drawBoard()
				self.board2.drawBoard()
				self.setup()

			if self.stateName == 'guessing':
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.guess(event, self.currentPlayer, self.otherPlayer):
							if self.currentPlayer == 'board1':
								self.otherPlayer = 'board1'
								self.currentPlayer = 'board2'
							else:
								self.currentPlayer = 'board1'
								self.otherPlayer = 'board2'



			if self.state:
				self.state.update(self.screen)
				self.state.draw(self.screen)


			pygame.display.flip()
			self.clock.tick(60)



	# This functions get triggered by gameLoop depending on gameState
	def start():
		# Dunno if this will be useful, but templating.

		# self.screen = p.display.set_mode(size = (850,850))
		# self.createCleanPlate() # Replaced with Board.drawBoard()
		# p.display.flip()

		# Prompt for number of ships
		# This is from their code
		ships = input("Input number of ships to place:")
		while ships not in "123456":
			print("Wrong number! It should be 1, 2, 3, 4, 5, or 6")
			ships = input("Input number of ships to place:")
		return ships

	# You can't quit the game in this middle of this function
	def setup(self):
		# Player 1 places ships
		while len(self.allowedLengths) > 0:
			self.placeShip("board1")

		# Player 2 places ships
		self.board1.hideShips()
		self.bannedPositions = []
		self.allowedLengths = list(range(1, self.maxShips+1))
		while len(self.allowedLengths) > 0:
			self.placeShip("board2")

		self.stateName = 'guessing'
		self.changeState()


		# self.guess("board1", "board2")

	def setAllowedLengths(self):
		self.allowedLengths = list(range(1, self.maxShips))

	def placeShip(self, activeBoard): # might move this into board.py
		# Mouse click on square = origin of ship
		brd = "none"
		while (brd == "none"):
			pos, brd = coordToBoard(getMouse())

		# Hover - tries potential ships
		running = True
		while running:
			self.boards[activeBoard].drawBoard() # Clears the screen of any previous hovers

			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]

			hover, hover_board = coordToBoard((x,y))
			length, positions, orientation = self.isValidShip(pos, brd, hover, hover_board, activeBoard)

			if length:
				#print(length, position, orientation)
				# Draw transparent ship, make it go away when position changes
				self.boards[activeBoard].addShips(length, positions, orientation, True)
			pygame.display.flip()

			# Click - click valid, add ship. Click invalid, do nothing
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if length:
						self.boards[activeBoard].addShips(length, positions, orientation, False)
						self.boards[activeBoard].showShips()
						self.allowedLengths.remove(length)
						for pos in positions:
							self.bannedPositions.append(pos)

					running = False # Exits the loop

		# Some game logic stuff might go here

	# I am quarantining this ugly code
	def isValidShip(self, pos, brd, hover, hover_board, activeBoard):
		# Add exception later to where you can only place on the correct board
		if (brd == activeBoard) and (brd == hover_board): # Can't go off board
			# Horizontal Placement
			# Extra conditions here shouldn't be needed, but sometimes loop is buggy
			if (pos[1] == hover[1]):
				length = abs(pos[0] - hover[0]) + 1
				# Only one ship of each length and can't exceed max length
				if (length in self.allowedLengths):
					# Can't overlap other ships
					minX = pos[0] if pos[0] < hover[0] else hover[0]
					positions = []
					for x in range(0, length):
						positions.append((minX+x, pos[1]))
						if (minX+x, pos[1]) in self.bannedPositions:
							return False, False, False
					return length, positions, "horizontal"

			# Vertical Placement
			if (pos[0] == hover[0]):
				length = abs(pos[1] - hover[1]) + 1

				# Only one ship of each length and can't exceed max length
				if (length in self.allowedLengths):
					# Can't overlap other ships
					maxY = pos[1] if pos[1] > hover[1] else hover[1]
					positions = []
					for y in range(0, length):
						positions.append((pos[0], maxY-y))
						if (pos[0], maxY-y) in self.bannedPositions:
							return False, False, False
					return length, positions, "vertical"
		return False, False, False


	def guess(self, event, ownBoard, targetBoard):
		self.boards[ownBoard].showShips()
		self.boards[targetBoard].hideShips()

		mouseCoords = event.pos
		pos = coordToBoard(mouseCoords)
		print('target board rect = {}'.format(self.boards[targetBoard].testRect))

		valid = self.boards[targetBoard].rect.collidepoint(mouseCoords)
		for marker in self.boards[targetBoard].markers:
			if marker.rect.collidepoint(mouseCoords):
				valid = False

		# Is hit or miss?
		if valid:
			marker = "miss"
			for ship in self.boards[targetBoard].ships:
				for shipPos in ship.pos:
					if pos[0] == shipPos:
						marker = "hit"
			self.boards[targetBoard].addShot(marker, pos)
		print('valid = ' + str(valid))
		return valid

	def gameOver(self):
		# Clear everything
		# Change to victory menu
		pass

	def optionAction(self):
		self.stateName = 'optionsMenu'


	def returnAction(self):
		print('return called')
		self.stateName = 'mainMenu'

	def difficultyAction(self):
		self.difficulty += 1
		self.difficulty %= 3
		for button in self.state.buttons:
			if not button.name.find('diff'): # Changes the difficulty text (why need NOT?)
				button.text = difficultyDict[self.difficulty]
				button.renderText()

	def shipcountAction(self):
		self.maxShips = max((self.maxShips + 1) % 7, 1)
		for button in self.state.buttons:
			if not button.name.find('#'):
				button.text = str(self.maxShips)
				button.renderText()
		self.setAllowedLengths()
		print(self.maxShips)
		print(self.allowedLengths)

	def startAction(self):
		self.stateName = 'start'

	def muteAction(self):
		self.mute = not self.mute
		print("muted = " + str(self.mute))

def coordToBoard(coords):
	# Converts to a square on a board. Maybe turn into function.
	if (coords[0] >= game.boards["board1"].pos[0]) and (coords[0] <= game.boards["board1"].pos[0]+750) and (coords[1] >= game.boards["board1"].pos[1]) and (coords[1] <= game.boards["board1"].pos[1]+750):
		brd = "board1"
	elif (coords[0] >= game.boards["board2"].pos[0]) and (coords[0] <= game.boards["board2"].pos[0]+750) and (coords[1] >= game.boards["board2"].pos[1]) and (coords[1] <= game.boards["board2"].pos[1]+750):
		brd = "board2"
	else:
		return (0, 0), "none"

	row = int((coords[0] - game.boards[brd].pos[0]) / 75)
	col = int((750 - coords[1] + game.boards[brd].pos[1]) / 75)

	return (row, col), brd




difficultyDict = {0: 'easy', 1: 'hard', 2: 'impossible'}












game = Game(WINDOWWIDTH, WINDOWHEIGHT)


game.gameLoop()
