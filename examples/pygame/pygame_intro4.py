#Script for opening images and sounds and interacting with them

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
pygame.display.set_caption("Fourth PyGame Program")
#Create a window of size 'size'
screen = pygame.display.set_mode(size)

#Variable to keep the main loop running
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Image from http://ProgramArcadeGames
#We use the convert() method to convert the image to a format Python can work more easily with (from the Image class)
background_image = pygame.image.load("assets\\saturn_family1.jpg").convert()
#Image from http://programarcadegames.com/index.php?lang=en&chapter=bitmapped_graphics_and_sound
player_image = pygame.image.load("assets\\player.png").convert()
#"Tell" the program to make a color "transparent" (not display that color)
player_image.set_colorkey(BLACK)
#Sound from http://programarcadegames.com/index.php?lang=en&chapter=bitmapped_graphics_and_sound
click_sound = pygame.mixer.Sound("assets\\laser5.ogg")

#Main Loop
while not done:
    #Check for user events
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    #Fill the screen with black
    screen.fill(BLACK)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    #Display 'background_image'
    screen.blit(background_image, [0,0])
    #Display 'player_image'
    screen.blit(player_image, [x,y])
    
    #This waits to display the screen until the program has finished drawing
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()