# Class to create queues
class Queue ():
	def __init__ (self):
		self.items = []

	def is_empty (self):
		return self.items == []

	def enqueue (self, item):
		self.items.append(item)

	def dequeue (self):
		return self.items.pop(0)

	def size (self):
		return len(self.items)


def get_week_day (num, first_week_day):
	'''
	Find what day of the week a certain day is, given what is the first day
	of the week for that month.

	Parameters
	----------
	num : int
		The day of the month whose week day we want to find out.
	first_week_day : int
		The day of the week of the first day of that month (1-7, with Sunday
		being 1 and Saturday 7).

	Returns
	-------
	string
		The day of the week for the wanted day (`num`).
	'''
	
	# List with all the days of the week, ordered
	days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	# Create a queue to hold a full week (the first item will be the first day of the week\
	# of the month and the last item will be the last day of that week)
	days_queue = Queue()
	# List to hold the days of the week ordered according to the first day of the week\
	# of this situation
	ordered_days = []
	# Variable to keep track of which day we are looking at
	day = 1

	# Find out the order of the days of the week for the weeks of this month
	for i in days[first_week_day-1:]:
		ordered_days.append(i)
	for i in days[:first_week_day-1]:
		ordered_days.append(i)

	# Fill the queue with the first week of the desired month (use the `ordered_days` list\
	# to fill the queue)
	for i in ordered_days:
		days_queue.enqueue(i)

	# Each day, remove the front day of the week from the queue. If today is not the desired\
	# day, put the day of the week at the end of the queue and advance the day (`day+=1`)
	while day <= num:
		# Remove the front item of the queue
		week_day = days_queue.dequeue()

		# If we are finally at the desired day, return its day of the week
		if day == num:
			return week_day
		# Otherwise just increment the `day` variable so we can look at the next day\
		# and put today's day of the week at the end of the queue
		else:
			day += 1
			days_queue.enqueue(week_day)


if __name__ == "__main__":
	print(get_week_day(4, 6)) # Feb. 2nd 2019
	print(get_week_day(9, 6)) # Mar. 9th 2019
	print(get_week_day(13, 1)) # Dec. 13th 2019