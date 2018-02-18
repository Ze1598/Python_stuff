from random import randint

def bubble_sort(lst):
    '''Sorts a list using the Bubble Sort sorting algorithm.
    Args:
        lst (list): The list to be sorted.
    
    Returns:
        lst (list): The sorted list.
    '''
    #Number of times numbers are swapped in the sort
    swaps_made = 0
    for i in range(len(lst)):
        bub = 0
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                bub += 1
                swaps_made += 1
        if bub == 0:
            break
    print(swaps_made, 'swaps were made.')
    return lst

a = [3,2,1]
b = [randint(1,50) for i in range(5)]
c = [randint(1,50) for i in range(10)]

print('a:', a, 'sorted:', bubble_sort(a))
print('b:', b, 'sorted:', bubble_sort(b))
print('c:', c, 'sorted:', bubble_sort(c))