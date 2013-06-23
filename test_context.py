
import unittest

from context import Context

class ContextTests(unittest.TestCase):
    def test_set_and_get_value(self):
        context = Context()
        context.set('foo', 'bar')
        self.assertEqual('bar', context.get('foo'))
    
if __name__ == '__main__':
    unittest.main()
    