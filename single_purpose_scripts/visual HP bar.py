#this is a simple program to output a "visual" HP bar in games.
#the HP bar should look like this /----------\; each '-' values 10% of the character's HP, and each space in place of a '-' would be the same as 10% of damage to the total HP

from math import trunc
from random import randint

def enemy_sprite():
    print()
    print('(- -- -)'.rjust(68))
    print('--|------|--'.rjust(70))
    print('|------|'.rjust(68))
    
def hp_bar_visual(hp, hp_now):
    hp_bar = '/'
    hp_bar += '-' * trunc(((hp_now/hp) * 10))
    hp_bar += ' ' * (10 - trunc(((hp_now/hp) * 10)))
    hp_bar += '\\'
    #of course it can be written in a single line; though i'll use two, so the first line is used as sort of a reset for the HP bar:
    # hp_bar = '/'
    # hp_bar += ('-' * trunc(hp/10)) +  (' ' * (10 - trunc(hp/10))) +  '\\'
    return hp_bar
a = 'Satanel'
#DEBUG purposes
hp1 = 100
hp1_now = 100
hp2 = 100
hp2_now = 100
keep = ''
while keep == '':
    print('{}\'s HP'.format(a).rjust(69))
    print(hp_bar_visual(hp1, hp1_now).rjust(70))
    enemy_sprite()
    print('Your HP'.rjust(10))
    print(hp_bar_visual(hp2, hp2_now))
    print()
    # hp1 = int(input('New hp1 value: '))
    # hp1_now = int(input('New hp1_now value: '))
    # hp2 = int(input('New hp2 value: '))
    # hp2_now = int(input('New hp2_now value: '))
    keep = input('Keep going? ')
    hp1 = randint(1,1000)
    hp2 = randint(1,1000)
    hp1_now = randint(0,hp1)
    hp2_now = randint(0,hp2)
    print('hp1-',hp1,'hp2-',hp2)
    print('hp1_now-',hp1_now,'hp2_now-',hp2_now)
    print('div enemy- ', trunc(((hp1_now/hp1) * 10)))
    print('div player- ', trunc(((hp2_now/hp2) * 10)))
