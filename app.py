print('Hello World!')

import pygame
pygame.init()


height = 750
width = 600


win = pygame.display.set_mode((width, height))
# This line creates a window of 600 width, 750 height

pygame.display.set_caption("WORDLE!!!")   #change window name



colummn_lenght= 6   #wordle dimesnions for later use
row_lenght= 5          























run = True

while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

pygame.quit()  # If we exit the loop this will execute and close our game #

