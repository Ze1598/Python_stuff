for i in range(99, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottles of beer on the wall, 2 more bottles of beer!')
                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))

#output
'''
99 bottles of beer on the wall, 99 bottles of beer!
So take one down, pass it around, 98 more bottles of beer on the wall!
98 bottles of beer on the wall, 98 bottles of beer!
So take one down, pass it around, 97 more bottles of beer on the wall!
97 bottles of beer on the wall, 97 bottles of beer!
So take one down, pass it around, 96 more bottles of beer on the wall!
...
3 bottles of beer on the wall, 3 bottles of beer!
So take one down, pass it around, 2 more bottles of beer on the wall!
2 more bottles of beer on the wall, 2 more bottles of beer!
So take one down, pass it around, 1 more bottle of beer on the wall!
1 bottle of beer on the wall, 1 bottle of beer!
So take it down, pass it around, no more bottles of beer on the wall!
'''