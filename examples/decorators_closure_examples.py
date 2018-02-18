'''Creates a closure function, that is, the nested function references a value\
in its enclosing scope'''
'''In this case, 'multiplier()' references 'n', a value from the enclosing\
function 'make_multiplier_of()'''
'''All 3 criteria are met for creating closure:
#Have a nested function;
#The nested function referes to a value defined in the enclosing
function;
#The enclosing function returns the nested function'''
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

#Assign a closure function object, passing it '3' as an argument
times3 = make_multiplier_of(3)

#Assign a second closure function object, passing it '5' as an argument
times5 = make_multiplier_of(5) 

print('times3(9) =>',times3(9)) #27

print('times5(3) =>',times5(3)) #15

print('times5(times3(2)) =>',times5(times3(2))) #30

'''All function objects have a '__closure__' attribute
that returns a tuple of cell objects if it is a closure
function. Then the cell object has the attribute cell_contents that
stores the wanted value'''
#Thus, we can extract the enclosed values from 'times3' and 'times5'
print('times3 cell contents:', times3.__closure__[0].cell_contents)
print('times5 cell contents:', times5.__closure__[0].cell_contents)
print()

#___________________________________________________

#Decorators
'''First create a closure function, that is, a nested
function that is, the nested function refers to a value
from the enclosing function (in this case executes the input 'func'tion)
Lastly, the enclosing function returns the nested one'''
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

#Define a basic function
def ordinary():
    print("I am ordinary")


'''Now to decorate 'ordinary', we can do it "manually" and then assing it to
a variable, like this'''
prettify = make_pretty(ordinary)
'''However, Python has proper syntax to simplify this process: @decorator_name
Though using this is simply syntatic sugar
We can decorate 'ordinary' simply like this'''
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary() #Exactly the same result as if you'd call prettify()
print()

'''This first example is rather easy because the decorator doesn't receive
any arguments ('inner' takes zero arguments).
What if we needed to receive at least one argument in our decorator?
Let's say we need a preventive if statement to avoid exceptions.'''
def divide(a,b):
    return a/b #If b==0 then ZeroDivisionError will be raised
'''To counteract the exception raise, we will add a decorator
that checks if b==0 or not'''
def smart_divide(func):
    def zero_testing(a,b):
        print(f'I am going to divide {a} by {b}')
        #If b is zero then simply return None
        if b == 0:
            print("Cannot divide by zero")
            return None
        #Else return the result of a/b
        return func(a,b)
    return zero_testing

@smart_divide
def divide(a,b):
    return a/b
print(divide(2,5))
print(divide(1,0))
print()

'''You could then create a general decorator that would work with
any number of parameters:
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner
Here 'args' will be a tuple of positional arguments and 
'kwargs' a dictionary of keyword arguments'''

'''You can also chain decorators for a same function'''
def star(func):
    def inner_star(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner_star

def percent(func):
    def inner_percent(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner_percent

@star
@percent
def printer(msg):
    print(msg)
#Equivalent to: star(percent(printer("Hello")))
printer("Hello")