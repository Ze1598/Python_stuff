'''
Script to test if a given string of parentheses, braces
and brackets contains balanced symbols or not, i.e., for each
opening symbol there's a corresponding closing counterpart. For this,
we'll use a stack data structure.
'''

# Create a class for stacks
class Stack ():

	def __init__ (self):
		self.items = []

	def is_empty (self):
		return self.items == []

	def push (self, item):
		self.items.append(item)

	def pop (self):
		return self.items.pop()

	def peek (self):
		return self.items[len(self.items)-1]

	def size (self):
		return len(self.items)

def compare_symbols (open_symb, close_symb):
	'''
	Function to handle the comparison of opening and closing symbols.

	Parameters
	----------
	open_symb : str
		The opening symbol which was just removed from the stack.
	close_symb : str 
		The closing symbol which is the character from the input string
		being currently looked at.

	Returns
	-------
	bool
		True if the closing symbol is the corresponding of the opening
		symbol; else False.
	'''

	openers = "({["
	closers = ")}]"
	# If the opening symbol is the correct counterpart of the closing\
	# symbol then return True; else return False
	return openers.index(open_symb) == closers.index(close_symb)


def balanced_symbols (par_str):
	'''
	Function to test if a string of parentheses, braces
	and brackets contains balanced symbols or not.

	Parameters
	----------
	par_str : str
		A string containing (only) parentheses, brackets and
		braces.

	Returns
	-------
	balanced : bool
		True if the symbols are balanced; else False.
	'''

	# This stack will contain only opening symbols. For each\
	# closing symbol we come across, we'll remove an opening\
	# one from the stack. If it's not possible, it means the\
	# symbols are not balanced
	par_stack = Stack()
	# Holds True as long as we don't find an unbalanced pair of\
	# symbols. If we find, it means the string as a whole doesn't\
	# contain balanced symbols
	balanced = True
	# Variable to keep the track of the index of the input string we are\
	# looking at
	index = 0

	# Loop through the input string while we haven't reached its last\
	# character and we haven't found an unbalanced pair of symbols
	while ( (index < len(par_str)) and balanced ):
		# The character we are currently looking at
		char = par_str[index]

		# If the character is an opening symbol, add it to the stack
		if char in "({[":
			par_stack.push(char)
		
		# Else, if it is a closing symbol, try to remove an opening\
		# counterpart from the stack
		else:
		
			# If it's not possible to remove because the stack is empty, then\
			# the string contains unbalanced symbols
			if par_stack.is_empty():
				# This will make the loop stop
				balanced = False
		
			# If the stack is not empty, then we simply remove an opening\
			# symbol from it
			else:
				# The top item, which is the one being removed
				top = par_stack.pop()
				# Compare the opening symbol just removed from the stack and closing\
				# symbol being currently looked at from the input string. If they\
				# are the correct counterpart of each other, then everything's fine;\
				# else, it means the string does not contain balanced symbols
				if compare_symbols(top, char) == False:
					balanced = False

		# Increment the `index` to move on to the next character
		index += 1

	# After finishing the loop, if `balanced` still holds a value of True (i.e.,\
	# we haven't found any closing symbol without an opening counterpart) and\
	# the stack is empty (i.e., there is no leftover opening symbols), then the\
	# string contains balanced symbols; else it doesn't
	if ( balanced and par_stack.is_empty() ):
		return True
	else:
		return False

if __name__ == "__main__":
	print(balanced_symbols('((()))'))
	print(balanced_symbols('(()'))
	print(balanced_symbols('{{([][])}()}'))
	print(balanced_symbols('[{()]'))