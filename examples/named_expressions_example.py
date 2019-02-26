# https://www.python.org/dev/peps/pep-0572/
# Example of a practical application for named expressions (using the new walrus
# operator).

sample_data = [
	{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
	{"userId": 1, "id": 2, "title": "quis ut nam facilis", "completed": False},
	{"userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": False},
	{"userId": 1, "id": 4, "title": "et porro tempora", "completed": True},
	{"userId": 1, "id": 4, "title": None, "completed": True},
]

print("With Python 3.8 named expressions:")
# Loop through the items (which are dictionaries) of the `sample_data` list
for entry in sample_data: 
	# Now, when calling the `get()` method on the item (dictionary) to find\
	# the value of the `title` key, save the returned result in the named\
	# expression `title`. This assignment is done with the walrus operator\
	# (:=) and so we can use the result of the expression directly as a\
	# conditional clause
	if title := entry.get("title"):
		print(f'Found title: "{title}"')


print("Pre-Python 3.8:")
# Loop through the items (which are dictionaries) of the `sample_data` list
for entry in sample_data:
	# Instead of using a named expression, we save the return value of the\
	# method in a variable
	title = entry.get("title")
	if title:
		print(f'Found title: "{title}"')