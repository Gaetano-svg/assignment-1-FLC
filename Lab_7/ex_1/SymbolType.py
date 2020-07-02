
class SymbolType:

    # CONSTRUCTOR
    def __init__(self, _type, dim):
        print("Symbol Type constructor called")
        self._type = _type
        self.dim = dim
    # DESTRUCTOR
    def __del__(self):
        print('Symbol Type destructor called.')

    def getType(self):

        return self._type
    
    def getDim(self):

        return self.dim