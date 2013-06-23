
import unittest

import ajlisp

class EvaluateTests(unittest.TestCase):
    def test_evaluate_integer(self):
        self.assertEqual(3, ajlisp.evaluate(3))
        
    def test_evaluate_string(self):
        self.assertEqual("spam", ajlisp.evaluate("spam"))
        
    def test_evaluate_symbol_in_context(self):
        context = ajlisp.Context()
        symbol = ajlisp.Symbol('one')
        context.set('one', 1)
        self.assertEqual(1, ajlisp.evaluate(symbol, context))
        
if __name__ == '__main__':
    unittest.main()