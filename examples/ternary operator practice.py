inpt = input('integer')

i = ('even' if (int(inpt) % 2 == 0) else 'odd')
print(i)


if int(inpt) % 2 == 0:
    i = 'even'
else:
    i = 'odd'
print(i)