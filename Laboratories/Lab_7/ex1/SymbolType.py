
class SymbolType:

    # CONSTRUCTOR
    def __init__(self, _type, dim):
        self._type = _type
        self.dim = dim

    def getType(self):

        return self._type
    
    def getDim(self):

        return self.dim