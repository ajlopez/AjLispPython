
import unittest

from symbol import Symbol
from context import Context

class SymbolTests(unittest.TestCase):
    def test_create_symbol(self):
        symbol = Symbol('a')
        self.assertEqual('a', symbol.name())
    
    def test_evaluate_undefined_symbol(self):
        context = Context()
        symbol = Symbol('a')
        self.assertIsNone(symbol.evaluate(context))
        
if __name__ == '__main__':
    unittest.main()
    