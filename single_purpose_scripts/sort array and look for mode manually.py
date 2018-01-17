arr = [2,3,3,3,1,10,4,5,2,4]
sorted_arr = []
min_value = float('inf')
while arr:
    for i in arr:
        if i < min_value:
            min_value = i
    arr.remove(min_value)
    sorted_arr.append(min_value)
    min_value = float('inf')

print(sorted_arr)

index = 0
n = 1
counter_max = 1
counter_current = 1
value = 0
for i in sorted_arr:
    # for i2 in sorted_arr:
    while ((index + n) <= (len(sorted_arr) - 1)) and (i == sorted_arr[index+n]):
        counter_current += 1
        n += 1 
        
    n = 1
    if counter_current > counter_max:
        counter_max = counter_current
        value = i
    counter_current = 1
    index += 1

print(value, 'frequency:', counter_max)