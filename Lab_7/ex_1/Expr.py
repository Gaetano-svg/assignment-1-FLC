
class Expr:

        def lookupSymbolType(self, id) :

            SymbolType _type = self.parser.symbolType_table[id]
            
            if (_type == None):
                self.parser.pSemError("Variable \""+id+"\" not declared")
                return SymbolType(-1, -1)
            
            return _type
        
        
        def __init__( self, parser, value, _type):
            self.parser = parser
            self.value = value
            self._type = _type
        

        def __init__(self, parser, id):
            self.parser = parser
            self.value = id
            self._type = self.lookupSymbolType(id)
        

        def __init__(self, parser, id, pos):
            self.parser = parser
            self.value = id+"[" + pos + "]" 
            self._type = self.lookupSymbolType(id)

            dim = self._type.getDim()
            if (pos >= dim & dim != -1):
                self.parser.pSemError("Array index ("+pos+") exceed array size ("+dim+")")
        '''
        def __init__(self, parser, id, pos):
            self.parser = parser
            self.value = id+"["+pos+"]"
            self._type = self.lookupSymbolType(id)
        '''
        

        def toString(self):

            return self.value
        

        def getSymbolType(self):
            return self._type
        

        # Check symbol type. In return unknown type in the case of type error

        def checkSymbolType(self, expr):

            type1 = self._type.getType()
            type2 = expr.getSymbolType().getType()

            if (type1==type2) :
                return self._type
            
            elif (type1!=-1 & type2!=-1) :

                # If operands are of two different types cast them to double 

                self.parser.pSemWarning("Operation between int and double, int number casted to double")
                return SymbolType(1, 1)

            else :
                return SymbolType(-1, -1)
            
    
        def checkSymbolTypeAssignment(self, expr):
            type1 = self._type.getType()
            type2 = expr.getSymbolType().getType()

            if (type1==0 & type2==1):
                self.parser.pSemWarning("Assignment of a double value to an int variable");
            
            elif (type1==1 & type2==0):
                self.parser.pSemWarning("Assignment of an int value to an double variable");
            
           