'''
A deque data structure works as an hybrid between a stack and
a queue. Items can be added both at the front or at the rear and
can be removed both at the front and the rear as well. Thus, a
deque does not need to respect neither the FIFO (first-in,
first-out) nor the LIFO (last-in, first-out) principles.
'''

class Deque ():
	'''
	Implement the deque data structure using Python's built-in lists.
	In this implementation, the beginning of the list is the deque's front and
	the end is the deque's rear.

	Attributes
	----------
	items : list
		The deque itself.

	Methods
	-------
	is_empty ()
		Check if the deque is empty.
	add_front (item)
		Add a new item to the front of the deque (beginning of the list).
	add_rear (item)
		Add a new item to the rear of the deque (end of the list).
	remove_front ()
		Remove and return the front item of the deque (beginning of the list).
	remove_rear ()
		Remove and return the front item of the deque (end of the list).
	size ()
		Get the size of the deque.
	'''

	# A new deque starts empty (an empty list)
	def __init__ (self):
		self.items = []

	def is_empty (self):
		'''
		Method to check if the deque is empty.

		Parameters
		----------
		None

		Returns
		-------
		bool
			True if the deque is empty; else False.
		'''

		return self.items == []

	def add_front (self, item):
		'''
		Add a new item to the front of the deque (start of the list).

		Parameters
		----------
		item
			The item to be added.

		Returns
		-------
		None
		'''

		self.items.insert(0, item)

	def add_rear (self, item):
		'''
		Add a new item to the rear of the deque (end of the list).

		Parameters
		----------
		item
			The item to be added.

		Returns
		-------
		None
		'''

		self.items.append(item)

	def remove_front (self):
		'''
		Remove and return the front item of the deque (start of the list).

		Parameters
		----------
		None

		Returns
		-------
			The item removed from the front of the deque.
		'''

		return self.items.pop(0)

	def remove_rear (self):
		'''
		Remove and return the rear item of the deque (end of the list).

		Parameters
		----------
		None

		Returns
		-------
			The item removed from the rear of the deque.
		'''

		return self.items.pop()

	def size (self):
		'''
		Return the size of the deque (length of the list).

		Parameters
		----------
		None

		Returns
		-------
		int
			The size of the deque.
		'''

		return len(self.items)


if __name__ == "__main__":
	my_deque = Deque()
	print("`my_deque` was created")
	print("Is the deque empty:", my_deque.is_empty())

	my_deque.add_front(3)
	print("Item added to the front")
	my_deque.add_front("Hello")
	print("Item added to the front")
	my_deque.add_rear(9.2)
	print("Item added to the rear")
	print("Size of the deque:", my_deque.size())
	my_deque.add_rear([1, 2, 3, 4, 5])
	print("Item added to the rear")
	my_deque.add_front({'a':1, 'b':2})
	print("Item added to the front")
	print("Size of the deque:", my_deque.size())
	
	print("The top item of the deque was removed:", my_deque.remove_front())
	print("The rear item of the deque was removed:", my_deque.remove_rear())
	print("The top item of the deque was removed:", my_deque.remove_front())
	print("Size of the stack:", my_deque.size())