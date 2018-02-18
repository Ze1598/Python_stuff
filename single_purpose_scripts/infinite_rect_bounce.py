import pygame, math
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

#Initial rectangle coordinates
rect_x, rect_y = 50, 50
#Rectangle's moving speeds
rect_change_x, rect_change_y = 5, 5
 
#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated

    #Fill the screen with black
    screen.fill(BLACK)
    
    #Draw a rectangle (a square in this case)
    #Draw it starting at (50,50), 50px wide and 50px tall
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, 50, 50))
    pygame.draw.rect(screen, RED, (rect_x+10, rect_y+10, 30, 30))
    
    #Move the rectangle's coordinates by these values, each frame
    rect_x += rect_change_x
    rect_y += rect_change_y
    #If the rectangle is about to go out of the screen, bounce it in the opposite direction
    if rect_x > 650 or rect_x < 0:
        rect_change_x *= -1
    if rect_y > 450 or rect_y < 0:
        rect_change_y *= -1


    #This waits to display the screen until the program has finished drawing.
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()