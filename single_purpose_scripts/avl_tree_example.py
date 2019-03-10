'''
An AVL tree is a self-balancing binary search tree. It was the first such data
structure to be invented.
In an AVL tree, the heights of the two child subtrees of any node differ by one
or less. If, at any time, they differ by more than one, rebalancing is done to
restore this property.
'''
'''
The balance factor of a node N is defined to be the height difference
	BalanceFactor(N) = Height(RightSubtree(N)) – Height(LeftSubtree(N))
of its two child subtrees.
A binary tree is defined to be an AVL tree if the BalanceFactor of each node in
the tree is in the inclusive range of -1 to 1.
A node N with BalanceFactor < 0 is called "left-heavy", one with
BalanceFactor > 0 is called "right-heavy", and one with BalanceFactor = 0 is
sometimes simply called "balanced".
'''

# Class to create nodes for the binary search tree
class TreeNode ():
	'''
	Represents a single node in the tree.

	Attributes
	----------
	key : str
		The that represents the node.
	payload : int
		The value held by the node.
	left_child : __main__.TreeNode
		The left child of this node.
	right_child : __main__.TreeNode
		The right child of this node.
	parent : __main__.TreeNode
		The parent of this node.
	balance_factor : int
		The balance factor of the node's subtrees.

	Methods
	-------
	has_left_child ()
		Check if the node has a left child.
	has_right_child ()
		Check if the node has a right child.
	has_any_children ()
		Check if the node has at least one child.
	has_both_children ()
		Check if the node has both children.
	is_left_child ()
		Check if the node is the left child of its parent.
	is_right_child ()
		Check if the node is right child of its parent.
	is_root ()
		Check if the node is the root node.
	is_leaf ()
		Check if the node is a leaf node.
	replace_node_data (key, value, lc, rc)
		Replace some information about the node: its key, its
		payload, its left child and/or its right child.
	splice_out ()
		Remove a successor node from its position and establish the
		link between the surrouding nodes.
	find_successor ()
		Find a successor for a deleted node.
	find_min ()
		Find the node that holds the smallest payload in the tree
		(the left-most child of the tree).
	'''

	def __init__ (self, key, val, left=None, right=None, parent=None):
		'''
		key: the key for this node.
		val: the value for this node.
		left: reference to the left child of this node. Defaults to `None`.
		right: reference to the right child of this node. Defaults to `None`.
		parent: reference to the parent of this node. Defaults to `None`.
		balance_factor: the balance factor of the node. Start at zero, that is,
		initially, consider the node to be balanced.
		'''
		self.key = key
		self.payload = val
		self.left_child = left
		self.right_child = right
		self.parent = parent
		self.balance_factor = 0

	# Has children?
	# -----------------------------------------------------------------------------
	def has_left_child (self):
		return self.left_child

	def has_right_child (self):
		return self.right_child

	def has_any_children (self):
		return self.left_child or self.right_child

	def has_both_children (self):
		return self.left_child and self.right_child
	# -----------------------------------------------------------------------------
	
	# The node is a left or right child?
	# -----------------------------------------------------------------------------
	def is_left_child (self):
		return self.parent and self.parent.left_child == self

	def is_right_child (self):
		return self.parent and self.parent.right_child == self
	# -----------------------------------------------------------------------------

	def is_root (self):
		return not self.parent

	# To be a leaf, the node can't have any children
	def is_leaf (self):
		return not (self.left_child or self.right_child)

	def replace_node_data (self, key, value, lc, rc):
		'''
		lc: left child.
		rc: right child.
		'''
		self.key = key
		self.payload = value
		self.left_child = lc
		self.right_child = rc
		if self.has_left_child():
			self.left_child = self
		if self.has_right_child():
			self.right_child = self


	# Remove the successor node and establish the connections between nodes
	# where the sucessor is removed
	def splice_out (self):
		'''
		Method responsible for, when deleting a node from the tree, removing its
		successor (the node which will replace the deleted node) and connect the
		successor's children and parent nodes.
		There are three possible scenarios: (1) the successor is a leaf node and
		so we just need to remove the reference to it from the parent; (2) the
		successor has a left child and its parent will now reference this child
		instead of the successor; (3) the successor has a right child and its
		parent will now reference this child instead of the successor.
		'''

		# (1) If the node is a leaf
		if self.is_leaf():
			# Remove the reference to it from its parent (dependant on which child\
			# the successor is)
			if self.is_left_child():
				self.parent.left_child = None
			else:
				self.parent.right_child = None

		# Otherwise, the successor has at least one child
		elif self.has_any_children():
			# (2) The successor has a left child
			if self.has_left_child():
				# If the successor itself is a left child
				if self.is_left_child():
					# The parent's left child will point to the successor's left child
					self.parent.left_child = self.left_child
				# Otherwise, the successor is a right child
				else:
					self.parent.right_child = self.right_child
				# No matter what child the successor was, make its parent the parent\
				# of its left child
				self.left_child.parent = self.parent

			# (3) The successor has a right child
			# The process is iddentical to what is done above, except here we are\
			# worried about the successor's right child
			else:
				if self.is_left_child():
					self.parent.left_child = self.right_child
				else:
					self.parent.right_child = self.right_child
				self.right_child.parent = self.parent


	# Find the successor of the deleted node (the node that will replace it)
	def find_successor (self):
		'''
		Find the successor node when a node is deleted from the tree.
		There are three conditions for a node to be considered the successor:
		(1) if the deleted node has a right child, then the successor is the
		one with the smallest key in the right subtree; (2) if the deleted
		node has no right child and is the left child of its parent, then
		the parent is the successor; (3) if the node is the right child of
		its parent and the node itself doesn't have a right child, then the
		successor is the successor of the parent (excluding this deleted node).
		'''

		# The successor node
		succ = None
		# (1) The node has a right child
		if self.has_right_child():
			# Then the successor is the node with the smallest key in the deleted\
			# node's right subtree
			succ = self.right_child.find_min()

		# If the node doesn't have a right child
		else:
			# If the node has a parent
			if self.parent:
				# (2) If the deleted node is the left child of its parent, then the
				# parent is the successor
				if self.is_left_child():
					succ = self.parent
				# Otherwise, the deleted node is the right child
				else:
					# Then look for the successor for the parent of the deleted node
					# Remove the reference to the parent's right child so that the\
					# deleted node can't be picked as the successor
					self.parent.right_child = None
					succ = self.parent.find_successor()
					# Restore the deleted node has its parent right child because this\
					# method is not responsible for deleting nodes
					self.parent.right_child = self

		# Finally, return the successor node
		return succ


	# Find the node with the minimum key in the whole tree (left-most child)
	def find_min (self):
		'''
		Utility method to find the node with the minimum key in the tree (the left-most
		child).
		'''

		# The node we are currently at (start at the node from which this method was\
		# called from)
		current = self
		# Keep moving down the tree while the current node has a left child (since we are\
		# only interested in moving down and towards the left-most child)
		while current.has_left_child():
			current = current.left_child
		# Return the node with the smallest key
		return current


	# Overload the `iter()` method for the tree so that we can iterate it inorder
	def __iter__ (self):
		'''
		Because this is an inorder traversal, first visit the left child, then
		the node itself and then the right child.
		'''
		if self:
			# Visit the left child
			if self.has_left_child():
				for elem in self.left_child:
					yield elem

			# Visit the node itself
			yield self.key

			# Visit the right child
			if self.has_right_child():
				for elem in self.right_child:
					yield elem




