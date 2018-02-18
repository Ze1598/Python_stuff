import unittest

#The function to be tested
def is_anagram(word1, word2):
    '''Tests if a pair of words is an anagram.'''
    return sorted(word1) == sorted(word2)

#Start by inheriting from the unittest.TestCase class
class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        '''A couple of tests to make sure the function is
        returns the expected values.'''
        self.assertTrue(is_anagram("abc", "acb"))
        self.assertTrue(is_anagram("silent", "listen"))
        self.assertFalse(is_anagram("one", "two"))
 
if __name__ == '__main__':
    #Execute all the tests and provides command-line interface to the test-script
    unittest.main()

#python unittest_example2.py
'''
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
'''

#python unittest_example2.py -v
'''
test_anagram (__main__.TestAnagram)
A couple of tests to make sure the function is ... ok

----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
'''