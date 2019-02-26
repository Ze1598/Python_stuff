# Sources:
# https://gist.github.com/Ayrx/5884790
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

import random, time

def miller_rabin(n, k):
    '''
    Use the Miller-Rabin primality test
    to test if a given integer is composite
    or (most) probably prime. 
    This is a non-deterministic algorithm.
    
    Parameters
    ----------
    n : int
        An integer to be tested for primality.
    k : int
        The number of tests to perform.

    Returns
    -------
    bool
        True if the number is probably prime,
        else False.
    ''' 
    
    # 1 and 2 are both primes
    if n in (1, 2):
        return True

    # If n is an even number, it is composite
    if n % 2 == 0:
        return False

    # After these checks, n is odd for sure

    # Counter for how many time d is evenly divided\
    # by 2 while remaining even
    r = 0
    # Subtract 1 from n to obtain an even integer.
    # For the test to be successful, its result should\
    # equal this number
    d = n - 1

    # Keep dividing d by 2 while it remains even; use r to\
    # count the number of times this division happens
    while d % 2 == 0:
        r += 1
        d //= 2
    # Now n-1 can be written as 2**r * d

    # Perform k tests
    for test in range(k):
        # Choose a random integer from the exclusive range (2, n-1)
        a = random.randrange(2, n - 1)
        # x = a ** d % n
        x = pow(a, d, n)
        # If x is 1 or n-1 we can move on to the next iteration
        if x == 1 or x == n - 1:
            continue
        # Run this nested loop as many times as n-1 can be\
        # evenly divided by 2 and remain an even number,\
        # minus two iterations
        for num in range(r - 1):
            # x = x ** 2 % n
            x = pow(x, 2, n)
            # If x is equal to n-1 break out of the loop to return\
            # that n is probably prime
            if x == n - 1:
                break
        # If it ran through all the iterations without x ever being\
        # equal to n-1, then n is composite
        else:
            return False
    
    # If n passed all tests, then it is probably prime
    return True


# Tests
# Create a list of twenty-five random numbers, where each number is a\
# random number from the exclusive range (1000000, 10000000000)
start = time.time()
test_nums = [random.randrange(1000000, 10000000000) for i in range(25)]
for i in test_nums:
    print(f'Is {i} a prime?\t\t{miller_rabin(i, 40)}')
print('Elapsed time:', round(time.time() - start, 3), 'seconds.')