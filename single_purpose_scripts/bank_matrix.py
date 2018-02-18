#Create a matrix card for a bank account, 9 by 9, with randomised numbers between 100 and 999

from random import randint
#Title for each row: each character represents a row
#Leave a space in the beginning so, matrix[0][0] is empty
rows = ' 12345678'
#Title for each column: each character represents a column
columns = 'ABCDEFGH'

#Create the matrix: begin by creating 8 rows, containing only the corresponding titles
matrix = [[char] for char in rows]
#Add the titles for each column (by appending the titles to matrix[0])
matrix[0].extend(char for char in columns)

#Now populate each row with numbers: each value is a random number between 100 and 999
for row in range(1, len(matrix)):
    for num in range(8):
        matrix[row].append(str(randint(100,999)))

#Create a string ready to hold the output format for each row in the matrix
format_string = '{:>4} ' * len(matrix[0])
#Print the matrix, by calling the '.format()' method on each line of the matrix\
#The string itself is already formatted
for num in range(len(matrix[0])):
    print(format_string.format(*matrix[num]))