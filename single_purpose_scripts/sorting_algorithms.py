'''
    Sorting algorithms.
    The presented algorithms are sorted in the following 
categories:
    
    Simple sorts
        Insertion sort
        Selection sort
    Efficient sorts
        Merge sort
        Heapsort
        Quicksort
    Bubble sort and variants
        Bubble sort
        Shellsort
        Comb sort
    Distribution sort
        Counting sort
        Bucket sort


    Some general ideas about sorting algorithms:

    Quick sort: When you don't need a stable sort and
    average case performance matters more than worst 
    case performance. A quick sort is O(N log N) on 
    average, O(N^2) in the worst case. A good 
    implementation uses O(log N) auxiliary storage in 
    the form of stack space for recursion.

    Merge sort: When you need a stable, O(N log N) sort, 
    this is about your only option. The only downsides 
    to it are that it uses O(N) auxiliary space and 
    has a slightly larger constant than a quick sort. 
    There are some in-place merge sorts, but they are 
    all either not stable or worse than O(N log N). 
    Even the O(N log N) in place sorts have so much 
    larger a constant than the plain old merge sort 
    that they're more theoretical curiosities than 
    useful algorithms.

    Heap sort: When you don't need a stable sort and you 
    care more about worst case performance than average 
    case performance. It's guaranteed to be O(N log N), 
    and uses O(1) auxiliary space, meaning that you won't 
    unexpectedly run out of heap or stack space on very 
    large inputs.

    Insertion sort: When N is guaranteed to be small, 
    including as the base case of a quick sort or merge 
    sort. While this is O(N^2), it has a very small 
    constant and is a stable sort.

    Bubble sort, selection sort: When you're doing 
    something quick and dirty and for some reason you 
    can't just use the standard library's sorting algorithm. 
    The only advantage these have over insertion sort is 
    being slightly easier to implement.

    Non-comparison sorts: Under some fairly limited conditions 
    it's possible to break the O(N log N) barrier and sort in 
    O(N).

    Counting sort: When you are sorting integers with a limited 
    range.

    Bucket sort: When you can guarantee that your input is 
    approximately uniformly distributed.

Sources:
    https://en.wikipedia.org/wiki/Sorting_algorithm
    https://stackoverflow.com/a/1934004
'''

# Used to create shuffled lists with random numbers
from random import randint, shuffle


def insertion_sort(arr):
    '''
    At each iteration, insertion sort removes one element from 
    the input data, finds the location it belongs within the 
    sorted list, and inserts it there. It repeats until no 
    input elements remain.

    Relevant links:
        https://en.wikipedia.org/wiki/Insertion_sort
        https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif
    '''

    # We'll loop through the entire list, starting at the second\
    # number (so that the first comparison compares the second number
    # with the first one in the list)
    for i in range(1, len(arr)):
        
        # Pick a number from the list to compare 
        num = arr[i]

        # While we are looking at valid indexes and the previous\
        # number is bigger than the current number
        while i > 0 and arr[i-1] > num:
            # The position of the current number will now hold the\
            # previous number
            arr[i] = arr[i-1]
            # Next we'll look at the previous position
            i -= 1
        
        # If nothing was swapped, the number will stay in place; if\
        # numbers were swapped, the last position we looked at will\
        # now hold the first number we picked in this iteration
        arr[i] = num
    
    return arr



def selection_sort(arr):
    '''
    The algorithm divides the input list into two parts: the sublist 
    of items already sorted, which is built up from left to right at 
    the left of the list, and the sublist of items remaining to be 
    sorted that occupy the rest of the list. 
    Initially, the sorted sublist is empty and the unsorted sublist 
    is the entire input list. The algorithm proceeds by finding the 
    smallest number in the unsorted sublist, swapping it with the 
    leftmost unsorted element, moving the sublist boundaries one 
    element to the right.
    
    Relevant links:
        https://en.wikipedia.org/wiki/Selection_sort
        https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif
    '''

    # Loop through the list
    for i in range(len(arr)):
        
        # We'll assume the next smallest number is the current one
        min_index = i

        # Now loop through the rest of the list to confirm what's the\
        # next smallest number (position)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Now put the next smallest number in the correct place by\
        # swapping it with the position we were looking at
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        # Or arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
        


