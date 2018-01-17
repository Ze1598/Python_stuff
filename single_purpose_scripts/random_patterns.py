'''From a square table, create a randomized image, starting at a random coordinate, that progressively grows bigger by \
filling adjacent coordinates.
The possible size for the image is randomized each time and at the end is printed the result without whitespaces.
Something to take into account: every time there\'s a coordinate, the first value represents the y axis and the second \
value represents the x axis. This is because of lists\' structures: you first acess the y axis for the table, and after \
that you access the x axis.'''

import random
#create the table (a 2D list)
canvas = [[[] for j in range(20)] for i in range(20)]
#generate coordinates for the first node
first_node = (random.randint(0,19), random.randint(0,19))
#pattern to "fill" the image
fill = '&'
#insert the first node in the canvas
canvas[first_node[1]][first_node[0]] = fill
#define how many nodes the image will can have 
#this isn't the actual value 99% of the time, but it's the number of iterations the script runs to fill a coordinate
max_size = random.randint(200,399)
#image starts at size 1
size = 1
#list to contain the coordinates of the used nodes
nodes_list = [first_node]
#get the coordinates of the latest created node
y = nodes_list[-1][0]
x = nodes_list[-1][1]
#directions to grow the image (North, South, East, West)
#the very first iteration will never choose 'N', that it, it will never go up in the first iteration
directions = ['S', 'E', 'W']
#counter to keep of "useless" iterations
out_range = 0

print('First node:', (y,x))
print('Max size:', max_size)
print('----------------------------')

#loop 'max_size' times
for i in range(max_size):
#Pick a direction to go
    direction = random.choice(directions)
    #Reset the possible directions
    directions = ['N', 'S', 'E', 'W']
    #Then remove the used direction in this iteration so it doesn't choose the same one twice in a row
    directions.remove(direction)
#Chooses to go up
    if direction == 'N':
        if (y-1) >= 0 and canvas[y-1][x] == []:
            canvas[y-1][x] = fill
            size += 1
            nodes_list.append((y-1,x))
            y,x = nodes_list[-1][0], nodes_list[-1][1]
        #     print('Coordinates', (y,x))
        else:
            out_range += 1
#Chooses to go down
    elif direction == 'S':
        if (y+1) <= 19 and canvas[y+1][x] == []:
            canvas[y+1][x] = fill
            size += 1
            nodes_list.append((y+1,x))
            y,x = nodes_list[-1][0], nodes_list[-1][1]
        #     print('Coordinates', (y,x))
        else:
            out_range += 1
#Chooses to go right
    elif direction == 'E':
        if (x+1) <= 19 and canvas[x+1][y] == []:
            canvas[y][x+1] = fill
            size += 1
            nodes_list.append((y,x+1))
            y,x = nodes_list[-1][0], nodes_list[-1][1]
        #     print('Coordinates', (y,x))
        else:
            out_range += 1
#Chooses to go left
    elif direction == 'W':
        if (x-1) >= 0 and canvas[y][x-1] == []:
            canvas[y][x-1] = fill
            size += 1
            nodes_list.append((y,x-1))
            y,x = nodes_list[-1][0], nodes_list[-1][1]
        #     print('Coordinates', (y,x))
        else:
            out_range += 1
    # print('Canvas with ', size, 'nodes')
    # for row in canvas:
    #     print(row)
    # print('----------------------------')
    # print()

#Print the canvas formatted
#"Blank" rows are ignored, the rest has its whitespaces and punctuation removed
print('Image size', len(nodes_list))
print('Number of useless iterations', out_range)
for row in canvas:
    if fill in str(row):
        print(str(row).replace('[','').replace(']','').replace(',','').replace('\'','').strip())
