'''
    Binary search in list of depth 2 where the result is not known,
except it's general direction relative to our current position in 
the grid (up, down, left, right, up-right, up-left, down-right, 
down-left).
    The search is performed in the lower or upper half of an axis, 
depending on the direction received. 
    The half not chosen is never taken into searched and each choice
is then followed by an adjustment of the lower/upper bound, which 
successively halves the searching area on each axis.
    In each search, we average the lower and upper bounds to find out
the next position to search for in the axis.

Helpful source: https://en.wikipedia.org/wiki/Binary_search_algorithm
'''

# Both width and height are given as input
# w: width of the list (1 <= w <= +inf)
# h: height of the list (1 <= h <= +inf)
w, h = [int(i) for i in input().split()]
# The starting position in the list
# x: the starting position in the x-axis
# y: the starting position in the y-axis
x, y = [int(i) for i in input().split()]
# Define the lower and upper bounds for both\
# axis.
# The lower bounds (minx and miny) start at 1,\
# given that it's the smallest value possible\
# for w an be; the upper bounds (maxx and maxy)\
# star at w and h, respectively, the input-defined\
# values for width and height
minx, maxx = 1, w
miny, maxy = 1, h


# Loop to run until the solution is found
while True:

    # The general direction of the result relative to\
    # our current position.
    # Possible values: U, UR, R, DR, D, DL, L, UL
    result_dir = input()

    # Given the general position of the result relative\
    # to our current position, calculate where to move next,
    # adjusting the upper and lower bounds for the axis
    if result_dir:

        # The result is Upwards
        if result_dir == "U":
            maxy = y - 1
            y = (miny + maxy) // 2

        # The result is Upwards, to the Right
        elif result_dir == "UR":
            minx = x + 1
            maxy = y - 1
            x = (minx + maxx) // 2
            y = (miny + maxy) // 2

        # The result is Rightwards
        elif result_dir == "R":
            minx = x + 1
            x = (minx + maxx) // 2

        # The result is Downwards, to the Right
        elif result_dir == "DR":
            minx = x + 1
            miny = y + 1
            x = (minx + maxx) // 2
            y = (miny + maxy) // 2

        # The result is Downwards
        elif result_dir == "D":
            miny = y + 1
            y = (miny + maxy) // 2

        # The result is Downwards, to the Left
        elif result_dir == "DL":
            maxx = x - 1
            miny = y + 1
            x = (minx + maxx) // 2
            y = (miny + maxy) // 2

        # The result is Leftwards
        elif result_dir == "L":
            maxx = x - 1
            x = (minx + maxx) // 2

        # The result is Upwards, to the Left
        elif result_dir == "UL":
            maxx = x - 1
            maxy = y - 1
            x = (minx + maxx) // 2
            y = (miny + maxy) // 2


    # Print the coordinates to where we'll move
    print(x, y)