def merge_sort(arr):
    '''
    Divide the unsorted list into n sublists, each containing 1
    element.
    Repeatedly merge sublists to produce new sorted sublists
    until there is only 1 sublist remaining. This will be the 
    resulting sorted list.

    Relevant links:
        https://en.wikipedia.org/wiki/Merge_sort
        https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif
    '''

    # If the input list is empty or contains just one\ 
    # number then it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the input list into two new lists: the first ('left') will\
    # hold the first half of the input list; the second ('right')\
    # will hold the second half
    left = [arr[i] for i in range(len(arr)) if (i < (len(arr) / 2) )]
    right = [arr[i] for i in range(len(arr)) if (i >= (len(arr) / 2) )]

    # Recursively merge sort each half of the input list
    left = merge_sort(left)
    right = merge_sort(right)

    # The list to hold the sorted result
    result = []

    # Trackers of the indexes being tested on the 'left' and 'right'\
    # lists, respectively
    l_index, r_index = 0, 0

    # Loop through the numbers in the 'left' list, comparing each with\
    # each number in the 'right' list. Append the smallest number of\ 
    # each comparison to the 'result' list: if the number is from 'left'\
    # then increment l_index by 1, else increment r_index by 1, that is,\
    # increment the appropriate index tracker so that the appended\
    # number isn't tested again
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1

    # After sorting the numbers from both lists, append to the\
    # resulting list whatever numbers remained in the 'left' list
    while l_index < len(left):
        result.append(left[l_index])
        l_index += 1

    # After sorting the numbers from both lists, append to the\
    # resulting list whatever numbers remained in the 'right' list
    while r_index < len(right):
        result.append(right[r_index])
        r_index += 1

    return result



