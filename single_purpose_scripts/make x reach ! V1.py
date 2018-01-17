#get 'x' above '!'
from time import sleep
character = 'x' #'player icon' that will move 

road = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '!'] #10 characters to be used as the 'map'


#introduction
print("Hello and welcome to my game. In this very simple game your objective is to get the \'x\' above the exclamation point.")
print()
#prints the initial 'map'
# print("---------!")
print(character[0])
def road_function():
    for item in road:
        print(item, end='')

# print("---------!")
road_function()

print()
print()


#output rules for the user 
print("To make the \'x\' reach the exclamation point you simply need to input \'go\' when prompted.")
print()
print("Please keep in mind that each time you input \'go\' it means moving the \'x\' 1 space to the right.")
print()


#user input starts here

#if input 'go', move 1 character to right
choice = input("Alright, please make the \'x\' move:")
keep_going = 0
progress_spaces = ' '
while keep_going in range(9): 
    '''enough range to look like the 'x' is above the '!' ''' 
    if choice.lower() == "go":
        if keep_going == 8: 
            '''execute this condition when the 'x' is above the '!' '''
            print()
            progress_spaces = '         '
            print(progress_spaces, end='')
            print(character)
            road_function()
            print() 
            print()
            print('Objective complete!')
            print('Thanks for playing my game.')
            sleep(5) 
            '''5-second delay'''
            break 
            '''ends program'''
        print()
        print(progress_spaces, end='') 
        '''prints 1+n space to the left of the 'x' so to the user it seems like the 'x' actually moved to the right'''
        print(character)
        road_function()
        progress_spaces = progress_spaces + ' ' 
        '''adds 1 space to the left of 'x' '''
        print()
        choice_continued = input("Great job, now please make it keep going just by pressing 'Enter'.") 
        '''prompts the user for the next move'''
        keep_going += 1 
        '''increments keep_going by 1 so it signifies 1 turn has passed'''
        
