import pygame

"""
Questions to ask:
-confusion on what this class actually needs to accomplish
-event handler is in main. Should it be moved here?
-what function does this class need to make once it gets info?

ToDo:
-figure out which position is being clicked if required.
-pass position on to next function.
"""


#Gets the top event
event = pygame.event.get()

#Checks if the event is triggered by a mouse click
if event.type == pygame.MOUSEBUTTONDOWN:
	#Checks if the left mouse button is clicked
	if pygame.mouse.get_pressed[0]:
		#assigns x & y with the current position of the mouse.
		x = pygame.mouse.get_pos[0]()
		y = pygame.mouse.get_pos[1]()