# Class to create a Binary Search Tree
class BinarySearchTree ():
	'''
	Implement a Binary Search Tree, that uses the __main__.TreeNode class
	to represent individual nodes.

	Attributes
	----------
	root : __main__.TreeNode
		The root node of the tree.
	size : int
		The size of the tree, that is, the number of existing nodes.

	Methods
	-------
	length ()
		Get the size of the tree.
	put (key, val)
		Insert a new node with a `key` key and payload `val` in the correct
		position.
	_put (key, val, current_node)
		Method used for actually insert the node by recursively searching
		the subtrees for the correct insert position.
	get (key)
		Return the node with a key `key` if it exists.
	_get (key, current_node)
		Method used for actually retrieving the node by recursively searching
		the subtrees for the node with the desired key.
	delete (key)
		Delete the first node with key `key`.
	remove (current_node)
		Method used for actually deleting a node, by recursively searching
		the subtrees and calling the necessary helper methods.
	'''

	# The constructor simply creates two attributes: the root and the size,\
	# both with an initial value of `None`
	def __init__ (self):
		self.root = None
		self.size = 0

	# Get the length (number of nodes) of the tree
	def length (self):
		return self.size


	# Add a new node to the tree
	# -----------------------------------------------------------------------------

	# Main ("public") method for adding a new node (responsible for calling the\
	# necessary helper method)
	def put (self, key, val):
		'''
		Add a new node to the tree. If there is no root, then the node is\
		added as the root; otherwise, we recursively search the tree (with\
		the `_put()` method) to find where to insert the node.
		'''

		# If the tree already has a root, recursively search the tree for\
		# where to insert the new node
		if self.root:
			# The search starts at the root
			self._put(key, val, self.root)

		else:
			self.root = TreeNode(key, val)

		# The tree grew because we added one new node
		self.size += 1


	# "Private" method for actually inserting the new node in the tree
	def _put (self, key, val, current_node):
		'''
		Method to recursively search the tree for where to insert the new node
		with key `key` and value `val`.
		This method is a "private method", that is, it is not to be called
		outside the class, only through the original and public `put()` method.
		'''

		# If the key we want to use for the new node is smaller than that of\
		# the current node, then we need to search in the left subtree
		if key < current_node.key:
			# If the current node has a left child, then move down to that child\
			# and repeat the search
			if current_node.has_left_child():
				self._put(key, val, current_node.left_child)
			# Otherwise, we have found where to insert the new node
			else:
				current_node.left_child = TreeNode(key, val, parent=current_node)

		# Otherwise, the new key is equal to or bigger than that of the current\
		# node and thus search the right subtree
		else:
			# If the current node has a right child, then move down to that child\
			# and repeat the search
			if current_node.has_right_child():
				self._put(key, val, current_node.right_child)
			# Otherwise, we have found where to insert the new node
			else:
				current_node.right_child = TreeNode(key, val, parent=current_node)
	# -----------------------------------------------------------------------------


	# Retrieve (get) a node from the tree
	# -----------------------------------------------------------------------------

	# Main ("public") method for retrieving a node (calls the necessary helper method)
	def get (self, key):
		'''
		Retrieve a node from the tree, given its key, by recursively searching the
		tree (with the help of the `_get()` method).
		'''

		# Only search if the tree has a root
		if self.root:
			# Search the tree (starting at the root) for a node with a key `key`
			res = self._get(key, self.root)
			# If the node was found, return its payload (value)
			if res:
				return res.payload
			# Otherwise, just return `None`
			else:
				return None

		# If the tree doesn't have a root then we don't need to search at all
		else:
			return None

	# "Private" method for actually getting a node
	def _get (self, key, current_node):
		'''
		Method to recursively search the tree for a node with key `key`.
		This method is a "private method", that is, it is not to be called
		outside the class, only through the original and public `get()` method.
		'''

		# If we reached a leaf node, then it means the node we want doesn't exist
		if not current_node:
			return None
		# Found the node we want
		elif current_node.key == key:
			return current_node
		# If the key is smaller than that of the current node, move down to its\
		# left child
		elif key < current_node.key:
			return self._get(key, current_node.left_child)
		# Else, it means the key is equal to or larger than that of the current node,\
		# so move down to its right child
		else:
			return self._get(key, current_node.right_child)
	# -----------------------------------------------------------------------------


	# Delete a node
	# -----------------------------------------------------------------------------
	
	# Actually delete a node from the tree
	def delete (self, key):
		'''
		Remove a node with the given key from the tree. There are four
		possible outcomes regarding node deletion: there are at least
		two nodes and the node with the target key can either (1) exist
		or (2) not (the latter raises an exception); (3) there is only
		the root and it holds the target key; lastly, (4) the tree has
		zero nodes, thus, the deletion raises an exception.
		'''

		# If there are at least two nodes in the tree (the root and one
		# or more other nodes)
		if self.size > 1:
			# Try to get the target node from the tree
			node_to_remove = self._get(key, self.root)
			# (1) If the node was found, remove it
			if node_to_remove:
				self.remove(node_to_remove)
				self.size -= 1
			# (2) If the node was not found, raise an exception
			else:
				raise KeyError("Error, key not in tree")

		# (3) Else, if there's only the root in the tree and its key is the
		# target key, then remove it (the tree becomes empty)
		elif (self.size == 1) and (self.root.key == key):
			self.root = None
			self.size -= 1

		# (4) Otherwise, the tree is empty or the root node does not hold
		# the target key, thus raise an exception
		else:
			raise KeyError("Error, key not in tree")


	# Main method to delete a node. It is responsible for calling the necessary helper\
	# methods
	def remove (self, current_node):
		'''
		Helping method for actually deleting a node from the tree.
		There are three possible cases: (1) the node to be deleted is a leaf
		node and so we just need to remove the reference to it from its
		parent; (2) the node has two children and so we need to look for a
		successor node and put it in the place of the deleted node (while
		calling another method that is responsible for executing this process
		and keeping the tree balanced); and, lastly, (3) the node has only one
		child and thus we establish a parent-child relationship between the
		deleted node's parent and whichever type of child the node's child is.
		'''

		# (1) For the leaf node, we just need remove the child reference from the node's\
		# parent
		if current_node.is_leaf():
			if current_node == current_node.parent.left_child:
				current_node.parent.left_child = None
			else:
				current_node.parent.right_child = None

		# (2) The node has two children
		elif current_node.has_both_children():
			# Find the successor
			succ = current_node.find_successor()
			# Remove the successor from its place
			succ.splice_out()
			# Delete the target node by replacing it with the successor
			current_node.key = succ.key
			current_node.payload = succ.payload

		# (3) The node has only one child
		else:
			# If the child has a left child
			if current_node.has_left_child():
				# If the node is a left child, then establish a parent-left\
				# child relationship between its parent and its left child
				if current_node.is_left_child():
					current_node.left_child.parent = current_node.parent
					current_node.parent.left_child = current_node.left_child
				# If the node is a right child, then establish a parent-right\
				# child relationship between its parent and its right child
				elif current_node.is_right_child():
					current_node.left_child.parent = current_node.parent
					current_node.parent.right_child = current_node.left_child
				# Otherwise, the node is the root. Thus, simply replace its data
				else:
					current_node.replace_node_data(
						current_node.left_child.key,
						current_node.left_child.payload,
						current_node.left_child.left_child,
						current_node.left_child.right_child
					)

			# Otherwise, it has a right child. The process is the same as above,\
			# except it's for the right child of the deleted node
			else:
				if current_node.is_left_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.left_child = current_node.right_child
				elif current_node.is_right_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.right_child = current_node.right_child
				else:
					current_node.replace_node_data(
						current_node.right_child.key,
						current_node.right_child.payload,
						current_node.right_child.left_child,
						current_node.right_child.right_child
					)
	# -----------------------------------------------------------------------------


	# Operator overloads
	# -----------------------------------------------------------------------------
	# When calling the `len()` function on an object of this class, return the\
	# `size` attribute
	def __len__ (self):
		return self.size

	# Set the __iter__ method such that it creates an iterator for the root\
	# of the tree
	def __iter__ (self):
		return self.root.__iter__()

	# Overload the brackets ([]) operator so that new nodes can be added using\
	# dictionary syntax (e.g., `my_BST["sample_node"] = 5`)
	def __setitem__ (self, k, v):
		'''
		k: key of the node.
		v: value of the node.
		'''
		self.put(k, v)

	# This overload allows us to get nodes using dictionary syntax (e.g.,\
	# `my_node_value = my_BST["sample_key"]`)
	def __getitem__ (self, key):
		return self.get(key)

	# Overload the `in` operator to check membership of keys in the tree\
	# (e.g., `sample_value in my_BST`)
	def __contains__ (self, key):
		# Simply try to get the key from the tree. If it's not possible, then\
		# the key is not in the tree (`False`); if it returns a value, then\
		# the key is in the tree (`True`)
		if self._get(key, self.root):
			return True
		else:
			return False

	# Overload the `del` operator so we can use it with the tree as if this was\
	# a dictionary (e.g., `del my_BST["sample_key"])
	def __delitem__ (self, key):
		self.delete(key)
	# -----------------------------------------------------------------------------



