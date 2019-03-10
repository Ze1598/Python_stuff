# Look for an integer in a shuffled list
from random import shuffle, randint


def shuffled_bin_search (x):
	'''
	Find the index of a given integer in a shuffled list.

	Parameters
	----------
	x : int
		The number we are looking for.

	Returns
	-------
	middle : int
		The index at which the target integer is located at.
	'''

	# Create and shuffle a list with the integers between 1 and 100, inclusive
	a = list(range(1,101))
	shuffle(a)

	# At first, the middle is the middle of the whole list
	middle = len(a) // 2
	# The lower bound starts as the beginning of the list
	low = 0
	# The upper bound starts as the end of the list
	high = len(a) - 1
	

	# Run the loop until we find what we are looking for
	while True:
		# If the number at index `middle` is the one we are looking for,\
		# then return that index (the answer)
		if x == a[middle]:
			return middle

		# Else, update the lower or upper bounds as necessary
		else:
			# If the target number is between the lower bound and the middle,\
			# then update the upper bound to be the middle and calculate the\
			# middle again
			if x in a[low : middle+1]:
				high = middle
				middle = (low+high) // 2

			# If the target number is between the middle and the upper bound,\
			# then update the lower bound to be the middle and calculate the\
			# middle again
			elif x in a[middle: high+1]:
				low = middle
				middle = (low+high) // 2


if __name__ == "__main__":
	for i in range(3):
		num = randint(1, 101)
		print(f"{num} is at index {shuffled_bin_search(num)}")