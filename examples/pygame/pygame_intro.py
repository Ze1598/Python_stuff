#Covers drawing shapes and text, drawing using the mouse position and basic stuff in general

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

def draw_stick_figure(screen, x, y):
    #Head
    pygame.draw.ellipse(screen, BLACK,[1+x,y,10,10],0)
    #Legs
    pygame.draw.line(screen, BLACK, [5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
    #Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
    #Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)

#Set to False hides the mouse cursor
pygame.mouse.set_visible(False)

#Main Loop
while not done:
    #Event loop
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked Close
            done = True #Flag that the main loop needs to be terminated
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
 
    #Game logic 
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    #Drawing code 
    #Clear the screen and set the screen background
    #This should be done before any drawing command is issued. 
    #Clearing the screen after the program draws graphics results\
    #in the user only seeing a blank screen.  
    screen.fill(WHITE)

    #Draw a line from (0,0) to (100, 100) in the screen, with 5 pixels of width
    #line(surface, color, start_pos, end_pos, width)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    
    #Draw a line from (250,125) to (300, 300) in the screen, with 3 pixels of width
    pygame.draw.line(screen, BLUE, [250,125], [300, 300], 3)
    
    #Draw a blue triangle, with vertices on (150,50), (175,75) and (200, 50)
    #polygon(surface, color, vertices, width)
    pygame.draw.polygon(screen, BLUE, [(150, 50), (175,75), (200, 50)])
    
    #Draw lines that start at the coordinate (0, 10+'y_offset') and end at (100, 110+'y_offset')
    #'y_offset' starts at zero and is incremented by 15 while it is smaller than 100
    for y_offset in range(0,100,15):
        pygame.draw.line(screen, RED, [0,10+y_offset], [100,110+y_offset], 3)
    
    #Draw lines using the sine and cosine functions as offsets
    for i in range(200):
        radians_x = i/20
        radians_y = i/6
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200 
        pygame.draw.line(screen, BLACK, [x,y], [x+5, y], 3)

    #Draw a rectangle: starts at (20,20), has 250px wide and 100px tall
    #rect(surface, color, dimensions, width)
    pygame.draw.rect(screen,BLACK,[20,20,250,100],2)

    #Draw an arc as part of an ellipse. Use radians to determine what angle to draw.
    #arc(surface, color, area_filled, start_angle, stop_angle, width)
    pygame.draw.arc(screen, GREEN, [100,100,250,200], PI/2, PI, 2)
    pygame.draw.arc(screen, BLACK, [100,100,250,200], 0, PI/2, 2)
    pygame.draw.arc(screen, RED, [100,100,250,200], 3*PI/2, 2*PI, 2)
    pygame.draw.arc(screen, BLUE, [100,100,250,200], PI, 3*PI/2, 2)
    
    #Create an object to hold the text's font, size and style (bold and/or italic)
    #SysFont(font_name, font_size, bold(T/F), italic(T/F))
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    #Only creates the text to appear on the screen
    #render(text, antialias(T/F), color)
    text = font.render("Hello World", True, BLACK)
    
    #Set the text to appear on (250,250)
    screen.blit(text, [450, 250])

    #Draw a stickman, centered at x,y
    # draw_stick_figure(screen, 300, 275)
    #Keep drawing a stickman at the mouse's position each frame
    draw_stick_figure(screen, mouse_x, mouse_y)
    
    #You must flip the display after you draw. 
    #The computer will not display the graphics as you draw them\
    #because it would cause the screen to flicker. 
    #This waits to display the screen until the program has finished drawing.
    pygame.display.flip()

    #Limit to 60 frames per second
    clock.tick(60)

#Quit the program properly
pygame.quit()