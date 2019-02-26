# Use a binary tree to extract a mathematical expression from a list of
# strings. We'll use the stack data structure as a way to store subtrees
# of the binary tree so that we can move up to the parents of nodes


# Create a simple stack data structure to which we can push and pop\
# elements from
class Stack:
	def __init__ (self):
		self.items = []

	def push (self, new_item):
		self.items.append(new_item)

	def pop (self):
		return self.items.pop()

# Create a binary tree class
class Binary_Tree:
	def __init__ (self, root):
		self.root = root
		self.left_child = None
		self.right_child = None

	def insert_left (self, new_node):
		if self.left_child == None:
			self.left_child = Binary_Tree(new_node)
		else:
			t = Binary_Tree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insert_right (self, new_node):
		if self.right_child == None:
			self.right_child = Binary_Tree(new_node)
		else:
			t = Binary_Tree(new_node)
			t.right_child = self.right_child
			self.right_child = t

	def get_right_child (self):
		return self.right_child

	def get_left_child (self):
		return self.left_child

	def set_root (self, new_root):
		self.root = new_root

	def get_root (self):
		return self.root

	# Traverse through the tree to calculate the expression using the operators and\
	# operands saved in the nodes
	def evaluate (self, node):
		# Get the left and right children of the root of the current subtree
		left_child = node.get_left_child()
		right_child = node.get_right_child()

		# If neither child is a leaf node, that is, neither is None
		if (left_child!=None) and (right_child!=None):
			# The operator is always the root of the subtree
			operator = node.get_root()
			# Compute the appropriate operation by recursively traversing through the\
			# children until it reaches a leaf node. On the way to finding a leaf node,\
			# compute any operations it can on the way
			if operator == "+":
				return self.evaluate(left_child) + self.evaluate(right_child)
			elif operator == "-":
				return self.evaluate(left_child) - self.evaluate(right_child)
			elif operator == "*":
				return self.evaluate(left_child) * self.evaluate(right_child)
			elif operator == "/":
				return self.evaluate(left_child) / self.evaluate(right_child)
		# If the left, right or both children are None, just return the root, that is,\
		# the operator
		else:
			return node.get_root()


def create_expression (input_exp):
	# Create a new binary tree which starts with an "empty" root (i.e., it\
	# doesn't matter which value is used right now to create the root)
	new_tree = Binary_Tree('')
	# We'll start by being located at the root of this new tree
	current = new_tree
	# Create an empty stack (will be used to hold subtrees)
	stack = Stack()
	# Push the created tree to the stack
	stack.push(new_tree)
	# String to contain the whole expression
	exp_string = ""

	# Loop through the list with the elements of the expression
	for element in input_exp:
		
		# If it's an opening parenthesis, then create a left node for the\
		# current subtree, push the current subtree to the stack and move to\
		# the created left node
		if element == '(':
			exp_string += element
			current.insert_left('')
			stack.push(current)
			current = current.get_left_child()
		
		# If it's an operator, set the root of the current subtree to that\
		# operator and insert a right child in the subtree. Then, push it to the\
		# stack and move to the created right child
		elif element in '/*-+':
			exp_string += element
			current.set_root(element)
			current.insert_right('')
			stack.push(current)
			current = current.get_right_child()

		# If it's a closing parenthesis, the current node will be whatever subtree is\
		# popped off the stack (which allows us to move up to the parent of the current\
		# node)
		elif element == ')':
			exp_string += element
			current = stack.pop()

		# If it's a number, set the root of the subtree to be that number and the current\
		# node will be whatever subtree is popped off the stack (it will allow us to move\
		# up to the parent of the current child)
		else:
			exp_string += element
			current.set_root(int(element))
			current = stack.pop()

	print("Expression:", exp_string)
	# `evaluate()` will traverse through the complete binary tree and compute the result of\
	# the expression
	print("Tree evaluation:", new_tree.evaluate(new_tree))



exp1 = ['(', '3', '+', '(', '4', '*', '5' ,')',')']
create_expression(exp1)
print()
exp2 = ['(', '(', '10', '+', '5', ')', '*', '3', ')']
create_expression(exp2)
print()