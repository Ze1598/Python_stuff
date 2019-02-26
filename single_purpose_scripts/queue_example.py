'''
	A queue is an ordered list of items where the insertion of new
items happens at the end (the rear) and the removal occurs at the
beginning (the front).
	Thus, the first item to be removed is the first one, that is, the 
one that has been in the queue the longest. The last to be removed is
the last in the queue, the one that has been there the shortest.
'''

# As such, we can use Python's built-in `list`s to create a Queue class.
# We'll use the beginning of the list as the Queue's front and the\
# end of the list as the Queue's rear
class Queue ():

	# A new queue starts empty (an empty list)
	def __init__ (self):
		self.items = []

	def is_empty (self):
		'''
		Method to check if the queue is empty.

		Parameters
		----------
		None

		Returns
		-------
		bool
			True if the queue is empty; else False.
		'''

		return self.items == []

	def enqueue (self, item):
		'''
		Method to add a new item to the rear of the queue (the end of the list).

		Parameters
		----------
		item
			The item to be added to the rear of the queue (end of the list).

		Returns
		-------
		None

		'''
		self.items.append(item)

	def dequeue (self):
		'''
		Remove and return the front (first) item of the queue (first item of the list).

		Parameters
		----------
		None

		Returns
		-------
			The front item of the queue (the first item of the list).
		'''

		return self.items.pop(0)

	def size (self):
		'''
		Get the size of the queue (the length of the list).

		Parameters
		----------
		None

		Returns
		-------
		int
			The size of the queue (list).
		'''

		return len(self.items)


if __name__ == "__main__":
	my_queue = Queue()
	print("`my_queue` was created")
	print("Is the queue empty:", my_queue.is_empty())

	print("Three items are going to be queued")
	my_queue.enqueue(15)
	my_queue.enqueue("Hello")
	my_queue.enqueue(9.2)
	print("Size of the queue:", my_queue.size())
	
	print("The front item of the queue was removed:", my_queue.dequeue())
	print("Size of the queue:", my_queue.size())
	print("Another item dequeued:", my_queue.dequeue())
	print("Another item dequeued:", my_queue.dequeue())
	print("Size of the queue:", my_queue.size())