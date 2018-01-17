from random import choice
from random import shuffle

dodge_rng = [] #list to hold the possible rng

for i in range(7): 
    dodge_rng.append('hit') #70% chance of getting hit
for i in range(3):
    dodge_rng.append('dodge') #30% of dodging

shuffle(dodge_rng) #shuffle the order of the items in the list
print(dodge_rng) #output the list to check how it looks like