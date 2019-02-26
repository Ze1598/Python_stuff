# This file goes over binary tree traversals: preorder, inorder and postorder
'''
	pre-order: start by visiting the root node, then recursively traverse through
the left subtree until reaching a leaf node. Then apply the same method to the
right subtree.
	in-order: recursively traverse the left subtree, then visit the root node and
after that traverse the right subtree.
	post-order: recursively traverse the left subtree, then the right subtree and
lastly the root node.
'''

class Binary_Tree:
	def __init__ (self, root):
		self.root = root
		self.left_child = None
		self.right_child = None

	# The new node is inserted as the left child of the root of the current (sub)tree.\
	# If a node already exists, it is pushed down one level as the left child of\
	# the new node
	def insert_left (self, new_node):
		if self.left_child == None:
			self.left_child = Binary_Tree(new_node)
		else:
			t = Binary_Tree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	# The new node is inserted as the right child of the root of the current (sub)tree.\
	# If a node already exists, it is pushed down one level as the right child of\
	# the new node
	def insert_right (self, new_node):
		if self.right_child == None:
			self.right_child = Binary_Tree(new_node)
		else:
			t = Binary_Tree(new_node)
			t.right_child = self.right_child
			self.right_child = t

	# Get the right child of the current (sub)tree
	def get_right_child (self):
		return self.right_child

	# Get the left child of the current (sub)tree
	def get_left_child (self):
		return self.left_child

	# Set a new root for the (sub)tree
	def set_root (self, new_root):
		self.root = new_root

	# Get the root of the (sub)tree
	def get_root (self):
		return self.root

	# Pre-order traversal
	def preorder (self):
		'''
		Start by visiting the root node, then recursively traverse through
		the left subtree until reaching a leaf node. Then apply the same
		method to the right subtree.
		Simply print out each node.
		'''
		print(self.root, end="-")
		if self.left_child != None:
			self.left_child.preorder()
		if self.right_child != None:
			self.right_child.preorder()

	# Post-order traversal
	def postorder (self):
		'''
		Start by visiting the left subtrees. Then visit the right subtrees.
		Only then, visit the root nodes.
		'''
		if self.left_child != None:
			self.left_child.postorder()
		if self.right_child != None:
			self.right_child.postorder()
		print(self.root, end="-")

	# In-order traversal
	def inorder (self):
		'''
		Start by visiting the left subtrees, then the root and lastly the right
		subtrees.
		'''
		if self.left_child != None:
			self.left_child.inorder()
		print(self.root, end="-")
		if self.right_child != None:
			self.right_child.inorder()


# Create a new binary tree with 1 as its root
new_tree = Binary_Tree(1)
# Insert a left child
new_tree.insert_left(2)
# Insert a right child
new_tree.insert_right(3)
# Insert a left child for the first left child of the tree
new_tree.get_left_child().insert_left(5)
# Insert a right child for the first right child of the tree
new_tree.get_right_child().insert_right(7)
# Use pre-order traversal in the tree, that is, we'll output the nodes\
# of the tree in the exact order that they are stored (left to right,\
# top to bottom)
print("Pre-order traversal:")
new_tree.preorder()
print()
# Use post-order traversal in the tree so that the left subtrees are\
# visited first, the right subtrees second and the root nodes last\
# (the very first node visited is the deepest and leftmost leaf node,\
# while the tree's root node is the last one)
print("Post-order traversal:")
new_tree.postorder()
print()
# Use in-order traversal in the tree so that the output will output the\
# values saved in tree sorted by ascending order
print("In-order traversal:")
new_tree.inorder()
print()