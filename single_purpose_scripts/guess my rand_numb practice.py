#guess my number

from random import randint

print("Welcome to my game!")
print("The rules are very simple, I pick a number between 1 and 50 and you try to guess it, you\'ll have 5 tries.")
print("To help you, after each try I\'ll say if the number you guessed is either higher or lower than the number I chose.")

my_number = randint(1,50)
try_number = 0

for try_number in range(6):
    if try_number < 5:
        try_input = int(input("So, what\'s your guess?"))
        if try_input == my_number:
            print("Well done, that\'s the number I chose!")
            break
        elif try_input < my_number:
            print("That\'s lower than what I chose.")
        elif try_input > my_number:
            print("That\'s higher than what I chose.")
    elif try_number == 5:
        print("Oops, you\'re out of guesses. The number I chose was", my_number)
    try_number += 1
