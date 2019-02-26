from random import randint
import unittest

def find_missing_numbers (num_list):
	'''
	Find n missing numbers in an array that
	contains the numbers from x to y, where
	x is the smallest number and y is the
	biggest.

	Parameters
	----------
	num_list : list
		The list of numbers with missing numbers.

	Returns
	-------
	list
		A list of missing numbers.
	'''

	# Convert the input list into a set (to remove duplicates)
	num_list = set(num_list)
	# Create a set that contains all numbers that should be in the input
	full_list = {x for x in range(min(num_list), max(num_list)+1)}
	# Return the resulting set of a XOR comparison between the input\
	# list (set) and the "complete" set
	return list(num_list ^ full_list)

class Test (unittest.TestCase):
	def test1 (self):
		self.assertEqual(find_missing_numbers([1,2,3,4,5,7,8,9,10]), [6])

	def test2 (self):
		self.assertEqual(find_missing_numbers([1,2,4,5,6,8,9,10]), [3,7])

	def test3 (self):
		self.assertEqual(find_missing_numbers([10,11,12,14,17]), [13,15,16])

unittest.main()