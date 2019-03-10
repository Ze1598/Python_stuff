'''
Reverse the order of the digits in a string. Keep removing the units digit
from the input number it the number is smaller than 1 (take the modulo of
dividing the number by 10 and add it to the result. Before adding,
multiply the current result by 10 so that the new digit is added as the
units digits).
'''


def reverse_int (x):

	# Variable to hold the reversed integer
	result = 0

	# Loop, that is, remove the units digit of the number until the number\
	# is less than 1 (a decimal which, when converted with the `int()`\
	# function is converted to zero)
	while (x > 0):
		# Get the module of dividing the number by 10 to obtain the current\
		# units digit
		remainder = int(x % 10)
		# Multiply the current result by 10 and then add the calculated modulo,\
		# so that the module (the obtained units digit) is added as the new units\
		# digit to the result
		result = (result * 10) + remainder
		# Divide the number by 10, that is, effectively remove its units digit
		x = int(x / 10)

	return result


from random import randint

for i in range(5):
	num = randint(100, 1000)
	print(num, "->", reverse_int(num))