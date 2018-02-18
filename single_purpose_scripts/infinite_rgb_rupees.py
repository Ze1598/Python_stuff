import pygame
from random import randint, choice
#Single-color rupees mode is commented out in tripple quotes
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
pygame.display.set_caption("INFINTE RGB RUPEES")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Randomize if it's monochromatic rupees or RGB rupees
modes = ('RGB', 'MONO')
mode = choice(modes)
#Number of rupees to be created initially
num_rupees = 200
if mode == 'RGB':
    
    rupees_list = []
    for i in range(num_rupees):
        top_left = [randint(0,size[0]), randint(0,size[1])]
        top_right = [top_left[0]+15, top_left[1]]
        top_middle = [(top_left[0]+top_right[0])//2, (top_left[1]+top_right[1])//2 - 10]
        bottom_left = [top_left[0], top_left[1]+20]
        bottom_right = [top_right[0], top_right[1]+20]
        bottom_middle = [top_middle[0], top_middle[1]+40]
        rupees_list.append([top_left, top_middle, top_right, bottom_right, bottom_middle, bottom_left])
else:
    rupees_list = []
    for i in range(num_rupees):
        top_left = [randint(0,size[0]), randint(0,size[1])]
        top_right = [top_left[0]+15, top_left[1]]
        top_middle = [(top_left[0]+top_right[0])//2, (top_left[1]+top_right[1])//2 - 10]
        bottom_left = [top_left[0], top_left[1]+20]
        bottom_right = [top_right[0], top_right[1]+20]
        bottom_middle = [top_middle[0], top_middle[1]+40]
        color = choice((RED, BLUE, GREEN))
        rupees_list.append([[top_left, top_middle, top_right, bottom_right, bottom_middle, bottom_left], color])

#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated

    #Fill the screen with black
    screen.fill(BLACK)

    #Draw the rupees
    if mode == 'RGB':
        for i in range(len(rupees_list)):
            pygame.draw.polygon(screen, choice((RED, BLUE, GREEN)), rupees_list[i],4)
            #Move each vertex of each rupee 7 units down
            for j in range(len(rupees_list[i])):
                rupees_list[i][j][1] += 7
            #If rupees are going out of vertical bounds create new ones to be drawn at the top
            if rupees_list[i][4][1] > size[1]:
                top_left = [randint(0,size[0]), randint(-50,-10)]
                top_right = [top_left[0]+15, top_left[1]]
                top_middle = [(top_left[0]+top_right[0])//2, (top_left[1]+top_right[1])//2 - 10]
                bottom_left = [top_left[0], top_left[1]+20]
                bottom_right = [top_right[0], top_right[1]+20]
                bottom_middle = [top_middle[0], top_middle[1]+40]
                rupees_list[i] = [top_left, top_middle, top_right, bottom_right, bottom_middle, bottom_left]
    else:
        for i in range(len(rupees_list)):
            pygame.draw.polygon(screen, rupees_list[i][1], rupees_list[i][0],4)
            #Move each vertex of each rupee 7 units down
            for j in range(len(rupees_list[i][0])):
                rupees_list[i][0][j][1] += 7
            #If rupees are going out of vertical bounds create new ones to be drawn at the top
            if rupees_list[i][0][4][1] > size[1]:
                top_left = [randint(0,size[0]), randint(-50,-10)]
                top_right = [top_left[0]+15, top_left[1]]
                top_middle = [(top_left[0]+top_right[0])//2, (top_left[1]+top_right[1])//2 - 10]
                bottom_left = [top_left[0], top_left[1]+20]
                bottom_right = [top_right[0], top_right[1]+20]
                bottom_middle = [top_middle[0], top_middle[1]+40]
                color = choice((RED, BLUE, GREEN))
                rupees_list[i] = [[top_left, top_middle, top_right, bottom_right, bottom_middle, bottom_left], color]



    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
    #FPS count
    clock.tick(30)

#Quit the program properly
pygame.quit()
