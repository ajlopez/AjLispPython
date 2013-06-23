
import unittest

import ajlisp

class EvaluateTests(unittest.TestCase):
    def test_evaluate_integer(self):
        self.assertEqual(3, ajlisp.evaluate(3))
        
    def test_evaluate_string(self):
        self.assertEqual("spam", ajlisp.evaluate("spam"))
        
if __name__ == '__main__':
    unittest.main()