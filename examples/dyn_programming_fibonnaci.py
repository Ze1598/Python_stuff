'''
Showing the three types of dynamic programming
    Recursion
    Memoisation
    Bottoms Up
using the Fibonnaci Sequence. In specific, to
find the what is the nth number of the sequence.
'''

# Will be used to time each function
from time import time

# Compute the first 'compute' numbers in the Fibonnaci sequence
compute = 30

def recur(n):
    '''
    Find the nth number of the Fibonnaci sequence
    using recursion.
    Time complexity: O(2**N)
    '''
    # If it's the 0th or 1st number, simply return n
    if n == 0 or n == 1:
        return n
    
    # A number in the sequence (if n!=0 and n!=1) is the sum\
    # of its two previous numbers. Thus, to find the nth number\
    # we need to sum nth-1 and nth -2. Because we are not\ 
    # starting at the beginning of the sequence, we need to\
    # recursively trace back until the beginning of the\
    # sequence so we can compute what is the nth number
    return recur(n-2) + recur(n-1)

start = time()
recur_results = [recur(i) for i in range(compute)]
print(recur_results)
print('Recursion took:', round(time() - start, 6), 'seconds.\n')

def memoi(n):
    '''
    Find the nth number of the Fibonnaci sequence
    using memoisation.
    Time complexity: O(N), space O(N)
    '''
    # Dictionary the mapping of each number to its position\
    # in the sequence
    results = {}
    # If n is 0 or 1, just return n
    if n == 0 or n == 1:
        return n
    
    # If n is in 'results', that is, n has already been\
    # computed, return the nth number of the sequence
    if n in results:
        return results[n]
    
    # The nth number of the sequence is the results of the\
    # sum of the nth-2 and nth-1 numbers of the sequence
    results[n] = memoi(n-2) + memoi(n-1)
    
    return results[n]

start = time()
memoi_results = [memoi(i) for i in range(compute)]
print(memoi_results)
print('Memoisation took:', round(time() - start, 6), 'seconds.\n')

def bottomsup(n):
    '''
    Find the nth number of the Fibonnaci sequence
    using a bottoms up approach.
    Time complexity O(N), space O(1)
    '''
    if n == 0 or n == 1:
        return n
    
    # Initialize two variables to simbolize the two numbers\
    # that are always involved in computing the next number.
    # We start them at 0 and 1 since those are the first two\
    # numbers of the sequence
    a = 1
    b = 0
    # The number that will be returned
    fib = 0

    # Because we already have the first and second numbers\
    # (b and a, respectively) we only need to compute n-1\
    # numbers to find the nth number in the sequence
    for i in range(n-1):
        # The next number is the sum of the two numbers we have
        fib = a + b
        # Now the second-previous is just the previous number
        b = a
        # Now the previous number is the just computed number\
        # (because the number that was computed is the number that\
        # comes before the number that will be computed next)
        a = fib
    
    return fib

start = time()
bottomsup_results = [bottomsup(i) for i in range(compute)]
print(bottomsup_results)
print('Bottoms Up took:', round(time() - start, 6), 'seconds.\n')