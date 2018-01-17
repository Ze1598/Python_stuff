array1 = [29, 25, 3, 49, 9, 37, 21, 43]
array2 = [1, 50, 100, 530, 20, 5, 95, 27, 33, 249]

def bucket_sort(array):
    #this list will hold the final bucket sort
    sorted_buckets = [] 
    
    #this chunk find the max value of array
    max_value = float('-inf')
    for num in array:
       if num > max_value:
           max_value = num
    
    #calculate the number of buckets [] needed and create them in the buckets variable
    number_of_buckets = int(max_value/10 + 1) 
    #basically gets me buckets for the intervals 0-9, 10,19, 20-21,...,x- number_of_buckets
    #then create the buckets list using list comprehension
    buckets = [[] for x in range(number_of_buckets)]
    # print('buckets creation:',buckets)
    
    #for each number in the initial array list, put it in the corresponding bucket 
    #eg: 2 in the 0-9 bucket; 15 in the 10-19 bucket
    for num in array:
        buckets[int(num / 10)].append(num)
    # print('buckets with some content:',buckets)
    
    #finally, sort each individual bucket and add all the values, ordered, to the final sorted_buckets list
    for item in buckets:
        for num in sorted(item):
            sorted_buckets.append(num)
            
    return sorted_buckets
    
print('bucket_sort([29, 25, 3, 49, 9, 37, 21, 43]) =>',bucket_sort([29, 25, 3, 49, 9, 37, 21, 43]))
print('bucket_sort([1, 50, 100, 530, 20, 5, 95, 27, 33, 249]) =>',bucket_sort([1, 50, 100, 530, 20, 5, 95, 27, 33, 249]))