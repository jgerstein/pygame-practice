import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# make colors
red = pygame.Color(255, 0, 0)

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        print(event)
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()

    # fill the screen with color
    screen.fill(red)
    pygame.display.flip()