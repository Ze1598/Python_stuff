def result_fact():
    x = int(input('Enter a positive integer:'))
    fact = 1
    
    for x in range(x,0,-1):
        fact *= x
    
    print(fact)