
import unittest
import specialforms

from context import Context
from list import List

class ListSpecialFormTests(unittest.TestCase):
    def test_evaluate_define(self):
        context = Context()
        list = List('one', List(1, None))
        define = specialforms.DefineForm()
        self.assertEqual(1, define.apply(context, list))
        self.assertEqual(1, context.get('one'))
        
if __name__ == '__main__':
    unittest.main()
    