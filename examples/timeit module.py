import timeit


# One-line tests
# -------------------------------------------------------------------------------

# Create iterables that contain all the integers between zero and one million
# The respective command line call for each test is commented out 
# Each test is executed ten times

# Iterator
# python -m timeit -n 10 "(i for i in range(1000000))"
time1 = timeit.timeit(stmt="(i for i in range(1000000))", number=10)
print("Iterator:", round(time1, 4), "seconds")

# List
# python -m timeit -n 10 "[i for i in range(1000000)]"
time2 = timeit.timeit(stmt="[i for i in range(1000000)]", number=10)
print("List:", round(time2, 4), "seconds")

# Set
# python -m timeit -n 10 "{i for i in range(1000000)}"
time3 = timeit.timeit(stmt="{i for i in range(1000000)}", number=10)
print("Set:", round(time3, 4), "seconds")

# Tuple
# python -m timeit -n 10 "tuple( (i for i in range(1000000)) )"
time4 = timeit.timeit(stmt="tuple( (i for i in range(1000000)) )", number=10)
print("Tuple:", round(time4, 4), "seconds")

# Dictionary (str(integer): integer)
# python -m timeit -n 10 "{str(i):i for i in range(1000000)}"
time5 = timeit.timeit(stmt="{str(i):i for i in range(1000000)}", number=10)
print("Dictionary:", round(time5, 4), "seconds")

# -------------------------------------------------------------------------------


# Function call tests
# -------------------------------------------------------------------------------

# Create a sample function
def test_func(x):
	return [i for i in range(x)]

# Execute and time the function 10 times
# The function to be tested needs to be imported in the `timeit()` call
# python -m timeit -n 10 "def test_func(x):" "    return [i for i in range(x)]" "test_func(1000000)"
time6 = timeit.timeit(
	stmt="test_func(1000000)", 
	setup="from __main__ import test_func", 
	number=10
)
print("test_func(1000000):", round(time6, 4), "seconds")

# -------------------------------------------------------------------------------


# globals() test
# -------------------------------------------------------------------------------

def func_a (x):
	return x + 10.5
def func_b (x):
	return x - 10.5
def func_c (x):
	return x * 10.5


# Execute the following tests in the global scope (by passing `globals()` to the\
# `globals` kwarg)
# In this test we make the same function call to three different functions
# python -m timeit -n 10 "def func_a (x):" "    return x + 10.5" "def func_b (x):" "    return x - 10.5" "def func_c (x):" "    return x * 10.5" "[func(100) for func in (func_a, func_b, func_c)]"
time7 = timeit.timeit(
	stmt="[func(100) for func in (func_a, func_b, func_c)]",
	globals=globals(),
	number=10
)
print("[func(100) for func in (func_a, func_b, func_c)]:", round(time7, 4), "seconds")

# -------------------------------------------------------------------------------