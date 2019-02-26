from itertools import combinations
from random import randint
from math import sqrt
import unittest

def find_sum_pairs (num_list, sum_value):
	'''
	Finds the combinations of two numbers in a given
	list that add up to a given value.

	Parameters
	----------
	num_list : list
		The list of numbers to search for pairs in.
	sum_value : int
		The value to which the pairs must add up to.

	Returns
	-------
	valid_pairs : list
		A list of pairs that add up to the desired 
		value.
	'''

	# From all the possible ways that two numbers can be\
	# paired up from the input list, create a list that\
	# contains only the pairs which add up to the desired\
	# value
	valid_pairs = [pair for pair in combinations(num_list, 2) if (sum(pair) == sum_value)]

	# Alternative code:	
	# valid_pairs = list()
	# for pair in combinations(num_list, 2):
	# 	if sum(pair) == sum_value:
	# 		valid_pairs.append(pair)

	return valid_pairs


def find_sum_pairs_v2 (num_list, sum_value):
	'''
	Finds the combinations of two numbers in a given
	list that add up to a given value.

	Parameters
	----------
	num_list : list
		The list of numbers to search for pairs in.
	sum_value : int
		The value to which the pairs must add up to.

	Returns
	-------
	valid_pairs : list
		A list of pairs that add up to the desired 
		value.
	'''

	# List to hold the pairs that add up to the desired valued
	valid_pairs = list()
	# We won't check numbers smaller than this
	stop_point = int(sqrt(max(num_list)))

	# Loop through all the numbers between the stop point and the\
	# greatest number in the input list
	for i in range(stop_point, max(num_list)+1):
		# The complement to the current number
		difference = sum_value - i
		# Both the current number and its complement need to be\
		# present in the list to be considered a valid pair
		if (i in num_list) and (difference in num_list):
			# Looking for combinations, so we only want the pairs that\
			# remain equal when sorted (which means it's the first time\
			# being found)
			if tuple(sorted((difference, i))) == (difference, i):
				valid_pairs.append((difference, i))

	# Reverse the order of the list to sort it by the first element of\
	# each pair
	return valid_pairs[::-1]


test1_result = [(0, 75), (1, 74), (2, 73), (3, 72), (4, 71), (5, 70), (6, 69), (7, 68), (8, 67), (9, 66), (10, 65), (11, 64), (12, 63), (13, 62), (14, 61), (15, 60), (16, 59), (17, 58), (18, 57), (19, 56), (20, 55), (21, 54), (22, 53), (23, 52), (24, 51), (25, 50), (26, 49), (27, 48), (28, 47), (29, 46), (30, 45), (31, 44), (32, 43), (33, 42), (34, 41), (35, 40), (36, 39), (37, 38)]
class Test (unittest.TestCase):
	def test1 (self):
		self.assertEqual(find_sum_pairs(list(range(0,101)), 75), test1_result)

	def test2 (self):
		self.assertEqual(find_sum_pairs_v2(list(range(0,101)), 75), test1_result)

unittest.main()