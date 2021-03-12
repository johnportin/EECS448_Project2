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


class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1670, 850)) #(800, 600)
		self.screen.fill((128,128,128)) # Background color
		self.clock = pygame.time.Clock()
		self.currentMenu = None # Use this to switch between menus
		self.gameState = {
			"state": "start",
			"turn": "n/a"
		}

		# Might not keep these.
		self.board1 = Board(self.screen, (50,50))
		self.board2 = Board(self.screen, (900,50))

		# Set icon and app window title
		pygame.display.set_caption("Battleship")
		pygame.display.set_icon(pygame.image.load("Assets/icon.png"))

	def gameLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			mainMenu.game = self
			#mainMenu.update()
			pygame.display.flip()
			self.clock.tick(60)

		# Dunno where to put this
		if (gameState.state == "something"):
			# Execute a function
			pass


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

	def setup():
		# Implement drag and drop to place ships
		pass

	def guess():
		# Guess
		print("Guess a battleship location")
		column_number = letters_to_numbers[getMouse()[0]]
		row_number = int(getMouse()[1]) - 1

		# Check valid
		# Is hit or miss?
		# Update board

	def gameOver():
		# Clear everything
		# Change to victory menu
		pass


game = Game()

mainMenu = Menu(game = game,
				title = 'Main Menu',
				bgColor = BLUE,
				btnTextArray = ['start', 'options', 'quit'],
				fontSize = 20,
				textColorArray = [WHITE] * 3,
				plainColorArray = [DARKBLUE] * 3,
				highlightedColorArray = [RED] * 3,
				centeredPositionArray = [(400, 300), (400, 400), (400, 500)],
				actionArray = [None] * 3)
game.gameLoop()
