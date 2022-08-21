import unittest

import String_Calculator

class TestStringcalculator(unittest.TestCase):
    def test_empty_string(self):
        '''It should return 0 if the string is empty'''
        self.assertEqual(String_Calculator.add(""),0)

    def test_single_string(self):
        '''It should return 1 if the string is 1'''
        self.assertEqual(String_Calculator.add("5"),5)
    
    def test_double_string(self):
        '''It should return the sum of given string like 1+2=3'''
        self.assertEqual(String_Calculator.add("1,2"),4)