# Create a new class for the AVL binary search tree, which inherits from the\
# original binary search tree (`BinarySearchTree`) class (though some methods\
# are overriden in this class, along with the addition of new ones)
class AVLBinarySearchTree (BinarySearchTree):
	'''
	Implement a AVL Binary Search Tree by inheriting the original
	__main__.BinarySearchTree class. This class overwrites and creates
	some methods to incorporate the tree balance property.

	Attributes
	----------
	root : __main__.TreeNode
		The root node of the tree.
	size : int
		The size of the tree, that is, the number of existing nodes.

	Methods
	-------
	length ()
		Get the size of the tree.
	put (key, val)
		Insert a new node with a `key` key and payload `val` in a position
		that keeps the tree balanced.
	_put (key, val, current_node)
		Method used for actually insert the node by recursively searching
		the subtrees for the correct insert position (that is, the position
		where the balance of the tree won't be negatively affected by the
		new node).
	get (key)
		Return the node with a key `key` if it exists.
	_get (key, current_node)
		Method used for actually retrieving the node by recursively searching
		the subtrees for the node with the desired key.
	delete (key)
		Delete the first node with key `key`.
	remove (current_node)
		Method used for actually deleting a node, by recursively searching
		the subtrees and calling the necessary helper methods.
	update_balance (node)
		Recursively update the balance factor of the nodes, starting at a given
		node and then working its way up to the root, excluded.
	rotate_left (old_parent)
		Swap a right child with its parent.
	rotate_right (old_parent)
		Swap a left child with its parent.
	rebalance (node)
		Adjust the tree in cases that performing a single swap isn't enough to
		make the tree balanced.
	'''

	# Override the `_put()` helper method so that when a new node is inserted\
	# we also update the balance for that new node
	def _put (self, key, val, current_node):
		# If the new node's key is smaller than that of the curren node, then it\
		# will be inserted in the left subtree
		if key < current_node.key:
			# If the current node already has a left child, then we go down the
			# left subtree to find where to insert the node
			if current_node.has_left_child():
				self._put(key, val, current_node.left_child)
			# Otherwise, the node is inserted as the left child and its balance is\
			# updated
			else:
				current_node.left_child = TreeNode(key, val, parent=current_node)
				self.update_balance(current_node.left_child)

		# If the new node's key is equal to or larger than that of the curren\
		# node, then it will be inserted in the right subtree
		else:
			# If the current node already has a right child, then we go down the
			# right subtree to find where to insert the node
			if current_node.has_right_child():
				self._put(key, val, current_node.right_child)
			# Otherwise, the node is inserted as the right child and its balance is\
			# updated
			else:
				current_node.right_child = TreeNode(key, val, parent=current_node)
				self.update_balance(current_node.right_child)


	# Recursively update the balance factor of the tree, starting at a given node\
	# and then works its way up to the root
	def update_balance (self, node):
		'''
		Update the balance for a given node (either put it back in the\
		[-1, 1] range or simply update its value
		'''

		# If the node's balance factor is outside the [-1,1] range, correct it
		if (node.balance_factor > 1) or (node.balance_factor < -1):
			self.rebalance(node)
			return

		# If this is not the root, then update the node balance factor
		if node.parent != None:
			# Left children add 1 to the balance factor
			if node.is_left_child():
				node.parent.balance_factor += 1

			# Right children subtract 1 from the balance factor
			elif node.is_right_child():
				node.parent.balance_factor -= 1

			# Only update the balance factor of the current node's parent\
			# if its factor is not zero
			if node.parent.balance_factor != 0:
				self.update_balance(node.parent)

	# Swap a right child with its parent (the child rotates to the left in the\
	# sense that it takes its parent place)
	def rotate_left (self, old_parent):
		'''
		old_parent: the parent of the node to be moved.
		'''

		# The node to be moved is the right child of the given node
		new_parent = old_parent.right_child
		old_parent.right_child = new_parent.left_child
		# If the moved node actually had a left child, update its parent
		if new_parent.left_child != None:
			new_parent.left_child.parent = old_parent

		# The parent of the moved node is the parent of its old parent
		new_parent.parent = old_parent.parent
		# If the parent of the moved node is the tree's root, then the\
		# moved node is now the root
		if old_parent.is_root():
			self.root = new_parent
		# Otherwise, update the parent of the moved node's parent to point\
		# to the moved node
		else:
			if old_parent.is_left_child():
				old_parent.parent.left_child = new_parent
			else:
				old_parent.parent.right_child = new_parent

		# Swap the relationship between the moved node and its parent (the node\
		# given as input for this method)
		new_parent.left_child = old_parent
		old_parent.parent = new_parent
		# And update the balance factor for these two nodes
		old_parent.balance_factor += 1 - min(new_parent.balance_factor, 0)
		new_parent.balance_factor += 1 - max(old_parent.balance_factor, 0)

	# Swap a left child with its parent (the child rotates to the right in the\
	# sense that it takes its parent place)
	# This method is iddentical to its `rotate_left()` counterpart, except that\
	# this one focuses in a left child
	def rotate_right (self, old_parent):
		'''
		old_parent: the parent of the node to be moved.
		'''

		# The node to be moved is the left child of the given node
		new_parent = old_parent.left_child
		old_parent.left_child = new_parent.right_child
		# If the moved node actually had a right child, update its parent
		if new_parent.right_child != None:
			new_parent.right_child.parent = old_parent

		# The parent of the moved node is the parent of its old parent
		new_parent.parent = old_parent.parent
		# If the parent of the moved node is the tree's root, then the\
		# moved node is now the root
		if old_parent.is_root():
			self.root = new_parent
		# Otherwise, update the parent of the moved node's parent to point\
		# to the moved node
		else:
			if old_parent.is_right_child():
				old_parent.parent.right_child = new_parent
			else:
				old_parent.parent.left_child = new_parent

		# Swap the relationship between the moved node and its parent (the node\
		# given as input for this method)
		new_parent.right_child = old_parent
		old_parent.parent = new_parent
		# And update the balance factor for these two nodes
		old_parent.balance_factor += 1 - min(new_parent.balance_factor, 0)
		new_parent.balance_factor += 1 - max(old_parent.balance_factor, 0)


	# Adjust the tree when performing a single left or right rotation is not enough\
	# to balance the tree
	def rebalance (self, node):
		# If the node is left-heavy, then check the balance of its right child\
		# to make the necessary rotations
		if node.balance_factor < 0:
			# If its right child is right-heavy, then rotate the child and then\
			# the node itself
			if node.right_child.balance_factor > 0:
				self.rotate_right(node.right_child)
				self.rotate_left(node)
			# Otherwise just rotate the node
			else:
				self.rotate_left(node)

		# If the node is right-heavt, then check the balance of its left child\
		# to make the necessary rotations
		elif node.balance_factor > 0:
			# If its left child is left-heavy, then rotate the child and then\
			# the node itself
			if node.left_child.balance_factor < 0:
				self.rotate_left(node.left_child)
				self.rotate_right(node)
			# Otherwise just rotate the node
			else:
				self.rotate_right(node)



if __name__ == "__main__":
	my_tree = BinarySearchTree()
	print("The tree was created")
	print("Size of the tree:", len(my_tree))
	
	print("Adding new nodes to the tree...")
	my_tree[3] = "panda"
	my_tree[4] = "koala"
	my_tree[6] = "platypus"
	my_tree[2] = "penguin"
	my_tree[7] = "elephant"
	my_tree[1] = "dog"
	print("Size of the tree:", len(my_tree))

	print("Value of node with key `6`:", my_tree[6])
	print("Value of node with key `2`:", my_tree[2])
	print("Value of node with key `1`:", my_tree[1])

	del my_tree[4]
	print("The node with key `4` was deleted")
	print("Size of the tree:", len(my_tree))

	print("Printing the whole tree...")
	for node in my_tree:
		print(f"my_tree[{node}] = {my_tree.get(node)}")