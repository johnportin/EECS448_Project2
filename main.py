import pygame
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
