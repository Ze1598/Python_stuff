from random import randint 

def product_pairs(n):
    '''
    Given a list of integers, find pairs of numbers
    from the list whose product equals the sum of
    all numbers in the list.
    '''
    print('n:', n)
    # The list of integers (1 to n, inclusive)
    num_list = list(range(1, n+1))
    # Sum of the list's numbers
    num_sum = sum(num_list)
    # List to hold the pairs found
    pairs = []

    # Loop through the list of integers
    for i in range(len(num_list)):
        # If we can evenly divide the sum by the current number
        if (num_sum%num_list[i] == 0):
            # And if the result of the division is in the list
            if (num_sum / num_list[i]) < n:
                # Then it means we found a pair
                pair = sorted((num_list[i], int(num_sum / num_list[i])))
                # Check if the pair is already in the found list
                if pair not in pairs:
                    pairs.append(pair)
    
    return pairs
    


for i in range(3):
    print(product_pairs(randint(1,1000)))
    print()