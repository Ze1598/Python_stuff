'''
Implement a palindrome checker using a deque data structure.
'''

# Class to implement deques
class Deque ():
	def __init__ (self):
		self.items = []

	def is_empty (self):
		return self.items == []

	def add_front (self, item):
		self.items.insert(0, item)

	def add_rear (self, item):
		self.items.append(item)

	def remove_front (self):
		return self.items.pop(0)


	def remove_rear (self):
		return self.items.pop()

	def size (self):
		return len(self.items)


def palind_checker (string):
	'''
	Function to test if a given string is a palindrome, using
	a deque.

	Parameters
	----------
	string : str
		The string to be tested.

	Returns
	-------
	bool
		True if the string is a palindrome; else False.
	'''

	# Create an empty deque
	char_deque = Deque()

	# Add each character to the deque
	for char in string:
		# Simply append each character to the deque
		char_deque.add_rear(char)

	# Each iteration remove one character from the front and another from\
	# the rear of the deque. If they are not the same character, it means\
	# this is not a deque

	# Let the loop run while the deque has more one character since the string\
	# in case the string has an odd number characters (in that case there will\
	# be one leftover character in the deque)
	while char_deque.size() > 1:
		front_char = char_deque.remove_front()
		rear_char = char_deque.remove_rear()
		if front_char != rear_char:
			return False

	# If the function executed until this point, it means the string is indeed\
	# a palindrome
	return True


if __name__ == "__main__":
	print(palind_checker("lsdkjfskf"))
	print(palind_checker("radar"))