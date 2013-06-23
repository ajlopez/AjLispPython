
import unittest

from list import List
from context import Context
from symbol import Symbol

class ListEvaluateTests(unittest.TestCase):
    def test_evaluate_define(self):
        context = Context()
        context.set('define', DefinePrimitive())
        list = List(Symbol('define'), List('one', List(1, None)))
        self.assertEqual(1, list.evaluate(context))
        self.assertEqual(1, context.get('one'))
        
class DefinePrimitive:
    def apply(self, context, args):
        name = args.head()
        value = args.tail().head()
        context.set(name, value)
        return value
        
if __name__ == '__main__':
    unittest.main()
    