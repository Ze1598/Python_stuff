import pygame
from random import randint
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
size = (900, 600)
#Window title
pygame.display.set_caption("First PyGame Program")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

snow_list = []
for i in range(350):
    x = randint(0,size[0])
    y = randint(0,size[1])
    snow_list.append([x, y])

#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated

    #Fill the screen with black
    screen.fill(BLACK)
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 3)
        snow_list[i][1] += 7
        #Create more snow for when the old one goes out of bounds
        if snow_list[i][1] > size[1]:
            x = randint(0, size[0])
            y = randint(-50, -10)
            snow_list[i][0], snow_list[i][1] = x, y


    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
    #FPS count
    clock.tick(30)

#Quit the program properly
pygame.quit()
