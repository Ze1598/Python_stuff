import itertools


'''
itertools.count(start, [step])
Create an iterator that returns evenly spaced numbers,
starting from `start`, with a difference of `step`
between each number. It accepts non-integers numbers.
'''
print("itertools.count()")
# Counts numbers starting at 1, with a step of two\
# between each returned number
counter = itertools.count(1, 2)
# Print the first ten numbers from the iterator
for i in range(10):
	# Get the next value from the iterator
	print(next(counter))
print()
# --------------------------------------------------------------------


'''
itertools.zip_longest(*iterables, fillvalue=None)
Create an iterator that aggregates elements from each of the `iterables`.
If the iterables are of uneven length, then fill the missing values with
`fillvalue`. Unlike the built-in zip() function, zip_longest() continues
until the longest iterable is exhausted. `fillvalue` is a single value
which will be substitued when an iterable has already run out of values
(i.e., if `fillvalue` is a list, then each missing value will be
filled in as the whole list).
'''
print("itertools.zip_longest()")
# Create lists with the integers between 0 and 10, 12 and 11, respectively
a = list(range(8))
b = list(range(10))
c = list(range(9))
# Aggregate the elements of each of the three lists. When it reaches the point\
# where `a` and `c` have been exhausted (since they are the shortests lists),\
# its elements will be substitued with `"N/A"`
zipper = itertools.zip_longest(a, b, c, fillvalue="N/A")
# Print each aggregate created by the iterator
for aggregate in zipper:
	print(aggregate)
print()
# --------------------------------------------------------------------


'''
itertools.cycle(iterable)
An iterator to loop through an iterator indefinitely.
'''
print("itertools.cycle()")
a = "CYCLE"
# Create an iterator to loop through the `a` string indefinitely
cycler = itertools.cycle(a)
# Counter to make the loop stop
counter = 0
# Use a while loop to output the iterator's contents ten times
while counter < 10:
	print(next(cycler))
	counter += 1
print()
# --------------------------------------------------------------------


'''
itertools.repeat(object, [times])
Create an iterator that returns `object` indefinitely. If a `times`
argument is passed, then `object` will be returned `times` times;
else it returns indefinitely.
'''
print("itertools.repeat()")
# Map the `pow()` (power) function to each element of the numbers in the range\
# 0-10, exclusive, as well as to `itertools.repeat(2)`, i.e., the integer `2` is\
# repeated as many times as the length of the range. In other words, raise each\
# number to the `pow`er of two (each element from the iterator returned by\
# `map()` is then equivalent to pow(list2[element], 2) )
repeater = list(map(pow, range(10), itertools.repeat(2)))
print(repeater)
print()
# --------------------------------------------------------------------


'''
itertools.starmap(function, iterable)
Create an iterator that applies `function` to each element of `iterable`. The difference
between this and `map()` is that, here, each element of `iterable` must be a tuple.
'''
print("itertools.starmap")
# Create a list of tuples, where the second item of the tuple is always one more than\
# then first item
a = [(x,x+1) for x in range(5)]
# starmap the `pow()` (power) function to each element of `a`. Given that each element\
# is a tuple, `pow()` receives the two items of each tuple as arguments, i.e., each\
# element of the returned iterator is equivalent to `pow(tuple[0], tuple[1])` or, in other\
# words, the `pow()` function raises the first item of each tuple to the power of the\
# second item
starmapper = list(itertools.starmap(pow, a))
print(starmapper)
print()
# --------------------------------------------------------------------


'''
itertools.combinations(iterable, r)
Return `r` length combinations of elements from `iterable`.
itertools.permutations(iterable, r)
Return `r` length permutations of elements from `iterable`.

Note that the combinations/permutations are emitted in lexicographic sort order.
Elements are treated as unique based on their position, not on their value.
Thus, there won't be repeated values in the combinations as long as all the input
elements are unique.
'''
print("itertools.combinations()")
# Create a list that contains all integers from 0 up to 4, inclusive
a = list(range(5))
# Using the integers from `a`, make two-number combinations using those\
# integers (since all integers are unique, there will be no repeated\
# combinations)
combiner = list(itertools.combinations(a, 2))
# Using the integers from `a`, make two-number permutations using those\
# integers
permutater = list(itertools.permutations(a, 2))
# Print the created combinations
for combination in combiner:
	print(combination)
