
import unittest

from list import List

class ListTests(unittest.TestCase):
    def test_create_list(self):
        list = List(1, None)
        self.assertEqual(1, list.head())
        self.assertIsNone(list.tail())
        
    def test_create_list_with_two_elements(self):
        list = List(1, List(2, None))
        self.assertEqual(1, list.head())
        self.assertIsNotNone(list.tail())
        tail = list.tail()
        self.assertEqual(2, tail.head())
        self.assertIsNone(tail.tail())
        
if __name__ == '__main__':
    unittest.main()
    