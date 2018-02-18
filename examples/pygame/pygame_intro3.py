#Script for using a joystick as the controller
#A joystick will return two floating point values.
#If the joystick is perfectly centered it will return (0, 0).
#If the joystick is fully up and to the left it will return (-1, -1).
#If the joystick is down and to the right it will return (1, 1). 
#If the joystick is somewhere in between, values are scaled accordingly.

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
pygame.display.set_caption("Third PyGame Program")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Current position
x_coord = 10
y_coord = 10
 
#Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    #No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    #Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
 
#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated

    #As long as there is a joystick
    if joystick_count != 0:
    
        #This gets the position of the axis on the game controller
        #It returns a number between -1.0 and +1.0
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
    
        #Move x according to the axis. We multiply by 10 to speed up the movement.
        #Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
        x_coord += int(horiz_axis_pos * 10)
        y_coord += int(vert_axis_pos * 10)

    #Fill the screen with black
    screen.fill(WHITE)
    
    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()