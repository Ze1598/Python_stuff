# Examples of iter() and next() as well as their implementation in a class\
# with __iter__() and __next__()

# -----------------------------------------------------------

# Using iter() and next() to iterate over an object

# The object which we'll iterate over (the iterable)
iterable_obj = "abc"
# Create the iterator (using the previous iterable, in this\
# case, a string)
it = iter(iterable_obj)
# Get the next value from the iterator (here it's the first value)
print(next(it)) # "a"
# Get the next value (the second value)
print(next(it)) # "b"
# Get the next value (the third and last value)
print(next(it)) # "c"
# Get the next value; since there's no next value, it raises\
# a StopIteration exception instead
# print(next(it))
print("\n\n")


# -----------------------------------------------------------

# Now let's create a class that implements the __iter__() and\
# __next__() methods

class ReverseIter:
	"""
	Class to iterate over an iterable object in reverse order.

	Attributes
	----------
	data : iterable
		Any iterable object, such as strings, lists, dictionaries,
		etc.
	index : int
		The index currently being targeted by the iterator. This is
		initialized as the length of the `data` attribute, given
		that it will be iterated in reverse order.

	Methods
	-------
	__iter__()
		Create an iterator for the `data` object passed when
		creating a class instance.
	__next__()
		Get the next item from the iterator created in __iter__().
	"""

	def __init__(self, data):
		"""
		Initialize a class instance.

		Parameters
		----------
		Any iterable object, such as strings, lists, tuples, etc.
		"""
		self.data = data
		self.index = len(data)

	def __iter__(self):
		"""
		Create an iterator for the `data` object passed when
		creating a class instance.

		Parameters
		----------
		None

		Returns
		-------
		self
		"""

		# Including the __iter__() method in the class definition is\
		# enough to make the iter() function work for objects of this\
		# class
		return self

	def __next__(self):
		"""
		Get the next item from the iterator created in __iter__().
		This method will iterate over the object in reverse order.

		Parameters
		----------
		None

		Returns
		-------
		self.data[self.index]
			The next value of the iterable.
		"""

		# If we are already at index 0, then it means there's nothing else\
		# to iterate over; raise a StopIteration exception
		if self.index == 0:
			raise StopIteration

		# Decrement the `index` attribute by 1 (because we are iterating in reverse\
		# order)
		self.index -= 1

		# Return the value of `self.data` at index `self.index`
		return self.data[self.index]


sample_iterable = ReverseIter("abc")
iter(sample_iterable)
# If we use a for loop to iterate over the object which already has its own created\
# iterator, it will call next() on its own
for value in sample_iterable:
	print(value)
print()

# Same process as before, except this time we are using a list as the iterable
sample_iterable2 = ReverseIter(["e", "f", "g"])
iter(sample_iterable2)
for value in sample_iterable2:
	print(value)