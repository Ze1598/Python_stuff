'''
	An ordered list is a list where each item contains a relative position
to the other items of that list. Thus, each item in the list must contain
a reference to the next one, so that the relative position of each item
can be expressed by following the links from one item to the next.
	The difference between an ordered and an unordered is that the relative
positions of the nodes in the former are based on some characteristic, such
as ascending or descending order of the values.
	We are going to implement an ordered list using the linked list data
structure.
	The first item of the list is known as the head. Each item is known as
a node.
	The last item does not need to point to any other item since it is the
last one.
	Each node must hold at least two informations: its data (known as data
field) and a reference to the next node.
'''

# Class to create a single node for the list
class Node ():
	'''
	Implement a Node for the ordered list. Each node has two information:
	its data field (the data it holds) and a reference to the node that
	follows it (`next`).

	Attributes
	----------
	data_field : int
		The data held by this node.
	next : __main__.Node
		The node that follows this one.

	Methods
	-------
	get_data ()
		Get the data held by this node.
	get_next ()
		Get the node (Node object) that follows this one.
	set_data (new_data)
		Overwrite the data held by the node.
	set_next (new_next)
		Overwrite the node that follows this one.
	'''

	def __init__ (self, init_data):
		'''
		Class constructor for a node of a linked list. `init_data` is the
		data to be contained in the node.

		Parameters
		----------
		init_data : int
			The data held by this node.
		next : __main__.Node
			The node that follows this node.
		'''

		self.data_field = init_data
		self.next = None

	def get_data (self):
		'''
		Return the data held by this node.

		Parameters
		----------
		None

		Returns
		-------
		int
			The data held by this node.
		'''

		return self.data_field

	def get_next (self):
		'''
		Get the reference to the next node.

		Parameters
		----------
		None

		Returns
		-------
		__main__.Node
			The reference to the next node.
		'''

		return self.next

	def set_data (self, new_data):
		'''
		Change (set) the data held by this node.

		Parameters
		----------
		new_data : int
			The new data to be held by this node.

		Returns
		-------
		None
		'''

		self.data_field = new_data

	def set_next (self, new_next):
		'''
		Change the reference to the next node (make this node point to
		another node).

		Parameters
		----------
		new_next : __main__.Node
			The new reference.

		Returns
		-------
		None
		'''

		self.next = new_next


