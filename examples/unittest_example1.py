#unittest official documents example
#https://docs.python.org/3/library/unittest.html#basic-example

import unittest

class TestStringMethods(unittest.TestCase):
    '''A customised test class that starts by inheriting from the
    unittest.TestCase class. The test methods' (three in this case)
    names must always start with "test" so that the test runner
    knows which methods represent tests.
    Instead of using the 'assert' statement, assertSomething functions
    are used so the test runner can accumulate the results and produce
    a report at the end.'''

    def test_upper(self):
        '''assertEqual() checks for an expected result.'''
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        '''assertTrue() and assertFalse() assert that a given value
        returns True or False, respectively.'''
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        '''assertRaises() verifies that a specific exception 
        is raised.'''
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #Check that s.split() fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    #Execute all the tests and provides command-line interface to the test-script
    unittest.main()


#When run from the command line, the tests' output looks like this
'''
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
'''


#However, if the '-v' option is used when running the script from the command
#line, you'll obtain a more detailed output (in this case since I've written
#included docstrings, those appear in the output too)
#python unittest_example1.py -v
'''
test_isupper (__main__.TestStringMethods)
assertTrue() and assertFalse() assert that a given value ... ok
test_split (__main__.TestStringMethods)
assertRaises() verifies that a specific exception ... ok
test_upper (__main__.TestStringMethods)
assertEqual() checks for an expected result. ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
'''