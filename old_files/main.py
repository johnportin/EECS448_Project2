import pygame
from game_logic import run

# Initialize the pygame 
pygame.init()

# Create the screen
#screen = pygame.display.set_mode((1000, 500))

# Setup.txt parser
setupfile = open('setup.txt')
SetupPacket = setupfile.readlines()
setupfile.close()

run(SetupPacket)