print("-"*10)
print("itertools.permutations()")
# Print the created permutations
for permutation in permutater:
	print(permutation)
print()
# --------------------------------------------------------------------


'''
itertools.product(*iterables, [repeat=1])
Create an iterator which computes the cartesian product of input iterables.
If `repeat` is specified,
Note that the function doesn't compute the actual product, rather, it computes
the values to be used for each product.
'''
print("itertools.product()")
# List of integers between 0 and 2, inclusive
a = list(range(3))
# List of integers between 3 and 5, inclusive
b = list(range(3, 6))
# Cartesian product between `a` and `b`
cart_prod = list(itertools.product(a, b))
print(cart_prod)
print("-"*10)
# Cartesian product of `a`
cart_prod = list(itertools.product(a))
print(cart_prod)
print("-"*10)
# Cartesian product of `a`, repeated three times, which is equivalent to\
# passing `a` as an input iterable three times with a repeat value of 1
cart_prod = list(itertools.product(a, repeat=3))
print(cart_prod)
print()
# --------------------------------------------------------------------


'''
itertools.chain(*iterables)
Create an iterator that loops through each input iterable; when one is
exhausted, it advances to the next one. This is useful to get all the
elements from multiple iterables in a single iterator.
'''
print("itertools.chain()")
# Numbers between 0 and 9
a = list(range(10))
# Numbers between 10 and 19
b = list(range(10, 20))
# Create a single iterator that contains all elements from `a` and `b`
chainer = list(itertools.chain(a, b))
print(chainer)
print()
# --------------------------------------------------------------------


'''
itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])
Create an iterator that returns a portion (slice) of an iterable.
Unlike normal slicing, `islice()` does not support negative indices.
If `start` is `None`, then iteration starts at zero; else it starts at
index `start`. If step is `None`, then the step defaults to one, else
it's set to `step` steps. If `stop` is `None`, then iteration continues
until the iterator is exhausted; otherwise, it stops at the specified
index.
'''
print("itertools.islice()")
# Numbers from 0 to 9
a = list(range(10))
# Create an iterator which returns a slice from `a`. Start the slice at\
# index 3, and skip 3 numbers each iteration, until the end of the list
slicer = list(itertools.islice(a, 3, None, 3))
print(slicer)
print()
# --------------------------------------------------------------------


'''
itertools.compress(data, selectors)
Create an iterator which filters elements from `data`, returning only those
that have a corresponding element in `selectors` that evaluates to True.
The function stops when either `data` or `selectors` has been exhausted. 
'''
print("itertools.compress()")
# Numbers from 0 to 9
a = list(range(10))
# Create a ten-element list where the elements with even index are set to\
# True and the others to False
selectors = [True if i%2==0 else False for i in range(10)]
# Compress/filter `a` so that we get a list containing only the elements that\
# have an even index
compressor = list(itertools.compress(a, selectors))
print(compressor)
print()
# --------------------------------------------------------------------


'''
itertools.filterfalse(predicate, iterable)
Create an iterator that filters elements from `iterable` returning only those\
for which the predicate is `False`. If predicate is `None`, return the items that\
are `False`.
'''
print("itertools.filterfalse()")
# Numbers between 0 and 9
a = list(range(10))
# A list with truthy and falsy elements
b = [0, 2, "", False, True, "string"]
# Create an iterator that returns the elements of `a` whose modulo is zero when\
# divided by two
filter_false = list(itertools.filterfalse(lambda x: x%2, a))
print(filter_false)
print("-"*10)
# Create an iterator that returns the elements of `b` that have a falsy value
filter_false = list(itertools.filterfalse(None, b))
print(filter_false)
print()
# --------------------------------------------------------------------


'''
itertools.dropwhile(predicate, iterable)
Create an iterator that drops values from `iterable` while `predicate` is `True`.
When it reaches a value where `predicate` evaluates to `False`, it returns the\
rest of `iterable` starting at that point.
'''
print("itertools.dropwhile()")
a = [1, 3, 6, 2, 4, 6, 2]
# Drop numbers from `a` while they are less than 5; when it reaches a number\
# which is equal to or higher than 5, return the rest of `a` starting at that\
# number
dropper = list(itertools.dropwhile(lambda x: x<5, a))
print(dropper)
print()
# --------------------------------------------------------------------


