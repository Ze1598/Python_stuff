# Script to count how many times a function is called

# Create the decorator
def counter(func):
    '''
    The function that will count how many times the inner
    function was called.

    Args:
        func (function): The function whose calls will be
    counter.
    
    Returns:
        func (function): The decorated function.
    '''
    def inner(*args):
        '''
        The decorated function. When calling it, increment
        the number of times the function was called.
        
        Args:
            *args: Receives as many arguments as the
        decorator function needs.        
    
        Attributes:
            count (int): The counter for function calls.
        
        Returns:
            func(*args): The return value of calling func
        with arguments.
        '''
        # We keep track of how many times it was called with\
        # this attribute
        inner.count += 1
        return func(*args)

    # Initliaze the counter
    inner.count = 0

    return inner


@counter
def inc(x):
    '''
    Returns the input integer, incremented by 1.

    Args:
        x (int): An integer.
    
    Returns:
        (int): The input integer incremented by 1.
    '''

    return x + 1

print('inc(1):', inc(1))
print('inc(2):', inc(2))

print('The inc() function was called:', inc.count, 'times.')