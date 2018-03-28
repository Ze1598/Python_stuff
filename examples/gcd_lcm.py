#Compute the lowest common multiple (lcm) of two integers using\
#the formula x*y=lcm(x,y)*gcd(x,y), where gcd stands for greatest\
#common divisor

'''The Euclidean algorithm is based on the principle that the greatest 
common divisor of two numbers does not change if the larger number 
is replaced by its difference with the smaller number.'''
#Source:https://en.wikipedia.org/wiki/Euclidean_algorithm

def gcd(x, y):
    '''Calculate the greatest common divisor
    for the integers x and y using the 
    Euclidian Algorithm'''
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    '''Calculate the lowest common multiplier
    for two integers'''
    #x*y=lcm(x,y)*gcd(x,y)
    return (x*y)//gcd(x,y)


from random import randint
x = randint(1,100)
y = randint(1,100)
print(f'gcd({x},{y}) =>', gcd(x,y))
print(f'lcm({x},{y}) =>', lcm(x,y))