'''
itertools.takewhile(predicate, iterable)
Create an iterator that returns values from `iterable` while `predicate` is\
`True`. When it reaches a value where `predicate` evaluates to `False`, it\
stops the iteration there.
'''
print("itertools.takewhile()")
a = [1, 3, 6, 2, 4, 6, 2]
# Return numbers from `a` while they are less than 5; when it reaches a number\
# which is equal to or higher than 5, stop the iteration
taker = list(itertools.takewhile(lambda x: x<5, a))
print(taker)
print()
# --------------------------------------------------------------------


'''
itertools.accumulate(iterable, [func])
Create an iterator that, by default, returns accumulated sums.
If `func` is given, it should be a function of two arguments.
'''
print("itertools.accumulate()")
# Numbers from 0 to 9
a = list(range(10))
# Return the accumulated sums using the elements of `a`
accumulator = list(itertools.accumulate(a))
print(accumulator)
print("-"*10)
# In ths example we still run an accumulated sum, but pass\
# a function which not only is responsible for the accumulated\
# sum but also by increasing the elements by 5% before adding\
# them to the sum
b = [1000, -90, -90, -90, -90]
accumulator = list(itertools.accumulate(b, lambda bal, pmt: round(bal*1.05 + pmt, 2) ))
print(accumulator)
print()
# --------------------------------------------------------------------


'''
itertools.groupby(iterable, key=None)
Create an iterator that returns a tuple containing a key and groups from
`iterable`.
The keys are the unique values found in `iterable`; the groups are another
iterator that contains all the occurrences of the corresponding key. To
obtain the group of a given key, it needs to be saved during that iteration,
otherwise it will be overwritten in the next iteration.
Note: it's recommended that `iterable` is sorted beforehand.
'''
print("itertools.groupby()")
a = sorted("AAABBBBBCCCCCAAAABBBBB")
# Call `groupby()` on `a` and use a list comprehension to extract the keys
grouper_keys = [k for k, g in itertools.groupby(a)]
# Call `groupby()` on `a` and use a list comprehension to extract the groups\
# (each iteration, save the group (`g`) as a list, otherwise the group is\
# overwritten between iterations)
grouper_groups = [list(g) for k, g in itertools.groupby(a)]
print(grouper_keys)
print(grouper_groups)
print("-"*10)
# Create a list of dictionaries to be grouped by the `phone` key
b = [
	{
		"name": "X",
		"phone": "123456789",
		"country": "Portugal"
	},
	{
		"name": "Y",
		"phone": "23456781",
		"country": "United Kingdom"
	},
	{
		"name": "Z",
		"phone": "34567812",
		"country": "Japan"
	},

]
# Create this function to use as the `key` for `groupby()`.\
# Using this function, the data will be grouped by the `phone`\
# key of each element (dictionary)
def get_phone(person):
	return person["phone"]
# Get the keys (which will be the values of the `phone` key)
grouper_keys = [k for k, g in itertools.groupby(b, get_phone)]
# Get the groups (each group is a list that contains the dictionary\
# correspondent to the key)
grouper_groups = [list(g) for k, g in itertools.groupby(b, get_phone)]
print(grouper_keys)
print(grouper_groups)
print()
# --------------------------------------------------------------------


'''
itertools.tee(iterable, n=2)
Returns `n` copies of `iterable`, with the default being two copies.
`iterable` can be an iterable such as a list or even an iterator.
'''
print("itertools.tee()")
# Numbers from 0 to 4
a = list(range(5))
# Create two copies of `a`
tee_1 = itertools.tee(a)
# Print the contents of each copy created by `tee()`
for iterable in tee_1:
	for item in iterable:
		print(item)
	print("-"*5)
print("-"*10)
# Create a sum accumulator iterator using `a`
b = itertools.accumulate(a)
# Create one copy of the iterator `b`
tee_2 = itertools.tee(b, 1)
# Print the contents of the copy created by `tee()`
for iterable in tee_2:
	for item in iterable:
		print(item)
print()
# --------------------------------------------------------------------