#guess 5 digits number

#modules
from random import randint

# introduction

# setting up the number
a = ''
a1 = randint(0,9) #digit1
a2 = randint(0,9) #digit2
a3 = randint(0,9) #digit3
a4 = randint(0,9) #digit4
a5 = randint(0,9) #digit5
a += str(a1) + str(a2) + str(a3) + str(a4) + str(a5) #setting up the entire number

# print('---',a)



#let's play
user_input = input('Guess a number composed of 5 digits:') #inital user input

result = 'x' #variable to be used as output for the result of the user's attempt
turn = 5 #number of guesses left
zipp = list(zip(a,user_input)) #pair up the number with the user input
result2 = '' #variable used only operations
i = True


# print('---',zipp)
# print('---', result.count('x'))

while len(user_input) != 5:
    user_input = input('You didn\'t guess a number composed of 5 digits. Enter your guess again:')

while result.count('x') >= 1: #while the user guess has at least 1 wrong digit
    result = '' #overwrite result each time the loop starts
    
    if turn == 0: #if user is out of guesses
        print()
        print('You\'re out of guesses. The correct number was {}.'.format(a))
        break
    
    if i == True:
        for item1 in zipp: #looping through the paired digits to see if they are the same or not
            if len(set(item1)) != len(item1): #if the digit-pair is composed of the same digit then add the digit to result
                result += item1[0]
            else: #else add an 'x' in place of that digit, meaning it's a wrong guess
                result += 'x'
        print(result) #output the result of the user's guess
        i = False
        
    else:
        result = ''
        for item1 in list(zip(a,retry)): #looping through the paired digits to see if they are the same or not
            if len(set(item1)) != len(item1): #if the digit-pair is composed of the same digit then add the digit to result
                result += item1[0]
            else: #else add an 'x' in place of that digit, meaning it's a wrong guess
                result += 'x'
        print(result) #output the result of the user's guess
    
    
    if result.count('x') >= 1: #to make sure the user still has wrong digits in its guess
        retry = input('Seems like you got some digits wrong, try again:')
        while len(retry) != 5:
            retry = input('You didn\'t guess a number composed of 5 digits. Enter your guess again:')

    turn -= 1 #decrease the number of guesses left in 1
    
else: #if the player got entire number right
    print()
    print('Congrats, you guessed the number!')


  
