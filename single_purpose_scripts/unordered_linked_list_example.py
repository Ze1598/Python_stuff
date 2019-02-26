'''
	An unordered list is a list where each item contains a relative position
to the other items of that list. Thus, each item in the list must contain a
reference to the next one, so that the relative position of each item can
be expressed by following the links from one item to the next.
	We are going to implement an unordered list using the linked list data
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
	def __init__ (self, init_data):
		'''
		Class constructor for a node of a linked list. `init_data` is the
		data to be contained in the node.

		Parameters
		----------
		init_data
			The data of the node.
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
		Node.data_field
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
		Node.next
			The reference to the next node.
		'''

		return self.next

	def set_data (self, new_data):
		'''
		Change (set) the data held by this node.

		Parameters
		----------
		new_data
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
		new_next
			The new reference.

		Returns
		-------
		None
		'''

		self.next = new_next


# Create a class for the unordered list (linked list) itself
# The order of insertion is the exact opposite order of the items in the list\
# (the last item inserted occupies the first position in the list and the\
# first item inserted is the last item in the list)
class UnorderedList ():
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

	def add (self, item):
		'''
		Add a new node to the list. It will be added as the head of the list,
		and the reference to the next node of this new node will be the previous
		head node.

		Parameters
		----------
		item
			The data to be held by the new node.

		Returns
		-------
		None
		'''

		# Create the new node
		new_node = Node(item)
		# Set the next node of this new node to be the current head node of the list
		new_node.set_next(self.head)
		# Update the list so that the brand-new node is the new head node as well
		self.head = new_node

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
		item
			The data to be searched for in the nodes of the linked list.

		Returns
		-------
		bool
			True if the data was found; else False.
		'''

		# Start the search at the head node
		current_node = self.head
		# Loop while we haven't reached the end of the list
		while current_node != None:
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

	def remove (self, item):
		'''
		Use linked list traversal to remove the first node that holds a data field equal
		to `item`.

		Parameters
		----------
		item
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
	new_linked_list = UnorderedList()
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
	print("Full linked list (as a Python list):", new_linked_list.get_full_list())
	print("Size of the linked list:", new_linked_list.size())

	print("The linked list contains at least one node that holds a value of 2:", new_linked_list.search(2))
	print("The linked list contains at least one node that holds a value of 3:", new_linked_list.search(3))

	new_linked_list.remove(13)
	print("The first node with a data field of 13 was removed")
	new_linked_list.remove(3)
	print("The first node with a data field of 3 was removed")

	print("Full linked list (as a Python list):", new_linked_list.get_full_list())