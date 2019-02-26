import getpass
'''
getpass.getpass(prompt='Password: ', stream=None)
	Prompt the user for a password without echoing. 
	The user is prompted using the string provided with the `prompt`
	kwarg.
	If `prompt` is not provided, defaults to 'Password: '.
'''

def get_invisible_password():
	'''Prompts the user for a password, providing blind input for
	the user.

	Args:
		None

	Returns:
		None
	'''

	# Prompts the user for a password, allowing blind input
	user_pass = getpass.getpass(prompt="What is the password: ")

	# Prints the user input
	print("The password is:", user_pass)


get_invisible_password()