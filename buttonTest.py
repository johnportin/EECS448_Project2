import pygame
import sys
import pygame.freetype
from pygame.sprite import RenderUpdates
from pygame.sprite import Sprite

from button import *
from auxx import *

pygame.freetype.init()


BLUE = (106, 159, 181)
DARKBLUE = (0, 0, 55)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BTNHEIGHT = 50
BTNWIDTH = 100

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

btn1 = Button('BTN1', 20, WHITE, DARKBLUE, RED, (400, 300))
btn2 = Button('BTN2', 20, WHITE, DARKBLUE, RED, (400, 400))
btn3 = Button('BTN3', 20, WHITE, DARKBLUE, RED, (400, 500))

buttons = pygame.sprite.Group()
buttons.add({btn1, btn2, btn3})

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #print(pygame.mouse.get_pos())


    screen.fill(BLUE)
    buttons.update(pygame.mouse.get_pos())
    buttons.draw(screen)
    pygame.display.flip()
    clock.tick(60)
