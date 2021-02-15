
import pygame
# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1000, 500))

# Title and Icon
pygame.display.set_caption("Battleship")
icon = pygame.image.load('img.png')
pygame.display.set_icon(icon)



# Game Loop
running=True
while running:
    # Basically event listener
    for event in pygame.event.get():
        # Allows you to exit pygame screen
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 128, 128))
    pygame.display.update()
