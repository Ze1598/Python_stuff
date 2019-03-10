'''
Priority queues act just like a normal queue, in the sense that items are
dequeded by being removed from the front.
The difference here is that, in priority queues, the logical order of items
is determined by their priority.
The classic way to implement a priority queue is using the binary heap data
structure.

The binary heap looks like a tree, but it has the advantage of being
implemented in a single list for internal representation.
Thus, the binary heap has two common variations: min heap, where the smallest
key is located at the front, and max heap, where the largest key is located
at the top.
This script implements a priority queue using a min binary heap.
'''
'''
Regarding the binary heap, we'll implement it with a complete binary tree,
that is, each level has all of its nodes full, except for the last level.
Since it will be implemented using a single list, we can define a couple of
properties:
	* given a parent node at index p, its left child can be found at index
	2p, while its right child can be found at 2p+1
	* given a child node at index n, its parent is located at index n/2
	* every child node holds a value equal to or larger than that of its parent
'''


# Create a class for the Min Binary Heap
class BinHeap ():
	'''
	Implement a priority queue using a min binary heap, that is, the node
	with the smallest key is located at the front/top of the heap.
	This implementation has a complete binary tree as it backbone and the
	nodes are stored in a Python list.

	Attributes
	----------
	heap_list : list
		The list that holds the binary heap's nodes. This list is initialized
		with a zero as its first node but it's never counted as a node of the
		heap, that is, it is only used to facilitate operations.
	current_size : int
		The size of the heap.

	Methods
	-------
	perc_up (i)
		Move up a node at a given index (swap it with the current parent)
		until it is in its correct position.
	insert (k)
		Insert a new node in the heap, while maintaining all of the heap's
		properties.
	perc_down (i)
		Mode down a node at a given index (swap it with one of its children)
		until it is in its correct position.
	min_child (i)
		Find which children of a given parent is the smallest one.
	del_min ()
		Remove and return the smallest node in the tree (the root). Also
		responsible for calling the necessary helper methods to maintain
		the heap's properties.
	print_heap ()
		Print the list representation of the heap.
	get_size ()
		Get the size of the heap.
	'''
	
	def __init__ (self):
		# The constructor creates the list to hold the heap and an attribute to\
		# keep track of the heap's size (starts at zero since it's an empty\
		# heap). While the initial 0 inside the list is just to allow divisions\
		# to work when inserting the first nodes, it will never be removed. Though,\
		# it will never be relevant to anything else
		self.heap_list = [0]
		self.current_size = 0

	# Insert new node
	# ---------------------------------------------------------------------------------
	# Function to swap (percolate) a child node with its parent (essentialy,\
	# move a node up one level) until the node is in its correct position
	def perc_up (self, i):
		'''
		Parameters
		----------
		i : int
			The index of the target node.

		Returns
		-------
		None
		'''

		# Run the loop while the node has a parent node (that is, the node is\
		# not the root)
		while (i//2 > 0):
			# If the current node is smaller than its parent, then swap the two nodes\
			# (according the properties of the binary heap, the parent is always smaller\
			# or equal to its children)
			if self.heap_list[i] < self.heap_list[i//2]:
				self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
			# At the end of the iteration, change focus to the parent of the current node\
			# (it will be the same node if we swapped it with its parent, otherwise this\
			# will be the parent of the node we are currently looking at)
			i //= 2


	# Insert a new item in the heap, while maintaing all of its properties
	# Start by appending the new item to the heap. Then, call the `perc_up()` method to\
	# move the node up until it is in its correct position
	def insert (self, k):
		'''
		Parameters
		----------
		k : int
			The value (integer) of the new node.

		Returns
		-------
		None
		'''

		# Append the new node to the end of the heap
		self.heap_list.append(k)
		# Since we added a new node, the heap is 1 node larger
		self.current_size += 1
		# Move the new node up until it is in its correct position
		self.perc_up(self.current_size)
	# ---------------------------------------------------------------------------------


	# Delete the smallest node (the root)
	# ---------------------------------------------------------------------------------

	# Move down a node until it's in its correct position
	def perc_down (self, i):
		'''
		Parameters
		----------
		i : int
			The index of the node target node.

		Returns
		-------
		None
		'''

		# Run the loop while the current node has a left child
		while ( (i*2) <= self.current_size ):
			# The smallest child of the current node (its index)
			small_child = self.min_child(i)
			# If the current node is larger than its smallest child,\
			# then swap them
			if self.heap_list[i] > self.heap_list[small_child]:
				self.heap_list[small_child], self.heap_list[i] = self.heap_list[i], self.heap_list[small_child]
			# Move down to the index of the smallest child of the current node
			i = small_child


	# Find out which child of a given parent node is the smallest one
	def min_child (self, i):
		'''
		If the left child is bigger than or equal to the right child or the
		right child	doesn't exist, then return the left child. Otherwise,
		return the right child.

		Parameters
		----------
		i : int
			The index of the target (parent) node.

		Returns
		-------
		int
			The index of the smallest child.
		'''
		
		# If the node doesn't have a right child, just return its left child
		if ( (i*2 + 1) > self.current_size ):
			return i*2

		# If the node has both children
		else:
			# Then if the left child is smaller, return it
			if self.heap_list[i*2] < self.heap_list[i*2+1]:
				return i*2
			# Else, return the right child
			else:
				return i*2 + 1

	# Remove and return the smallest node in the heap (the root).
	# Call the necessary functions to restore the heap's order property
	def del_min (self):
		'''
		Remove and return the smallest node in the heap. Then, put the last node
		at the root and then percolate (swap) it down until it's in its correct
		position and the heap's property is restored.

		Parameters
		----------
		None

		Returns
		-------
		return_val : int
			The smallest value in the heap (the root).
		'''

		# We want to return the root (since the first item of the heap is actually\
		# a placebo zero, the root is located at index 1)
		return_val = self.heap_list[1]
		# Make the last node the new root
		self.heap_list[1] = self.heap_list[self.current_size]
		# We removed a node, so the heaps one node shorter
		self.current_size -= 1
		# Remove the last node (since it is now at the root)
		self.heap_list.pop()
		# Call the function responsible for restoring the order property
		self.perc_down(1)
		return return_val

	# ---------------------------------------------------------------------------------

	# Utilities
	# ---------------------------------------------------------------------------------
	
	# Print the list representation of the heap
	def print_heap (self):
		# Don't print the first item, since it's the placebo zero
		print(self.heap_list[1:])

	# Return the size of the heap
	def get_size (self):
		return self.current_size
	# ---------------------------------------------------------------------------------


if __name__ == "__main__":
	from random import randint

	# Create a new empty Min Binary Heap
	my_heap = BinHeap()
	print("Created the binary heap")

	# Insert 15 random integers in the heap
	for i in range(15):
		# Pick a random integer between 1 and 100, inclusive, and insert it\
		# in the heap
		num = randint(1, 100)
		print("Inserting", num)
		my_heap.insert(num)

		# Flip a coin
		coin = randint(0,1)
		# If the coin is 1, then remove the smallest number from the heap
		if coin == 1:
			my_heap.del_min()
			print("Removed the root")

		print("Current size:", my_heap.get_size())
		# Print the list representation of the binary heap
		my_heap.print_heap()
		print()