def heap_sort(arr):
    '''
    Heapsort can be thought of as an improved selection sort: 
    like that algorithm, it divides its input into a sorted and 
    an unsorted region, and it iteratively shrinks the unsorted 
    region by extracting the largest element and moving that to 
    the sorted region. The improvement consists of the use of a 
    heap data structure rather than a linear-time search to find 
    the maximum.
    
    As this algorithm sorts the array in-place, first the list
    is sorted as a heap (max heap or min heap). Then, after the
    heap is finished, the root element is swapped with the nth
    element of the list, heapifying the new root each time a
    swap is made so that with each swap the list is gradually 
    sorted.

    In computer science, a heap is a specialized tree-based 
    data structure that satisfies the heap property: if P is a 
    parent node of C, then the key (the value) of P is either 
    greater than or equal to (in a max heap) or less than or 
    equal to (in a min heap) the key of C. The node at the 
    "top" of the heap (with no parents) is called the root node.

    Relevant links:
    https://en.wikipedia.org/wiki/Heapsort
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif
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
    
        # If the left child exists and it's bigger than the\
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
 
    n = len(arr)
 
    # Build the list's max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # Now sort the list (in-place): swap the current\
    # root (the largest number in the heap) with the last\
    # element. This way the root elements are gradually\
    # smaller, i.e., the list is sorted as we move the roots.\
    # Heapify after each swap to make sure the biggest\
    # number is in the root.
    for i in range(n-1, 0, -1):
        # Swap the root with the nth element of the heap
        arr[i], arr[0] = arr[0], arr[i]  
        
        #heapify root element
        heapify(arr, i, 0)



def quick_sort(arr):
    '''
    Quicksort is a comparison sort, meaning that it 
    can sort items of any type for which a "less-than" 
    relation (formally, a total order) is defined. 

    In efficient implementations it is not a stable 
    sort, meaning that the relative order of equal 
    sort items is not preserved. Quicksort can 
    operate in-place on an array, requiring small 
    additional amounts of memory to perform the 
    sorting. It is very similar to selection sort, 
    except that it does not always choose worst-case 
    partition.

    For this sorting algorithm, we use a second function
    called partition, which is responsible for creating
    the partitions needed to sort the input list.

    This quick_sort list by itself is only responsible for
    continuing the recursive partition calls and returning
    the sorted list at the end.

    Here I always consider the pivot number to be the last
    number in the list.

    Relevant links:
        https://en.wikipedia.org/wiki/Quicksort
        https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif
    '''
    
    # If the list has less than two numbers, return the list
    if len(arr) < 2:
        return arr

    def partition(arr):
        '''
        Responsable for partitioning lists for the quicksort algorithm.
        It receives a sublist as input to partition and then returns
        the index of the pivot number.

        Parameters
        ----------
        arr : list
            The list to be partitioned.

        Returns
        -------
        pivot : int
            The index of the pivot number.

        '''

        # Pick the indexes for the pivot, lower and upper bounds\
        # for the comparisons.

        # The pivot number will be the last number
        pivot = len(arr)-1
        # The lower bound is initially the first number
        lower_bound = 0
        # The upper bound bound is initially the second-last number
        upper_bound = pivot-1

        # Run the loop while the list is not fully partitioned
        while True:
            # If the lower bound is bigger than the upper bound then\
            # swap the pivot with the lower bound, than swap the lower\
            # bound (where the pivot is) with the upper bound. This way
            # the pivot is moved one index to the left, the upper bound\
            # is moved to where the lower bound was and the upper bound\
            # now occupies the original position of the pivot
            if arr[lower_bound] > arr[pivot]:
                # Swap the pivot with the lower bound
                arr[pivot], arr[lower_bound] = arr[lower_bound], arr[pivot]
                # Then swap the indexes of the upper bound with the lower bound so
                # that we can put the pivot number in its correct position
                arr[upper_bound], arr[lower_bound] = arr[lower_bound], arr[upper_bound]
                # Now the pivot is at the index of current upper bound
                pivot = upper_bound
                # Decrement the upper bound so that it is always the index to the left\
                # of the pivot
                upper_bound -= 1
            
            # If we didn't swap it means the lower bound was either equal to or smaller\
            # than the pivot, in that case we don't need to check this index again
            else:
                lower_bound += 1
            
            if lower_bound > upper_bound:
                break
        return pivot

    # Find the index of the pivot after partitioning the list
    pivot = partition(arr)
    # The sorted list is the combination of the sorted sublist of\
    # the numbers lesser or equal than the pivot, the pivot and the\
    # sorted sublist of the number bigger than the pivot
    return quick_sort(arr[:pivot]) + [arr[pivot]] + quick_sort(arr[pivot+1:])
    


def bubble_sort(arr):
    '''
    Bubble sort, sometimes referred to as sinking sort, is a simple 
    sorting algorithm that repeatedly steps through the list to be 
    sorted, compares each pair of adjacent items and swaps them if 
    they are in the wrong order. The pass through the list is 
    repeated until no swaps are needed, which indicates that the 
    list is sorted.

    Relevant links:
        https://en.wikipedia.org/wiki/Bubble_sort
        https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif
    '''

    # The size of the sublist we have to compare decreases\
    # with each iteration
    for max_index in range(len(arr)-1,0,-1):
        # From the left-most number, compare it with the next.\
        # If the current number is bigger than the next swap them.
        for i in range(max_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]



def shell_sort(arr):
    '''
    Shellsort, also known as Shell sort or Shell's method, is an 
    in-place comparison sort. It can be seen as either a 
    generalization of sorting by exchange (bubble sort) or 
    sorting by insertion (insertion sort). The method starts 
    by sorting pairs of elements far apart from each other, then 
    progressively reducing the gap between elements to be 
    compared. Starting with far apart elements, it can move 
    some out-of-place elements into position faster than a simple 
    nearest neighbor exchange.

    Relevant links:
        https://en.wikipedia.org/wiki/Shellsort
        https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif
    '''

    def gap_insertion_sort(arr, start, gap):
        '''
        We use this function to pretty much select specific
        numbers in the list similarly to calling range()
        with all three start, stop and step arguments.
        Then, from the selected numbers, we sort them by
        swapping them so that they sorted between themselves.

        arr: list to be sorted.
        start: the starting point to select numbers.
        gap: has the same utility as the step step argument 
        in range().

        '''

        # We start on the position next to the one passed, always\
        # go until the end of the list and jump "gap" positions\
        # between each selected number
        for i in range(start+gap, len(arr), gap):

            currentvalue = arr[i]
            position = i

            # If a pair of the selected numbers are inverted, swap them\
            # and keep swapping the bigger number until it is on its\
            # correct position
            while position >= gap and arr[position-gap] > currentvalue:
                arr[position] = arr[position-gap]
                # Adjust the position variable
                position = position-gap

            # Now put the original number in its due position
            arr[position] = currentvalue

    # The initial number of sublists to use is half of the list's length
    sublist_count = len(arr) // 2
    
    # Run the following loop while we can still create sublists
    while sublist_count > 0:
        
        # Use a range() function of sorts to sort sublists of the list
        for start_pos in range(sublist_count):
            gap_insertion_sort(arr, start_pos, sublist_count)
        
        # Halve the number of sublists to use
        sublist_count = sublist_count // 2



def comb_sort(arr):
    '''
    The basic idea is to eliminate turtles, or small values
    near the end of the list, since in a bubble sort these 
    slow the sorting down tremendously. Rabbits, large 
    values around the beginning of the list, do not pose a 
    problem in bubble sort.
    In bubble sort, when any two elements are compared, 
    they always have a gap (distance from each other) of 1. 
    The basic idea of comb sort is that the gap can be much 
    more than 1. The inner loop of bubble sort, which does 
    the actual swap, is modified such that gap between 
    swapped elements goes down (for each iteration of outer 
    loop) in steps of a "shrink factor" k: [ n/k, n/k2, 
    n/k3, ..., 1 ].
    The gap starts out as the length of the list n being 
    sorted divided by the shrink factor k (generally 1.3)
    and one pass of the aforementioned modified bubble sort 
    is applied with that gap. Then the gap is divided by 
    the shrink factor again, the list is sorted with this 
    new gap, and the process repeats until the gap is 1. 
    At this point, comb sort continues using a gap of 1 
    until the list is fully sorted. The final stage of the 
    sort is thus equivalent to a bubble sort, but by this 
    time most turtles have been dealt with, so a bubble 
    sort will be efficient.

    Relevant links:
        https://en.wikipedia.org/wiki/Comb_sort
        https://upload.wikimedia.org/wikipedia/commons/4/46/Comb_sort_demo.gif
    '''

    # The gap starts as the length of the input list
    gap = len(arr)
    # The shrink factor is 1.3
    shrink = 1.3
    # Variable used to make the loop run
    is_sorted = False

    # Run the loop while the list is not sorted
    while not(is_sorted):
        # Floor divide the gap by the shrink factor with each iteration
        gap = int(gap // shrink)

        # If the gap is equal to or less than 1 then the list will\
        # be fully sorted at the end of this iteration. Thus, update
        # "is_sorted" to end the loop with this iteration
        if gap <= 1:
            is_sorted = True

        # Used to keep track of indexes
        i = 0

        # Loop while we can compare pairs of numbers "gap"-indexes distant
        while (i + gap) < len(arr):
            
            # If the two numbers being compared are not sorted, swap them
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]

            # Increment i to compare the next number            
            i += 1



def counting_sort(arr):
    '''
    Counting sort starts by creating a new array with k empty arrays,
    where k is the value of the largest value in the input array.
    The unsorted values are then placed into the new array using the 
    value as the index. The auxiliary array is now holds the original
    values in sorted order and can be iterated over to construct the 
    final sorted array.

    This implementation doesn't include duplicates.

    Relevant links:
        https://en.wikipedia.org/wiki/Counting_sort
        https://www.growingwiththeweb.com/2014/05/counting-sort.html
    '''

    # Create a list of n empty lists. n is the value of the largest\
    # number in the input list
    temp_list = [[] for i in range(max(arr) + 1)]

    # Loop through the input list insert each number n at the index n\
    # of the temporary list
    for num in arr:
        temp_list[num] = num

    # Now loop through the temporary list to construct the final sorted list
    sorted_list = []
    for lst in temp_list:
        if lst:
            sorted_list.append(lst)
    
    return sorted_list


def bucket_sort(arr, buckets_to_create=10):
    '''
    Bucket sort works as follows:
        Set up an array of initially empty "buckets".
        Scatter: Go over the original array, putting each object in 
    its bucket.
        Sort each non-empty bucket.
        Gather: Visit the buckets in order and put all elements back 
    into the original array.
    
    The most common implementation of bucket sort works by splitting 
    the array of size n into k buckets, each of which houses a value
    in the range of n/k.

    Relevant links:
        https://en.wikipedia.org/wiki/Bucket_sort
        https://www.growingwiththeweb.com/2015/06/bucket-sort.html
    '''
    
    # Get the smallest and largest numbers in the list
    min_num = min(arr)
    max_num = max(arr)

    # Create the list of buckets
    num_buckets = int( (max_num - min_num) // buckets_to_create ) + 1
    list_buckets = [[] for i in range(num_buckets)]

    # Distribute the numbers among the created buckets
    for i in range(0, len(arr)):
        bucket_index = int( (arr[i] - min_num) // buckets_to_create)
        list_buckets[bucket_index].append(arr[i])

    # Will hold the sorted list
    sorted_list = []
    # Sort each bucket and add its content to the sorted list
    # Sort using an insertion sort
    for bucket in list_buckets:
        if bucket:
            sorted_list += insertion_sort(bucket)
    
    return sorted_list




if __name__ == "__main__":
    # Test each sorting method with random lists: 10-numbers lists where\
    # each number is a random integer between 0 and 100, inclusive
    for func in [insertion_sort, selection_sort, merge_sort, heap_sort, quick_sort, bubble_sort, shell_sort, comb_sort, counting_sort, bucket_sort]:
        
        # Print the name of the current sorting algorithm
        print(' '.join(func.__name__.split('_')).capitalize())
        
        # Create a 10-integer list, where each integer is a random\
        # integer between 0 and 100, inclusive
        sample = [randint(0, 100) for i in range(10)]
        print('Sample:', sample)

        # If it's an algorithm that sorts the list in-place, call the\
        # function and then print the sorted sample
        if func in [heap_sort, bubble_sort, shell_sort, comb_sort]:
            func(sample)
            print('Result:', sample)

        # Otherwise just print the sorted list returned by the function
        else:
            print('Result:', func(sample))

        print()