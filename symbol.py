
class Symbol:
    def __init__(self, name):
        self.__name = name
        
    def name(self):
        return self.__name
        
    def evaluate(self, context):
        return context.get(self.__name)