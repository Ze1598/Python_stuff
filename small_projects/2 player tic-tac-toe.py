#A 2-player version of tic-tac-toe

#Imports
from random import randint

#create the initial 3 by 3 grid
grid = [[[] for i in range(3)] for j in range(3)]
'''Just to see the spacing needed 
grid = [['X' for i in range(3)] for j in range(3)]'''

#unfinished code to vary which player uses which symbol
'''
print('Before starting let\'s throw a coin to see which player goes firsta and what symbol each player will use: the coin has the number 1 on a side and the number 2 on the other side.')
print('The player who wins the coin toss will use an \'X\' and the other player will use \'O\'.')
coin_flip = randint(1,2)
print()
    if coin_flip == 1:
    print('1. S')
    '''
#Function to print the grid, so we each time we need to print the grid we just call the function
def print_grid():
    print('   1    2    3')
    print('1  {} | {} | {}'.format(grid[0][0], grid[0][1], grid[0][2]))
    print('   ------------')
    print('2  {} | {} | {}'.format(grid[1][0], grid[1][1], grid[1][2]))
    print('   ------------')
    print('3  {} | {} | {}'.format(grid[2][0], grid[2][1], grid[2][2]))
print_grid()
print()

#Variable to keep the loop executing while neither player has won or there's at least one space left to play
finished = False
#Spaces chosen by PLayer 1 will have an 'X' symbol
player1_symbol = 'X'
#Spaces chosen by Player 2 will have an 'O' symbol
player2_symbol = 'O'
#Number of spaces used by the player; could also be interpreted as number of total plays, either way, 'spaces_used' in all games will be less or equal than 9
spaces_used = 0

#Main loop to run the game while the game is not finished
while not finished:

#Decrement the players column and row input so it doesn't conflict with the zero-based index of lists
#Player 1 inputs
    player_row = int(input('Enter the row:')) - 1
    player_column = int(input('Enter the column: ')) - 1
#Test if the player entered the coordinates for an empty space, else prompt the player for new coordinates
    if grid[player_row][player_column] == []:
        grid[player_row][player_column] = player1_symbol
        spaces_used += 1
    else:
        print('The space you chose is occupied, please choose another space.')
        player_row = int(input('Enter the row:')) - 1
        player_column = int(input('Enter the column: ')) - 1
        grid[player_row][player_column] = player1_symbol
        spaces_used += 1
    print()
    print_grid()
    print()
    
#Test if all spaces have been used
    if spaces_used == 9:
        finished = True
#Test if Player 1 won by completing a row
    elif (grid[0][0] == grid[0][1] == grid[0][2] != []) or (grid[1][0] == grid[1][1] == grid[1][2] != []) or (grid[2][0] == grid[2][1] == grid[2][2] != []):
        print('Player 1 has won!')
        break
#Test if Player 1 won by completing a column
    elif (grid[0][0] == grid[1][0] == grid[2][0] != []) or (grid[0][1] == grid[1][1] == grid[2][1] != []) or (grid[0][2] == grid[1][2] == grid[2][2] != []):
        print('Player 1 has won!')
        break
#Test if Player 1 won by completing the left diagonal
    elif grid[0][0] == grid[1][1] == grid[2][2] != []:
        print('Player 1 has won!')
        break
#Test if Player 2 won by completing the right diagonal
    elif grid[0][2] == grid[1][1] == grid[2][1] != []:
        print('Player 1 has won!')
        break
    
#Player 2 inputs
    player_row = int(input('Enter the row:')) - 1
    player_column = int(input('Enter the column: ')) - 1
#Test if the player entered the coordinates for an empty space, else prompt the player for new coordinates
    if grid[player_row][player_column] == []:
        grid[player_row][player_column] = player2_symbol
        spaces_used += 1
    else:
        print('The space you chose is occupied, please choose another space.')
        player_row = int(input('Enter the row:')) - 1
        player_column = int(input('Enter the column: ')) - 1
        grid[player_row][player_column] = player2_symbol
        spaces_used += 1
    # grid[player_row][player_column] = player2_symbol
    print()
    print_grid()
    print()
    # print('spaces_used:', spaces_used)
    
#Test if all spaces have been used
    if spaces_used == 9:
        finished = True
#Test if Player 2 won by completing a row
    elif (grid[0][0] == grid[0][1] == grid[0][2] != []) or (grid[1][0] == grid[1][1] == grid[1][2] != []) or (grid[2][0] == grid[2][1] == grid[2][2] != []):
        print('Player 2 has won!')
        break
#Test if Player 2 won by completing a column
    elif (grid[0][0] == grid[1][0] == grid[2][0] != []) or (grid[0][1] == grid[1][1] == grid[2][1] != []) or (grid[0][2] == grid[1][2] == grid[2][2] != []):
        print('Player 2 has won!')
        break
#Test if Player 2 won by completing the left diagonal
    elif grid[0][0] == grid[1][1] == grid[2][2] != []:
        print('Player 2 has won!')
        break
#Test if Player 2 won by completing the right diagonal
    elif grid[0][2] == grid[1][1] == grid[2][1] != []:
        print('Player 2 has won!')
        break
    
else:
    print('The game has finished in a tie.')