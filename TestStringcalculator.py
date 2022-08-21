import unittest

import String_Calculator

class TestStringcalculator(unittest.TestCase):
    def test_empty_string(self):
        '''It should return 0 if the string is empty'''
        self.assertEqual(String_Calculator.add("1"),0)