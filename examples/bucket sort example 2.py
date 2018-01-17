from random import shuffle,randint

#Create a list of numbers, starts at somewhere between 0 to 50 and ends at
#somewhere between 100 to 200
num_list = list(range(randint(0,50), randint(100,200)))
print(f'Starts at: {min(num_list)}\nEnds at: {max(num_list)}')
#Shuffle the list
shuffle(num_list)

def bucket_sort(arr):
    #Create a list to hold the buckets
    #Each bucket will hold 10 numbers, each set of ten
    buckets_list = [[] for x in range(max(arr)//10+1)]

    #Loop through the initial numbers' list
    #If the number < 10, put it in the very first bucket
    #If the number has more than 3 digits, put it in the bucket with the index \
    #corresponding to the first two digits of that number
    #If the number has 2 digits, put it in the bucket whose index corresponds to \
    #the first digit of that number
    for num in arr:
        if len(str(num)) == 1:
            buckets_list[0].append(num)
        elif len(str(num)) > 2:
            buckets_list[int(str(num)[:-1])].append(num)
        else:
            buckets_list[int(str(num)[0])].append(num)
        #instead of all this crap I could've just used the following line:
        #buckets_list[int(num/10)].append(num)
        
    #Finally, sort each bucket
    for bucket in buckets_list:
        bucket.sort()
    return buckets_list

for bucket in bucket_sort(num_list):
    print(bucket)