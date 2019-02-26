# When executing this script from the command line, the user can pass\
# an integer as a positional argument, an integer whose square\
# will be output. 
# The user also has the possibility of passing an optional argument,\
# which will make the script prompt the user for a second integer; if\
# this optional argument is missing, then the script simply outputs the\
# square of the positional argument.
# There's still a second positional argument which sets the output's\
# verbosity

import argparse

# Create the main object to handle command line arguments
# -----------------------------------------------------------------------------

# The object to hold all the necessary information to parse the\
# command line commands into Python data types
'''
It accepts the following parameters:
	prog: The name of the program (defaults to sys.argv[0], a.k.a.
the first command line argument)
	usage: The string describing the program usage (by default it
is generated from the arguments added to parser)
	description: Text to display before the `help`argument (defaults
to None)
'''
parser = argparse.ArgumentParser(description="Calculate the square of a given integer in the range 0-9, inclusive.")

# -----------------------------------------------------------------------------


# Create positional and optional arguments
# -----------------------------------------------------------------------------

'''
ArgumentParser.add_argument(name or flags, action, nargs, const, default,
type, choices, required, help, metavar, dest)
	name or flags: Either a name or a list of option strings: e.g. `foo` or
`-f`, `--foo`.
	action: What to do when this argument is encountered at the command
line. It accepts the following values: `store` (default), `store_const` (the
value specified with the `const` kwarg), `store_true` or `store_false` (saves
a Boolean value), `append`(saves values in a list; useful for arguments that
are called multiple times), `append_const`(append the `const` value of arguments
to the same list), and `count` (counts the number of times a kwarg occurs).
	nargs: The number of command-line arguments that should be consumed
(accepts integers, wildcards (?, + and *) argparse.REMAINDER (takes a list of
the remainder passed arguments)).
	const: A constant value required by some action and nargs selections.
	default: The value produced if the argument is absent from the command line.
	type: The type to which the command line argument should be converted.
	choices: A container of the allowable values for the argument.
	required: Whether or not the command-line option may be omitted (optionals only).
	help: A brief description of what the argument does.
	metavar: A name for the argument in usage messages.
	dest: The name of the attribute to be added to the object returned by .parse_args().
'''

# Add a positional argument `to_square` which is converted to an integer.\
# In this case, we are restricting the user input to integers between 0 and\
# 10, exclusive. If the input is outside this range, the program outputs\
# the valid input values
parser.add_argument(
	"to_square",
	help="the integer whose square will be displayed",
	type=int,
	choices=list(range(10))
)

# Add an optional argument which, if present is saved with a value of True (if\
# it's not present it's saved with a value of None)
# It's intended to use this argument as a flag that the user wants to input a\
# second argument
parser.add_argument(
	"-s",
	"--second",
	help="a flag to prompt the user for a second integer to square",
	action="store_true"
)
# Add another optional argument, this time one that will be responsible for setting\
# the output's verbosity. In this case, we use `count` as the argument's `action`\
# so that the user can set it by repeating the argument (`-v` for 1, `-vv` for 2\
# and omitting defaults to a value of 0)
# Note: setting a default value of 0 is important, if it isn't explicit then it would\
# default to `None`, which isn't an int and thus can't be used for comparisons
parser.add_argument(
	"-v",
	"--verbosity",
	help="set output verbosity",
	action="count",
	default=0
)

# -----------------------------------------------------------------------------

# Set the argument parser (what is responsible for converting the arguments into\
# Python data types)
# -----------------------------------------------------------------------------

'''
ArgumentParser.parse_args(args=None, namespace=None)
	args: list of strings to parse; by default, it uses the
arguments taken from sys.argv (i.e., the command line arguments
passed to a Python script).
	namespace: an object to hold the arguments parsed; defaults
to creating a new empty Namespace object.
'''
'''
	This method is typically called with no arguments, and it's
used for the ArgumentParser object to parse arguments from the
command line (which includes converting said arguments into Python
data types).
	In the backgroud, .parse_args() creates a new Namespace object,
exclusive for these arguments. The method returns this Namespace,
but populated with the arguments already converted into Python
data types.
	Calling this method without specifying any positional or
optional arguments results in creating a single optional argument:
help (-h or --help).
'''
args = parser.parse_args()

# -----------------------------------------------------------------------------

# General code to handle the output for this file
# -----------------------------------------------------------------------------

def print_square(num, verb):
	'''
	Function to print the square of input numbers, dependant on
	the verbosity defined.

	Parameters
	----------
	num : int
		The integer to be squared.
	verb : int
		The level of output verbosity.

	Retuns
	------
	None
	'''

	# If the user set verbosity to 2 or more, then output the\
	# most verbose output
	if verb >= 2:
		print("The square of your number is:", num ** 2)
	# If the user set verbosity to 1, then output the\
	# intermediately verbose output
	elif verb == 1:
		print(f"{num} ** 2 = {num ** 2}")
	# If the user set verbosity to 0 or didn't set it at all\
	# (which defaults to 0), then just output the square
	else:
		print(num ** 2)
	
	return None

# Print the square of the integer passed as a positional argument
print_square(args.to_square, args.verbosity)

# If the user included the optional argument `--s` or `--second`,\
# then prompt for a second number and print its square
if args.second:
	# Prompt the user for an integer
	second_num = int(input("What's the second number: "))
	# Then print the square of that integer
	print_square(second_num, args.verbosity)

# -----------------------------------------------------------------------------


# Extra
# -----------------------------------------------------------------------------

# ArgumentParser.add_argument_group(title=None, description=None)
'''
Create a group of arguments (instead of arguments being separated by default\
into positional and optional groups)
	title: the group's title.
	description: the group's description.
Arguments not covered by any of the developer-defined groups will still end\
up in the original positional or optional groups.
'''
'''
group = parser.add_argument_group('group_title')
group.add_argument('x')
group.add_argument('y')
args = parser.parse_args()
'''

# -----------------------------------------------------------------------------