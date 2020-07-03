
from SymbolType import *
class Expr:

        def lookupSymbolType(self, id) :

            self._type = self.parser.symbolType_table[id]
            
            if (self._type == None):
                self.parser.pSemError("Variable \""+id+"\" not declared")
                return SymbolType(-1, -1)
            
            return _type
        
        def __init__(self, parser, value, _type):
            self.parser = parser
            self.value = value
            self._type = _type


        #constructor with value and type
        @classmethod
        def valTypeConstr( cls, parser, value, _type):

            return cls(parser, value, _type)
        
        # constructor with id
        @classmethod
        def idConstr(cls, parser, p, indId):
            id = p[indId]
            _value = id
            _type = parser.lookupSymbolType(p, indId)

            return cls(parser, _value, _type)
        
        # constructor with id and pos
        @classmethod
        def idPosConstr(cls, parser, p, indId, indPos):
            _pos = str(p[indPos])
            id = p[indId]
            _value = id+"[" + _pos + "]" 
            _type = parser.lookupSymbolType(p, indId)

            pos = ''

            if _pos.isnumeric():
                pos = int(p[indPos])
                dim = int(_type.getDim())
                if (pos >= dim & dim != -1):
                    parser.pSemError("Array index ("+pos+") exceed array size ("+dim+")")
            
            return cls(parser, _value, _type)
                

        def toString(self):

            return self.value
        

        def getSymbolType(self):
            return self._type
        

        # Check symbol type. In return unknown type in the case of type error

        def checkSymbolType(self, p, ind):

            expr = p[ind]
            type1 = self._type.getType()
            type2 = expr.getSymbolType().getType()

            if (type1==type2) :
                return self._type
            
            elif (type1!=-1 & type2!=-1) :

                # If operands are of two different types cast them to double 

                self.parser.pSemWarning("Operation between int and double, int number casted to double", p, ind)
                return SymbolType(1, 1)

            else :
                return SymbolType(-1, -1)
            
    
        def checkSymbolTypeAssignment(self, p, ind):
            expr = p[ind]
            type1 = self._type.getType()
            type2 = expr.getSymbolType().getType()
        
            '''
            if (type1==0 & type2==1):
                self.parser.pSemWarning("Assignment of a double value to an int variable", p)
            
            elif (type1==1 & type2==0):
                self.parser.pSemWarning("Assignment of an int value to an double variable", p)
            '''
           