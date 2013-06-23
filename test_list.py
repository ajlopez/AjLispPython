
import unittest

from list import List

class ListTests(unittest.TestCase):
    def test_create_list(self):
        list = List(1, None)
        self.assertEqual(1, list.head())
        self.assertEqual(None, list.tail())
        
if __name__ == '__main__':
    unittest.main()