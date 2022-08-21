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
        self.assertEqual(String_Calculator.add("1,2"),3)
    
    # Allow the add method to handle an unknown amount of numbers
    def test_multiple_string(self):
        '''It should retrun the sum of unknow amount of number'''
        self.assertEqual(String_Calculator.add("1,2,3"),6)
    
    '''Allow alphabets to be included with numbers.
    The numeric value for the alphabet would be equal to its position.
    Such as a = 1, b = 2, c = 3 … y = 25, z = 26.
    For example:
    Input: "1,2,a,c"
    Output: 7 (1 + 2 + 1 + 3)
    Note: Use lowercase alphabets only.'''
    def test_aplhanumberic(self):
        self.assertEqual(String_Calculator.add("a,b,c,1"),7)
    
    #Numbers bigger than 1000 should be ignored.
    def test_numberbiggerthan_1000(self):
        '''It should ignore number bigger than 1000'''
        self.assertEqual(String_Calculator.add("4,1001"),4)
    
    def test_negative_number_exception(self):
        '''It should raise an exception containing all negative number if any are found'''
        with self.assertRaises(Exception):
            String_Calculator.add('-1')
    def test_MultipleNegative_number_exception(self):
        '''It should raise an exception containing all negative number if any are found'''
        with self.assertRaises(Exception):
            String_Calculator.add("-1,-2,-3,1,2,3")
    def test_new_line_as_delimiter(self):
        '''It should be able to use new line as delimiter'''
        self.assertEqual(String_Calculator.add("1\n2,3"),5)
