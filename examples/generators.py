# Examples of generators: generator iterators and generator expressions
'''
These are particularly useful since at first they are just what the name
implies: generators of values, waiting to fetch the next value. This is
because it doesn't hold all the values in memory, instead, it only gets
one value at a time whenever it is "asked" to (when it is iterated over
with a for loop, using next(), etc.)
'''

# -----------------------------------------------------------

# This function (generator iterator) loops through an iterable passed as\
# input and yields one value at a time. The difference between `yield`\
# and `return` is that the former only fetches one value at a time,\
# without "looking" into the remaining values, while the latter fetches\
# all values at once
def reverse(data):
	"""
	Get the values of an iterable, in reverse order, one at a time.

	Parameters
	----------
	data : iterable
		The object to be iterated over.

	Yields:
	item
		One item from `data`.
	"""

	# Loop through the input iterable in reverse order
	for item in range(len(data)-1, -1, -1):
		# By using the `yield` statement, the function fetches only one\
		# value at a time, unlike with `return` which would return all\
		# the values at once. It's also worth noting that when a function\
		# ends in a `yield` statement its execution state will be saved for\
		# the next time the function is called
		yield data[item]

# This will get each character in the string "generator", one at a time,\
# in reverse order
for char in reverse("generator"):
	print(char)
print("\n\n")

# -----------------------------------------------------------

# Now let's creator a generator using generator expressions
# The syntax for these is similar to that of list comprehensions, but instead it\
# uses parenthesis instead of brackets

# Double each value between 0 and 10, exclusive
gen_exp1 = (i*2 for i in range(10))
# Loop through the generator to print one value at a time
for num in gen_exp1:
	print(num)

# Alternatively, save and print the values generated in a list
# Due note that this removes any performance gains from using generators
gen_exp1 = (i*2 for i in range(10))
print(list(gen_exp1))
print()

# Create two three-item lists
x = [3,6,9]
y = [4,8,12]
# Create a generator which multiplies pairs of values from a zip of the previously\
# created lists
gen_exp2 = (x_val*y_val for x_val, y_val in zip(x,y))
# Now print each value generated
for value in gen_exp2:
	print(value)