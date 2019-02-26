from random import randint

def sieve (x):
	'''
	Find all the prime numbers between 2 and `x`.
	For this, we are using the Sieve of Eratosthenes, that is, from the list
	of all integers between 2 and `x`, we loop from left to right, one number
	at a time to remove all multiples of that number from the list.

	Parameters
	----------
	x : int
		The upper bound for the integers to test for primality.

	Returns
	-------
	lst : list
		The list of prime numbers between 2 and `x`.
	'''

	# Create the initial list with all consecutive integers between 2 and x, inclusive
	lst = list(range(2, x+1))
	# Keep track of the index we are looking at from the list to use the corresponding\
	# number as the primality factor
	factor = 0
	# Loop until we find the final answer
	while True:
		# Filter out of the list the multiples of the current factor
		lst = list(filter(lambda x: x%lst[factor]!=0 or x==lst[factor], lst))
		# Increment this variable by one so that we can test the next factor in the next\
		# iteration
		factor += 1
		# If `factor` equals or surpasses the square root of `x`, then return the list\
		# as it is, i.e., the final answer
		if factor >= round(x**0.5):
			return lst



if __name__ == "__main__":
	for i in range(5):
		x = randint(10, 10000)
		print(f"Primes between 2 and {x}:")
		print(sieve(x))
		print()
		print()