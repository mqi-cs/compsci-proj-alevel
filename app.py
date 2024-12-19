print('Hello World!')

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
# This line creates a window of 500 width, 500 height

pygame.display.set_caption("WORDLE!!!")   #change window name

run = True

while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

pygame.quit()  # If we exit the loop this will execute and close our game
