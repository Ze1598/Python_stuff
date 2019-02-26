'''
map(function, +iterable)
Return an iterator that applies `function` to every item of `iterable`, 
yielding the results. 
If multiple `iterable`s arguments are passed, `function` must take
that many arguments and, without forgetting that `function` is applied
to the items from all iterables in parallel. 
With multiple iterables, the iterator stops when the shortest iterable
is exhausted. 
'''

# Create a list where each element is an alphabet letter
list1 = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
# Map the `str.capitalize()` function to each element of `list1`, that is,
# capitalize each string from `list1`
list1_ = list(map(str.capitalize, list1))
print(list1_)



import itertools
# Create a list with all the integers between 0 and 10, exclusive
list2 = list(range(10))
# Map the `pow()` (power) function to each element of `list2` as well as to\
# `itertools.repeat(2)`, i.e., the integer is `2` repeated as many times as the\
# length of `list2`. In other words, raise each element of `list2` to the\
# `pow`er of two (each element from the iterator returned by `map()` is then\
# equivalent to pow(list2[element], 2) )
list2_ = list(map(pow, list2, itertools.repeat(2)))
print(list2_)