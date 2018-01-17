#Create a list of 10 items: 7 'hit' strings and 3 'dodge' strings
list1 = ['hit' if (x <=6) else 'dodge' for x in range(10)]
print(list1)

#Fizzbuzz challenge
fizzbuzz = ['FizzBuzz' if (x%15==0) else 'Fizz' if (x%3==0) else 'Buzz' if (x%5==0) else x for x in range(1,101)]
for i,j in enumerate(fizzbuzz):
    print(f'{i}: {j}')