'''
Convert a given base-10 integer to any base using a stack data structure.
'''

# Create a class for the stack
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


def base_conv(num, base):
	'''
	Convert a base-10 integer into any base.

	Paramaters
	----------
	num : int
		The base-10 integer to be converted.
	base : int
		The target base for the resulting number.

	Returns
	-------
	result : str
		The converted number.
	'''
	
	# If the input number is 0 then just return 0 straight away
	if num == 0:
		return "0"

	else:
		# Each item of the stack corresponds to a digit of the resulting\
		# number (the order of removal is the order of the digits in\
		# the resulting number, i.e., the first item to be removed is the\
		# first digit in the result, and so on)
		digit_stack = Stack()

		# The digits that can be used for the conversion
		conv_digits = "0123456789ABCDEF" 

		# While the input number is larger than zero, we can still divide it\
		# further
		while num > 0:
			# Find the remainder of dividing the current value of the number\
			# by the desired base
			remainder = num % base
			# Actually (floor) divide the number
			num //= base
			# Push the remainder to the stack
			digit_stack.push(remainder)

		# String to hold the converted number
		result = ""
		# Remove everything from the stack to build the converted number (the\
		# order of the digits is the order of removal from the stack)
		while (not digit_stack.is_empty()):
			result += conv_digits[digit_stack.pop()]

	return result


if __name__ == "__main__":
	print(base_conv(0, 2))
	print(base_conv(42, 2))
	print(base_conv(25, 8))
	print(base_conv(25, 16))
	print(base_conv(42, 5))
	print(base_conv(42, 5))
	print(base_conv(256, 16))