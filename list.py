
class List:
    def __init__(self, head, tail):
        self.__head = head
        self.__tail = tail
        
    def head(self):
        return self.__head
        
    def tail(self):
        return self.__tail

    def asString(self):
        result = "("
        result += listAsString(self)            
        result += ")"
        
        return result
        
def listAsString(list):
    head = list.head()
    
    if (hasattr(head, 'asString')):
        result = head.asString()
    else:
        result = str(head)
    
    if list.tail():
        result += " "
        result += listAsString(list.tail())
        
    return result