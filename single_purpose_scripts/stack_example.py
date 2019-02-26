'''
	Stacks are an ordered list of items where the addition and removal of
items always occurs at the end (the top). 
	A stack works just like a real-life stack of, say, books. The first
book to be removed is the one at the top and the last the one at the
base (thus fulfilling the "first-in, first-out" (FIFO) principle).
	As a consequence, the order of insertion is the exact opposite of the
order of removal.
'''


# As such, we can Python's built-in `list`s to implement a class for\
# the stack data structure.
class Stack ():

	# A new stack starts empty (an empty list)
	def __init__ (self):
		self.items = []

	def is_empty (self):
		'''
		Method to check if the stack is empty.

		Parameters
		----------
		None

		Returns
		-------
		bool
			True if the stack is empty; else False.
		'''

		return self.items == []

	def push (self, item):
		'''
		Method to add a new item to the stack.

		Parameters
		----------
		item
			The item to be added to the top of the stack (end of the list).

		Returns
		-------
		None

		'''

		# We can just use the list's data type `append()` method to add the\
		# new item to the top of the stack (which is the end of the list)
		self.items.append(item)

	def pop (self):
		'''
		Remove and return the top item from the stack (last item of the list).

		Parameters
		----------
		None

		Returns
		-------
			The top item of the stack (the last item of the list).
		'''

		return self.items.pop()

	def peek (self):
		'''
		Get the top item of the stack (without removing it).

		Parameters
		----------
		None

		Returns
		-------
			The top item of the stack (last item of the list).
		'''

		return self.items[len(self.items)-1]

	def size (self):
		'''
		Get the size of the stack (the length of the list).

		Parameters
		----------
		None

		Returns
		-------
		int
			The size of the stack (list).
		'''

		return len(self.items)



if __name__ == "__main__":
	my_stack = Stack()
	print("`my_stack` was created")
	print("Is the stack empty:", my_stack.is_empty())
	
	print("Three items are going to be stacked")
	my_stack.push(15)
	my_stack.push("Hello")
	my_stack.push(9.2)
	print("Size of the stack:", my_stack.size())

	print("This is the top item of the stack:", my_stack.peek())
	print("The top item of the stack was removed:", my_stack.pop())
	print("Size of the stack:", my_stack.size())