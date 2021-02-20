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
def getMouse():
	#Checks if the left mouse button is clicked
	if pygame.mouse.get_pressed()[0]:
		#assigns x & y with the current position of the mouse.
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

		return(xVal, yVal)
