
from list import List
from context import Context
from symbol import Symbol

def evaluate(arg, context = None):
    if isinstance(arg, Symbol):
        return arg.evaluate(context)
    return arg