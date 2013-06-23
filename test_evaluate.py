
import unittest

import ajlisp

class EvaluateTests(unittest.TestCase):
    def test_evaluate_integer(self):
        self.assertEqual(3, ajlisp.evaluate(3))
        
if __name__ == '__main__':
    unittest.main()