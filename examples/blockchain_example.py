# Source of this example: https://www.codecademy.com/learn/introduction-to-blockchain
'''
	A simple script to create a blockchain along with blocks to fill it with.
	It includes a method for proof-of-work and another validating the blockchain.
'''

# Used for the blocks' timestamps
import datetime
# We'll use SHA-256 for hashing
from hashlib import sha256

class Block:
	"""
	A class used to represent a single block of the blockchain.

	Attributes
	----------
	time_stamp : datetime.datetime
		The time of creation of the block.
	transactions : dict
		A dictionary containing the information relative
		to a transaction that will be saved in the block.
	previous_hash : str
		The hash of the previous block.
	nonce : int
		The nonce (number used only once) value of the
		block (used for proof-of-work).
	hash : str
		The block's hash.

	Methods
	-------
	generate_hash()
		Generates the hash for the Block.
	print_contents()
		Prints each propety of the Block, individually.
	"""

	def __init__(self, transactions, previous_hash):
		"""
		Parameters
		----------
		transactions : dict
			A dictionary containing the information relative
			to a transaction that will be saved in the block.
		previous_hash : str
			The hash of the previous block.
		"""
		
		# The block's timestamp		
		self.time_stamp = datetime.datetime.now()
		# The transactions contained in the block
		self.transactions = transactions
		# The hash of the previous block
		self.previous_hash = previous_hash
		# The nonce (number used only once)
		self.nonce = 0
		# After setting the other properties, generate\
		# the block's hash
		self.hash = self.generate_hash()

	def generate_hash(self):
		"""
		Generates the hash for a block.
		
		Returns
		-------
		block_hash.hexdigest() : str
			The (hex) digest of the block's hash.
		"""

		# Create a single string for the contents of the\
		# block
		block_header = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
		# Hash the block's contents
		block_hash = sha256(block_header.encode())

		# Return a (hex) digest of the hash
		return block_hash.hexdigest()

	def print_contents(self):
		"""
		Print all the contents (attributes) of the block.

		Parameters
		----------
		None

		Returns
		-------
		None
		"""

		# Print each property of the block, individually
		print("Timestamp:", self.time_stamp)
		print("Transactions:", self.transactions)
		print("Current hash:", self.generate_hash())
		print("Previous hash:", self.previous_hash) 


