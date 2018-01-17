for x in range(1, 11):
    print(repr(x).rjust(3), repr(x*x).rjust(4), repr(x*x*x).rjust(5))
    
print()

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#   1    1     1
#   2    4     8
#   3    9    27
#   4   16    64
#   5   25   125
#   6   36   216
#   7   49   343
#   8   64   512
#   9   81   729
#  10  100  1000

#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000