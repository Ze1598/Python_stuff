#Loop practice

print('Loop 1')
for i in range(10):
    print('*', end=' ')
print()
print()

print('Loop 2')
for i in range(10):
    print('*', end=' ')
print()
for j in range(5):
    print('*', end=' ')
print()
for h in range(20):
    print('*', end=' ')
print()
print()

print('Loop 3')
for i in range(10):
    for j in range(10):
        print('*', end=' ')
    print()
print()
print()

print('Loop 4')
for i in range(10):
    for j in range(5):
        print('*', end=' ')
    print()
print()
print()

print('Loop 5')
for i in range(5):
    for j in range(20):
        print('*', end=' ')
    print()
print()
print()

print('Loop 6')
for i in range(10):
    for j in range(10):
        print(j, end=' ')
    print()
print()
print()

print('Loop 7')
for i in range(10):
    for j in range(10):
        print(i, end=' ')
    print()
print()
print()

print('Loop 8')
for i in range(10):
    for j in range(i):
        print(j, end=' ')
    print()
print()
print()

print('Loop 9')
for i in range(10):
    #Spaces before
    for h in range(i):
        print(' ', end=' ')
    #Numbers
    for j in range(10-i):
        print(j, end=' ')
    print()
print()
print()

print('Loop 10')
for i in range(1, 10):
    for j in range(1, 10):
        #Format the spacing between numbers
        if (i*j < 10) and (j > 1):
            print(' ', end='')
        print(i*j, end=' ')
    print()
print()
print()

print('Loop 11')
for i in range(1, 10):
    #Leading whitespace for each row
    for j in range(9-i):
        print(' ', end=' ')
    #Numbers up to the middle, included
    for h in range(1, i+1):
        print(h, end=' ')
    #Numbers after the middle, middle excluded
    for g in range(i-1,0,-1):
        print(g, end=' ')
    print()
print()
print()

print('Loop 12')
#The upper half (middle row included)
for i in range(1, 10):
    #Leading whitespace for each row
    for j in range(9-i):
        print(' ', end=' ')
    #Numbers up to the middle of the row, included
    for h in range(1, i+1):
        print(h, end=' ')
    #Numbers after the middle of the row
    for g in range(i-1,0,-1):
        print(g, end=' ')
    print()
#The bottom half (middle row not included)
for i in range(1, 9):
    #Leading whitespace for each row
    for j in range(i):
        print(' ', end=' ')
    #Numbers up to the middle of each row, row included
    for h in range(1, 10-i):
        print(h, end=' ')
    #Numbers after the middle of each row
    for g in range(8-i, 0, -1):
        print(g, end=' ')
    print()
