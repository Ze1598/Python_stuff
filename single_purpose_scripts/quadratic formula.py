from math import sqrt

def eq(a,b,c):
    d = b**2 - 4*a*c
    
    if d < 0:
        print("This equation has no real solution")
    elif d == 0:
        x = (-b + sqrt(d)) / (2*a)
        print("This equation has one solutions: ", x)
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print("This equation has two solutions: ", x1, " and", x2)
    
eq(1,2,3)
eq(3,2,1)
eq(1,9,2)