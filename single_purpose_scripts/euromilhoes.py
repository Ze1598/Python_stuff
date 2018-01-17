from random import randint
from random import choice

def euromilhoes():
    
    
    nums = list(range(1,51))
    stars = list(range(1,12))
    n1 = choice(nums)
    nums.remove(n1)
    n2 = choice(nums)
    nums.remove(n2)
    n3 = choice(nums)
    nums.remove(n3)
    n4 = choice(nums)
    nums.remove(n4)
    n5 = choice(nums)
    
    s1 = choice(stars)
    stars.remove(s1)
    s2 = choice(stars)
    # print('Numbers-',n1,n2,n3,n4,n5)
    # print('Stars-',s1,s2)
    # print()
    
    print('Welcome to my Euromilhões game!')
    print('In this game you try to guess the random combination of 5 Numbers and 2 Stars the program creates.')
    print()
    
    print('Numbers:','\n')
    
    for i in range(1,51,5):
        print(i, end = ' ')
    print('')
    
    for i in range(2,51,5):
        print(i, end = ' ')
    print()
    
    for i in range(3,51,5):
        print(i, end = ' ')
    print()
    
    for i in range(4,51,5):
        print(i, end = ' ')
    print()
    
    for i in range(5,51,5):
        print(i, end = ' ')
    print('\n')
    
    print('Stars:', '\n')
    
    for i in range(1,12,4):
        print(i, end = ' ')
    print()
    
    for i in range(2,12,4):
        print(i, end = ' ')
    print()
    
    for i in range(3,12,4):
        print(i, end = ' ')
    print()
    
    for i in range(4,12,4):
        print(i, end = ' ')
    print('\n')
    
    print('Now you need to choose 5 Numbers from the list above.')
    num1 = int(input('Choose the first number: '))
    num2 = int(input('Choose the second number: '))
    num3 = int(input('Choose the third number: '))
    num4 = int(input('Choose the fourth number: '))
    num5 = int(input('Choose the fifth number: '))
    print()
    print('Now you need to choose 2 Stars from the list above.')
    star1 = int(input('Choose the first star: '))
    star2 = int(input('Choose the second star:'))
    print()
    
    if (num1 == n1) and (num2 == n2) and (num3 == n3) and (num4 == n4) and (num5 == n5): 
        if (star1 == s1) and (star2 == s2):
            print('You completly guessed the combination!')
            print('Numbers: ',n1,n2,n3,n4,n5)
            print('Stars: ',s1,s2)
        else:
            print('You guessed all the numbers!')
            print('Numbers: ',n1,n2,n3,n4,n5)
            print('Correct Stars: ',s1,s2)
            print('Your Stars: ',star1,star2)
    elif (star1 == s1) and (star2 == s2):
        print('You guesse both stars!')
        print('Correct Numbers: ',n1,n2,n3,n4,n5)
        print('Your Numbers: ',num1,num2,num3,num4,num5)
        print('Stars: ',s1,s2)
    else:
        print('Here is the correct combination: ')
        print('Correct Numbers: ',n1,n2,n3,n4,n5)
        print('Your Numbers: ',num1,num2,num3,num4,num5)
        print('Correct Stars: ',s1,s2)
        print('Your Stars: ',star1,star2)
        
euromilhoes()