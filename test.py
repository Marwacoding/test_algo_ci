import unittest
from palindrome import palindrome

class TestStringMethods(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome('ressasser'), 'ressasser')
    

    def test_number_of_word(self):
        


if __name__ == '__main__':
    unittest.main(verbosity=2)