'''Initially draws a 10 by 10 white grid to the screen. Clicked squares
turn green.'''

import pygame
#Start the engine
pygame.init()

# Define constants
BLACK = (0, 0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Window size
size = (255, 255)
#Window title
pygame.display.set_caption("Grid-backed Game")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Size variables for each grid location
width = 20
height = 20
#Space between each grid location
margin = 5

#Create the grid (matrix)
grid = [[[] for i in range(10)] for j in range(10)]

#Main Loop
while not done:
    
    #A tuple for the mouse coordinates
    mouse_pos = pygame.mouse.get_pos()

    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            #Flag that the main loop needs to be terminated
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Convert the x-value of the mouse's position to the corresponding column
            mouse_x = mouse_pos[1]//(height+margin)
            #Convert the y-value of the mouse's position to the corresponding row
            mouse_y = mouse_pos[0]//(width+margin)
            # print('Row:', mouse_x, 'Column:', mouse_y)
            grid[mouse_x][mouse_y] = 1

    #Fill the screen with black
    screen.fill(BLACK)
    
    for i in range(10):
        #Have a border of 'margin' units on the top and the bottom the grid
        y = margin + i*(height+margin)
        for j in range(10):
            #Have a border of 'margin' units on the left and right of the grid
            x = margin + j*(width+margin)
            #Draw a white square 'width' px wide and 'height' px tall at (x,y)
            if grid[i][j] == 1:
                pygame.draw.rect(screen, GREEN, [x, y, width, height])    
            else:
                pygame.draw.rect(screen, WHITE, [x, y, width, height])

    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the engine properly
pygame.quit()