class Blockchain:
	"""
	Creates a blockchain from scratch.

	Attributes
	----------
	chain : list
		A list containing all the blocks of the blockchain.
	unconfirmed_transactions : list
		A list containing all the unconfirmed transactions.

	Methods
	-------
	genesis_block()
		Creates the genesis block, that is, the first block
		of the blockchain.
	add_block(transactions)
		Appends a new block to the blockchain.
	print_blocks()
		Prints each propety of a block, individually, for
		all the blocks in the blockchain.
	validate_chain()
		Validates the blockchain, that is, validates that
		no block has been tampered with.
	proof_of_work(block, difficulty=2)
		Creates the Proof-of-Work for a given block, using
		a given difficulty.
	"""

	def __init__(self):
		"""
		Creates a new blockchain. The constructor calls the necessary
		method to create the genesis block, that is, when a new
		blockchain is created, its genesis block is created as well.

		Parameters
		----------
		None
		"""
		
		# The list containing all blocks
		self.chain = []
		# List to contain unconfirmed transactions
		self.unconfirmed_transactions = []
		# Create the genesis block, that is, the first block
		self.genesis_block()

	def genesis_block(self):
		"""
		Creates the genesis block of the blockchain, that is,
		the first block.

		Parameters
		----------
		None

		Returns
		-------
		None
		"""

		# List to hold the transactions of the genesis block (empty list)
		transactions = []
		# The genesis block contents will be empty and since\
		# it doesn't have a previous block, the previous hash\
		# value will be 0 (zero)
		genesis_block = Block(transactions, "0")
		# Generate the genesis block hash
		genesis_block.generate_hash()
		# Append the genesis block to the list of blocks
		self.chain.append(genesis_block)

	def add_block(self, transactions):
		"""
		Creates and appends a new block to the blockchain.

		Parameters
		----------
		transactions : dict
			A dictionary containing the information relative
			to a transaction that will be saved in the block.
		"""

		# Get the hash of the previous block (since we are appending a\
		# block to the chain, what we want is the hash of the last block\
		# (last element in the list))
		previous_hash = self.chain[-1].hash
		# To create the new block, use the list of transactions passed\
		# to this method call and use the hash of the last block in\
		# the chain as the previous hash value for the new block
		new_block = Block(transactions, previous_hash)
		# Generate the hash for this newly-created block
		new_block.generate_hash()
		# proof = proof_of_work(block)
		# Append the new block to the chain
		self.chain.append(new_block)

	def print_blocks(self):
		"""
		Prints each property of a block, for each block in the
		blockchain.

		Parameters
		----------
		None

		Returns
		-------
		None
		"""

		# Loop through the blocks in the chain (list) and print their\
		# information
		for i in range(len(self.chain)):
			current_block = self.chain[i]
			print(f"Block {i} {current_block}")
			# This method print each property of the block
			current_block.print_contents()
			print()

	def validate_chain(self):
		"""
		Validates the blockchain, that is, validates that no
		block has been tampered with.
		Loop through the chain and hash each block and its previous
		block's. If one of these is not equal to the hashes saved in
		those blocks, then the blockchain has been tampered with.
		Otherwise, if we reach the end of the chain without finding
		any incorrect hashes, it means the chain is validated.

		Parameters
		----------
		None

		Returns
		-------
		bool
			False if the blockchain has been tampered with; else True.
		"""

		# Loop through the chain of blocks (start at the second block, that\
		# is, ignore the genesis block since it doesn't have a previous block)
		for i in range(1, len(self.chain)):
			# The current block we're examining
			current = self.chain[i]
			# The block previous to the current block
			previous = self.chain[i-1]

			# If we hash the current block and the result does not\
			# match the hash saved in it, it means the chain is not\
			# validated
			if current.hash != current.generate_hash():
				print("Found a mismatch with the current block's hash")
				return False

			# If we hash the previous block and the result does not\
			# match the saved hash, it means the chain is not validated
			if current.previous_hash != previous.generate_hash():
				print("Found a mismatch with the previous block's hash")
				return False

		# If the method ran up to this point, it means we didn't find\
		# any block that has been tampered with. Thus, return True,\
		# that is, the chain is validated
		return True


	def proof_of_work(self, block, difficulty=2):
		"""
		Create the Proof-of-Work for a given block, with a given
		difficulty.

		Parameters
		----------
		block : __main__.Block
			A Block object, that is, a block of the blockchain.
		difficulty : int
			The number of trailing zeros required for the Proof-
			-of-Work.
		"""

		# Generate the hash for the passed block to use as proof\
		# (this is considered the first attempt at producing the\
		# proof-of-work)
		proof = block.generate_hash()
		# The number of trailing zeros we are aiming for is equal\
		# to the difficulty argument
		trailing_zeros = ''.join(['O' for i in range(difficulty)])

		# Loop while the proof doesn't have enough trailing zeros
		while proof[:2] != trailing_zeros:
			# Increment the nonce
			block.nonce += 1
			# With the nonce incremented, try generating the block's\
			# hash one more time
			proof = block.generate_hash()

		# After producing the proof-of-work, reset the nonce attribute
		block.nonce = 0

		# Finally, return the proof-of-work
		return proof 


if __name__ == "__main__":

	# Create some transactions
	block_one_transactions = {
		"sender": "Alice",
		"receiver": "Bob",
		"amount": "50"
	}
	block_two_transactions = {
		"sender": "Bob",
		"receiver": "Cole",
		"amount": "25"
	}
	block_three_transactions = {
		"sender": "Alice",
		"receiver": "Cole",
		"amount": "35"
	}
	# This one will be used to modify a block of the chain
	fake_transactions = {
		"sender": "Bob",
		"receiver": "Cole, Alice",
		"amount": "25"
	}

	# Create a new Blockchain
	local_blockchain = Blockchain()
	# Print the currently existing blocks in the blockchain
	print('Blockchain contents')
	local_blockchain.print_blocks()
	print()
	print()

	# Create a block for each transaction (dictionary) and add those\
	# blocks to the blockchain
	local_blockchain.add_block(block_one_transactions)
	local_blockchain.add_block(block_two_transactions)
	local_blockchain.add_block(block_three_transactions)
	
	# Print the currently existing blocks in the blockchain
	print('Blockchain contents')
	local_blockchain.print_blocks()
	print()

	# Tamper with a block by changing its transactions
	local_blockchain.chain[2].transactions = fake_transactions
	# Now try to validate the blockchain
	print('Is the blockchain valid?', local_blockchain.validate_chain())