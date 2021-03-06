
from collections import deque

class List:
    def __init__(self, head, tail):
        self.__head = head
        self.__tail = tail
        
    def make(*args):
        return makeList(deque(args))
        
    def head(self):
        return self.__head
        
    def tail(self):
        return self.__tail

    def asString(self):
        result = "("
        result += listAsString(self)            
        result += ")"
        
        return result
        
    def evaluate(self, context):
        form = self.__head.evaluate(context)
        return form.apply(context, self.__tail)
        
def listAsString(list):
    head = list.head()
    
    if isinstance(head, List):
        result = head.asString()
    else:
        if head == None:
            result = 'nil'
        else:
            result = str(head)
    
    if list.tail():
        result += " "
        result += listAsString(list.tail())
        
    return result
    
def makeList(queue):
    if len(queue):
        head = queue.popleft()
        return List(head, makeList(queue))
    
    return None
