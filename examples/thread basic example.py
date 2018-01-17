import threading
import time

def product(a,b):
    #first thing to be executed
    print('{} \n'.format(a**b))
    #while it sleeps the code outside the thread is executed
    time.sleep(3)
    #after sleep finishes the function prints this statement
    print('Finished')

#create a thread called 't1', that targets the 'product' function, and takes in two arguments    
t1 = threading.Thread(target = product, name = 't1', args = (2,3))

#start the thread
t1.start()

#this statement will be executed while the thread is "sleep"ing
print('Concurrent execution motherfuckers')