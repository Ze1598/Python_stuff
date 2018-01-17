from random import choice
from random import randint

room_options = [[0,'O'], [1, '|'], [2, '-'], [3,'X'], [4,'i']] #the options for each room (character) in the board are 'O' (empty space), '|' (vertical wall), '-' (horizontal wall), 'X' (end of the maze) or 'i' (player)

row_ongoing = [] #will hold the layout for the row that is being worked on
tf = [True, False] #list to help decide if something happens or not 

row_index = 0 
column_index = 0

#function to generate content for each room; needs to be given the string slicing arguments
def get_room(x,y,z): #x- start, y-stop, z-step
    gen = choice(room_options[x:y:z])
    gen_get = gen[1]
    return gen_get

#function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

#creates the initial board: a 10x15 board, containing only 'O' as rooms 
board = [['O' for i in range(10)] for j in range(10)]

#generates where the player will 'spawn'; it can only 'spawn' in the first row
gen_player = [0, randint(1,len(board[0])-2)]
print(gen_player)
#generates the exit room; it can only be in the last row
gen_exit = [len(board)-1, randint(1,len(board[0])-2)]
print(gen_exit)


#loop through the rows in board
for row in board:
    #if it is the first or last row of the board, then it will only contain horizontal walls ('-')
    if (row_index == 0) or (row_index == (len(board[0]) - 1)):
        for i in range(len(board[0])):
            row_ongoing.append(str(room_options[2][1]))
        #after the row is created add it to the board; to the beginning if dealing with the first row, or to the end if dealing with the last row
        board.insert(row_index, row_ongoing)
        #delete the previous first row if dealing with index 0; else delete the previous last row
        if row_index == 0:
            del board[row_index + 1] 
        else:
            del board[row_index + 1]
        row_ongoing = [] #reset 
    row_index += 1 
row_index = 0

'''
#loop through the columns of board
for row in board:
    for column in row:
        #the first and last columns of the board will only have vertical walls ('|')
        if (column_index == 0) or (column_index == (len(row)-1)):
            board[row_index][column_index] = room_options[1][1]
        column_index += 1 
    row_index += 1 
    column_index = 0
'''
#loop through all the rows so that the first and last columns only have vertical walls ('|')
for i in range(len(board[0])):
    board[i][0] = room_options[1][1]
    board[i][len(board[0]) - 1] = room_options[1][1]

#place the exit on the board
board[gen_exit[0]][gen_exit[1]] = room_options[3][1]
#place the player on the board
board[gen_player[0]][gen_player[1]] = room_options[4][1]
#print the board
print_board(board)
