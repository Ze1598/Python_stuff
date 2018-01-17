from random import choice, shuffle
#List to hold the rng; in this case 70% chance of getting 'hit', 30% chance of 'dodge'ing
dodge_rng = ['hit' if (x<7) else 'dodge' for x in range(10)]
#Shuffle the list
shuffle(dodge_rng) 
print(dodge_rng)
