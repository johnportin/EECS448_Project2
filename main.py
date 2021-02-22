import pygame
from .game_logic import run

# Initialize the pygame 
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1000, 500))

# Setup.txt parser
setupfile = open('setup.txt')
asset = setupfile.readline()
try:
    # Title and Icon
    pygame.display.set_caption(asset)
    asset = setupfile.readline()
    icon = pygame.image.load(asset)
    pygame.display.set_icon(icon)

    # Futher file processing will go here

except ValueError:
    print("Error: reading from file")

setupfile.close()
#calls run from game_logic to start game
run()
