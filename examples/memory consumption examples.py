import sys
x=1
print(sys.getsizeof(x)) #28
x = 12
print(sys.getsizeof(x)) #28
x=1.2 
print(sys.getsizeof(x)) #24
x='1.2'
print(sys.getsizeof(x)) #52
x=[1,2]
print(sys.getsizeof(x)) #80
x=[]
print(sys.getsizeof(x)) #64
x=[1]
print(sys.getsizeof(x)) #72
x={}
print(sys.getsizeof(x)) #240
x={'1':1}
print(sys.getsizeof(x)) #240
x={'1':1, '2':2}
print(sys.getsizeof(x)) #240
x = [i**2 for i in range(10)] 
print(sys.getsizeof(x)) #192
x = [i**2 for i in range(5)]
print(sys.getsizeof(x)) #128
class Test:
    pass
print(sys.getsizeof(Test)) #1056

