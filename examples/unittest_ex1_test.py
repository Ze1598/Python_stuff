import unittest
import os
os.chdir("C:\\Users\\ze179\\Desktop\\temporary\\code\\Python\\")
from unittest_ex1_source import is_anagram
 
class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(  is_anagram("abc", "acb") )
        self.assertTrue(  is_anagram("silent", "listen") )
        self.assertFalse( is_anagram("one", "two") )
 
if __name__ == '__main__':
    unittest.main()