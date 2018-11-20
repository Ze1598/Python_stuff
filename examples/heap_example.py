'''
    In computer science, a heap is a specialized tree-based 
data structure that satisfies the heap property: if P is a 
parent node of C, then the key (the value) of P is either 
greater than or equal to (in a max heap) or less than or 
equal to (in a min heap) the key of C. The node at the 
"top" of the heap (with no parents) is called the root node.
'''

'''
    If the index of any element in the array is i, the element 
in the index 2i+1 will become the left child and element in 
2i+2 index will become the right child. 
    The parent of any element at index i is given by the lower 
bound of (i-1)/2.
'''

def heapify(arr, n, i):
    '''
    Build a max-heap for a given list.

    arr: list to be heapified
    n: length of the list to be heapified
    i: index of the subtree root
    '''

    # Subtree root index
    largest = i
    # Subtree root index left child index
    l = 2 * i + 1
    # Subtree root index right child index
    r = 2 * i + 2 

    # If the left child exists and it's bigger than the\
    # root then save the child's index as the largest\
    # number in the comparison
    if l < n and arr[i] < arr[l]:
        largest = l

    # If the right child exists and it's bigger than the\
    # root then save the child's index as the largest\
    # number in the comparison
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # If the root is not largest then swap it with the\
    # largest and continue heapifying until the original\
    # subtree root is put in its place
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
  

arr = [1, 12, 9, 5, 6, 10]
n = len(arr)
# Heapify each number in the list (starting at the end of the list)
for i in range(n, -1, -1):
    heapify(arr, n, i)
print(arr) # [12, 6, 10, 5, 1, 9]