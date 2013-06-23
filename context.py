
class Context:
    def __init__(self):
        self.__values = {}
        
    def set(self, name, value):
        self.__values[name] = value
        
    def get(self, name):
        return self.__values[name]
        