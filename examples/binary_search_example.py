from random import randint

def binary_search(num, lower_bound, upper_bound):
    #The mid point is the floored average of the lower and upper bounds
    mid_pos = (lower_bound+upper_bound)//2

    #Run the loop while the number hasn't been found
    while mid_pos != num:
        
        #Each iteration one of the bounds is modified, so we can update the mid point here
        mid_pos = (lower_bound+upper_bound)//2

        #If the mid point is bigger than the number, then update the upper bound to\
        #be the current value of the mid point - 1
        if mid_pos > num:
            print(mid_pos, 'is too high.')
            upper_bound = mid_pos - 1

        #If the mid point is smaller than the number, then update the lower bound to\
        #be the current value of the mid point + 1
        elif mid_pos < num:
            print(mid_pos, 'is too low.')
            lower_bound = mid_pos + 1

    #When the number is found, print a statement with the number
    else:
        print(mid_pos, 'is the correct answer.')    

#The initial lower bound is the smallest number in the range
lower_bound = 1
#The initial upper bound is the biggest number in the range
upper_bound = 128
#The number to be guessed is a random integer in the inclusive range of lower bound to upper bound
rand_num = randint(lower_bound, upper_bound)
print('Number to be guessed:', rand_num)

#Call the function to find the random number using binary search
binary_search(rand_num, 1, 128)