import typing
#https://www.python.org/dev/peps/pep-3107/
#Function annotation examples
''' "By itself, Python does not attach any particular\
meaning or significance to annotations. Left to its\
own, Python simply makes these expressions available(...)" '''
#def foo(a: expression, b: expression = value):
#   pass

#Here we assing 'a' to 3, and expect 'x' to be an integer; then\
#we return whatever argument was passed as 'x', plus the value of 'a'
def test1(x: int, a = 3):
    return x + a
print('test1(2)=',test1(2)) #5
print('test1(5.0)=',test1(5.0)) #8.0

#We assign 'a' and 'b' to strings and return their concatenation
def test2(a = "Hello ", b = "World"):
    return a + b
print('test2()=',test2()) #Hello World

#We assign 'a', 'b', 'c' and 'd' to integers and then return their sum
def test3(a = 1, b = 5, c = 17, d = 9):
    return a+b+c+d
print('test3()=',test3()) #32

#We expect 'a' to be 10 and 'b' to be a list, and the return value 9
def test4(a: 10, b: list) -> max(2,9):
    return a, b
print('test4(15, [1,2,3])=',test4(15, [1,2,3]))

#Get the function annotation mapping for 'test4'
print(typing.get_type_hints(test4))
