#unittest official documents example
#https://docs.python.org/3/library/unittest.html#basic-example

import unittest

#@unittest.skip("showing class skipping") <= classes can be skipped too
class MyTestCase(unittest.TestCase):
    
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        '''A test function that is skipped during testing.'''
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        '''A function that is not tested for certain versions of a library.'''
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


#Output when running these tests in verbose mode (-v)
'''
test_format (__main__.MyTestCase) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase) ... skipped 'demonstrating skipping'
test_windows_support (__main__.MyTestCase) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK (skipped=3)
'''

#It’s easy to roll your own skipping decorators by making a decorator that calls skip()\
#on the test when it wants it to be skipped.
def skipUnlessHasattr(obj, attr):
    '''This decorator skips the test unless the passed object has 
    a certain attribute.'''
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))