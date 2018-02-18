#This script draws a stickman and allows the user to move it using the arrow keys

import pygame
#Start the engine
pygame.init()

def draw_stick_figure(screen, x, y):
    #Head
    pygame.draw.ellipse(screen, BLACK,[1+x,y,10,10],0)
    #Legs
    pygame.draw.line(screen, BLACK, [5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
    #Body
    pygame.draw.line(screen, BLACK, [5+x,17+y], [5+x,7+y], 2)
    #Arms
    pygame.draw.line(screen, BLACK, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,7+y], [1+x,17+y], 2)

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
pygame.display.set_caption("Second PyGame Program")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Speed, in pixels, per frame
x_speed = 0
y_speed = 0
 
#Current position (starting position)
x_coord = 10
y_coord = 10

#Make the mouse invisible
pygame.mouse.set_visible(False)

#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        
        #If user clicked Close
        if event.type == pygame.QUIT:
            done = True #Flag that the main loop needs to be terminated
        
        #User pressed down a key
        elif event.type == pygame.KEYDOWN:
            #Figure out if it was an arrow key; If so, adjust speed
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        
        #User let up a key
        elif event.type == pygame.KEYUP:
            #If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    #Move the object according to the speed vector
    #The if conditions make sure the stickman doesn't go out of bounds
    if (x_coord + x_speed > 0) and (x_coord + x_speed < size[0]-10):
        x_coord += x_speed
    if (y_coord + y_speed > 0) and (y_coord + y_speed < size[1]-27):
        y_coord += y_speed

    #Fill the screen with white
    screen.fill(WHITE)
    
    #Draw a stickman at (x_coord, y_coord)
    draw_stick_figure(screen, x_coord, y_coord)

    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()