class OrderedList ():
	'''
	Implement an ordered list (linked list) using Python's built-in lists.
	This implementation orders nodes in ascending order of their data fields,
	that is, the first node holds the smallest data field while the last holds
	the largest.

	Attributes
	----------
	head : __main__.Node
		The head (first) node of the list.

	Methods
	-------
	is_empty ()
		Check if the list is empty.
	size ()
		Get the size of the list.
	search (item)
		Search for a node that holds the given data field.
	add (item)
		Add a new node to the list.
	remove (item)
		Remove the first node in the list that holds the given data field.
	get_full_list ()
		Use linked list traversal to return a Python list with all the
		data fields of the linked list.
	'''

	# When a new linked list is created it is empty (it doesn't point\
	# to a head, thus it's empty)
	def __init__ (self):
		self.head = None


	def is_empty (self):
		'''
		Check if the linked list is empty.

		Parameters
		----------
		None

		Returns
		-------
		bool
			True if the list is empty; else False.
		'''

		# If there's no reference to the head node, then the list is empty
		return self.head == None

	def size (self):
		'''
		Get the size of the linked list. To find the size we'll use linked list
		traversal, i.e., we'll pass through (traverse) each node, while counting
		how many nodes we pass.

		Parameters
		----------
		None

		Returns
		-------
		count : int
			The size of the linked list.
		'''

		# Start at the head of the list
		current_node = self.head
		# Keep track of the number of visited nodes (size of the list)
		count = 0
		# Loop through the nodes until we find one that doesn't point to a\
		# another node (i.e., it's `next` attribute is `None`)
		while current_node != None:
			# We found another node, so increment the count of nodes found
			count += 1
			# Now we move on to the node pointed by the current node
			current_node = current_node.get_next()

		return count

	def search (self, item):
		'''
		Use linked list traversal to search for the first node that holds a
		data field equal to `item`. If a node holding the specified data is
		found, returns True, else the method returns False.

		Parameters
		----------
		item : int
			The data to be searched for in the nodes of the linked list.

		Returns
		-------
		bool
			True if the data was found; else False.
		'''

		# Start the search at the head node
		current_node = self.head
		# Loop while we haven't reached the end of the list and the current node holds a\
		# value smaller than the one we are looking for
		while current_node != None and current_node.get_data() <= item:
			# If the current node holds the desired data, return True right away because\
			# there's at least one node in the linked list with said data
			if current_node.get_data() == item:
				return True
			# If it doesn't, move on to the next node
			else:
				current_node = current_node.get_next()

		# If the function reached this point, it means it traversed the whole linked list\
		# and didn't find a single node that held the desired data. Thus, return False
		return False

	def add (self, item):
		'''
		Add a new node to the list. Since this is an linked list ordered from with the\
		smallest number at the head node and the largest at the last node, we need to\
		use linked list traversal to find where to insert the new node so this list\
		remains ordered.

		Parameters
		----------
		item : int
			The data to be held by the new node.

		Returns
		-------
		None
		'''

		# Create the new node
		new_node = Node(item)
		# We'll start traversing at the head node
		current_node = self.head
		# The head node does not have a previous node
		previous_node = None

		# Loop while we haven't reached the end of the list
		while current_node != None:
			# If the current node holds a data field smaller or equal to that of the\
			# node we want to insert, move on to the next node
			if current_node.get_data() <= item:
				previous_node = current_node
				current_node = current_node.get_next()
			# If the current node's data field is smaller than that of the new node, stop\
			# the loop because we found where to insert the new node
			else:
				break

		# If the previous node is None, it means the list is empty. Thus, the new node will\
		# be the head node
		if previous_node==None:
			new_node.set_next(self.head)
			self.head = new_node
		# If the previous node is not None, the new node will be inserted either between two\
		# already existing nodes or at the end of the list
		else:
			new_node.set_next(current_node)
			previous_node.set_next(new_node)

	def remove (self, item):
		'''
		Use linked list traversal to remove the first node that holds a data field equal
		to `item`.

		Parameters
		----------
		item : int
			The first node in the list that holds this data field will be deleted.

		Returns
		-------
		None
		'''

		# The current node we are looking at
		current_node = self.head
		# The node previous to the current one (starts as None since the head node doesn't\
		# have a previous node)
		previous_node = None

		# Loop while we haven't traversed the whole linked list
		while current_node != None:
			# If we found the node that holds the target data
			if current_node.get_data() == item:
				# If we are not going to remove the head node, then we can safely set the\
				# previous node to point to the node that follows the current node (the one\
				# to be removed)
				if previous_node != None:
					previous_node.set_next(current_node.get_next())
				# Otherwise, if we are going to remove the head node (i.e., the previous node\
				# is None), set the new head node to be the node that follows the removed node
				else:
					self.head = current_node.get_next()
				# Then break out of the loop because we won't have to keep searching
				break

			# If the current node is not the one we are looking for, then the current node is\
			# now the previous node and the current node is the node that follows what was the\
			# current node
			else:
				previous_node = current_node
				current_node = current_node.get_next()

	def get_full_list (self):
		'''
		Use linked list traversal to return a Python list with all the values saved in the
		nodes of the linked list.

		Parameters
		----------
		None

		Returns
		-------
		values_list : list
			A Python list with all the values saved in the linked list.
		'''

		# Start at the head node
		current_node = self.head
		# List to be returned with the values
		values_list = []

		while current_node != None:
			values_list.append(current_node.get_data())
			current_node = current_node.get_next()

		return values_list




if __name__ == "__main__":
	new_linked_list = OrderedList()
	print("Linked list created")
	print("The linked list is empty:", new_linked_list.is_empty())

	new_linked_list.add(5)
	print("Added the first node to the linked list")
	print("The linked list is empty:", new_linked_list.is_empty())
	new_linked_list.add(13)
	print("Added another node to the linked list")
	new_linked_list.add(9)
	print("Added another node to the linked list")
	new_linked_list.add(3)
	print("Added another node to the linked list")
	new_linked_list.add(17)
	print("Added another node to the linked list")
	print("Full linked list (as a Python list):", new_linked_list.get_full_list())
	print("Size of the linked list:", new_linked_list.size())

	print("The linked list contains at least one node that holds a value of 2:", new_linked_list.search(2))
	print("The linked list contains at least one node that holds a value of 3:", new_linked_list.search(3))
	print("The linked list contains at least one node that holds a value of 17:", new_linked_list.search(17))

	new_linked_list.remove(13)
	print("The node with a data field of 13 was removed")
	new_linked_list.remove(3)
	print("The node with a data field of 3 was removed")

	print("Full linked list (as a Python list):", new_linked_list.get_full_list())
	print("Size of the linked list:", new_linked_list.size())