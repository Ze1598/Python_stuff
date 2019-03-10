'''
	The tree data structure is quite similar with its natural counterpart,
except that in computer science trees have their roots at the top, with
the leaves (nodes) sprawling downwards. A tree can be defined in two ways:
the first involves nodes and edges, while the second involves recursion.
	
	First definition: a tree consists of a set of nodes and a set of edges
that connects pairs of nodes. Every tree has the following properties:
	* A single node of the tree is designed as the root;
	* Every node n, except the root, is connected by an edge from one other
	node p, where p is the parent node of n;
	* A unique path traverses from the root to each node;
	* If each node in the tree has two or less children, it is called a
	binary tree.

	Second definition: a tree is either empty or consists of a root and zero
or more subtrees, where each subtree is also a tree. The root of each subtree
is connected to the root of the parent tree by an edge.
'''
'''
The following are some fundamental concepts and definitions of trees:
	
	* Node: a node is one element in a tree. It can have a name (called a
	key), as well as additional information (called payload).

	* Edge: an edge connects two nodes to prove there is a relationship
	between them. Every node, except the root, is connected by one incoming
	edge; however it can have multiple outgoing edges.

	* Root: the first node of from where the rest of the tree originates. As
	the first node, it has no incoming edges.

	* Path: ordered list of nodes that are connected by edges.

	* Children: the set of nodes that sprung from one single node (this means
	the children are located in the level below that of its parent).

	* Parent: a node that sprungs at least one node (this means the parent is
	located in the level above that of its children).

	* Sibling: nodes that sprung from the same parent node are called siblings.

	* Subtree: a section of a tree comprised by a set of nodes and edges.

	* Leaf node: a node with no children. 

	* Level: the number of edges on the path between the root and the node n.

	* Height: the height of a tree is equal to the maximum level of any node
	in the tree.
'''

# Example using separate functions and a list of lists to create and insert nodes in\
# a binary tree
# Note that when a root is mentioned it is in the context of the root of a subtree, not\
# necessarily the root of the tree as a whole
# ------------------------------------------------------------------------------------

# Create a new tree
def binary_tree (root):
	return [ root, ['X'], ['X'] ]

# Insert a left node. If the left child of the given root is empty, simply add a new node;\
# else, the new node is added as the root's left child and the previous left child is pushed\
# down one level as the left child of the new node
def insert_left (root, new_node):
	temp_node = root.pop(1)
	if len(temp_node) > 1:
		root.insert(1, [ new_node, temp_node, ['X'] ])
	else:
		root.insert(1, [ new_node, ['X'], ['X'] ])
	return root

# Insert a right node. If the right child of the given root is empty, simply add a new node;\
# else, the new node is added as the root's right child and the previous right child is pushed\
# down one level as the right child of the new node
def insert_right (root, new_node):
	temp_node = root.pop(2)
	if len(temp_node) > 1:
		root.insert(2, [new_node, ['X'], temp_node])
	else:
		root.insert(2, [new_node, ['X'], ['X']])
	return root

# Get the root of the given (sub)tree
def get_root (root):
	return root[0]

# Set a new root for the (sub)tree
def set_root (root, new_root):
	root[0] = new_root

# Get the left child of the (sub)tree
def get_left_child (root):
	return root[1]

# Get the right child of the (sub)tree
def get_right_child (root):
	return root[2]


tree = binary_tree(1)
tree = insert_left(tree, 2)
#	1
# 2
tree = insert_right(tree, 3)
#    1
#  2   3
tree = insert_right(get_left_child(tree), 5)
#     1
#   2   3
#    5
print(tree)
# ------------------------------------------------------------------------------------



# The following is the implementation of a Binary Tree using a Python class
# ------------------------------------------------------------------------------------

class BinaryTree:
	'''
	Implement a Binary Tree. Instead of creating node objects for each node,
	each node represents the root node of its own (sub)tree. 
	In this implementation, nodes only have a payload, that is, the value they
	hold.

	Attributes
	----------
	root : int
		The root.
	left_child : __main__BinaryTree
		The left child of the root. The child itself is the root of the original
		root's left subtree.
	right_child : __main__BinaryTree
		The right child of the root. The child itself is the root of the original
		root's right subtree.

	Methods
	-------
	insert_left (new_node)
		Insert a left child for the root of the current (sub)tree.
	insert_right (new_node)
		Insert a right child for the root of the current (sub)tree.
	get_right_child ()
		Get the right child of the root of the current (sub)tree.
	get_left_child ()
		Get the left child of the root of the current (sub)tree.
	set_root ()
		Set a new value for the root of the current (sub)tree.
	get_root ()
		Get the root of the current (sub)tree.
	'''

	def __init__ (self, root):
		self.root = root
		self.left_child = None
		self.right_child = None

	# The new node is inserted as the left child of the root of the current (sub)tree.\
	# If a node already exists, it is pushed down one level as the left child of\
	# the new node
	def insert_left (self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	# The new node is inserted as the right child of the root of the current (sub)tree.\
	# If a node already exists, it is pushed down one level as the right child of\
	# the new node
	def insert_right (self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
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

# Create a new binary tree with 1 as its root
new_tree = BinaryTree(1)
# Insert a left child
new_tree.insert_left(2)
# Insert a right child
new_tree.insert_right(3)
# Insert a left child for the first left child of the tree
new_tree.get_left_child().insert_left(5)
# Insert a right child for the first right child of the tree
new_tree.get_right_child().insert_right(7)

# ------------------------------------------------------------------------------------