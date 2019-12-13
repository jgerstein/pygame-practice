import sys
import pygame
import random

# Initialize pygame so it runs in the background and manages things
pygame.init()

# colors
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 128, 0)
yellow = pygame.Color('#ffff00')
green = pygame.Color('#00ff00')
c = pygame.Color(0, 0, 255)
change = 1

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    print(c.r)
    if random.random() < .05:
        c.r += change
        c.b -= change
    if c.r >= 255:
        c.r = 255
        change = -abs(change)
    elif c.r <= 0:
        c.r = 0
        change = abs(change)
    screen.fill( c )

    pygame.display.flip()