#Template for a pygame script: initializes the script, defines colors, window size and title,\
#defines an event for when the user closes the window, fills the screen, flips it and\
#locks the script at 60 fps

import pygame
#Start the engine
pygame.init()

# Define constants
BLACK = (0, 0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PI = 3.141592653

#Window size
size = (700, 500)
#Window title
pygame.display.set_caption("First PyGame Program")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

 
#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated

    #Fill the screen with black
    screen.fill(BLACK)
    
    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()