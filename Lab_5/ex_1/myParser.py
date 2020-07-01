from myLexer import *
import ply.yacc as yacc
import sys


class MyParser:

    # CONSTRUCTOR
    def __init__(self,lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        # static variables initialization
        self.fact_found = 0
        self.error_found = 0
        self.symbol_table = {}

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    def isFloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    
    tokens = MyLexer.tokens

    # Ensure our parser understands the correct order of operations.
    # The precedence variable is a special Ply variable.

    precedence = (

        ('left', 'MINUS', 'PLUS'),
        ('left', 'DIV', 'PROD', 'PT'),
        ('left', 'EXP'),
        ('left', 'UMINUS'),

    )

    # GRAMMAR START

    def p_sessione(self,p):
        '''
        sessione : expr_list QP
        '''
    
    def p_expr_list(self,p):
        '''
        expr_list : expr_list PV expr
                    | expr
        '''

    def p_expr(self,p):
        '''
        expr : scalar_assign 
                    | vector_assign 
                    | vect_expr_ 
                    | scalar_expr_
        '''

    def p_vect_expr_(self,p):
        '''
        vect_expr_ : vect_expr
        '''

        p[0] = p[1]

        print("vector expression: ", end="")
        print( p[0] )        

    def p_scalar_expr_(self,p):
        '''
        scalar_expr_ : scalar_expr
        '''

        p[0] = p[1]

        print("scalar expression: ", end="")
        print( p[0] )

    # VECTOR EXPRESSIONS
    def p_vect_scal_expr (self,p):
        '''
        vect_scal_expr : scalar_expr PROD vect_expr 
                            | scalar_expr DIV vect_expr
        '''

        if p[2] == '*':
            p[0] = [0,0] #declare as array
            p[0][0] = p[1] * p[3][0]
            p[0][1] = p[1] * p[3][1]
                
        elif p[2] == '/':
            p[0] = [0,0] #declare as array
            p[0][0] = p[1] / p[3][0]
            p[0][1] = p[1] / p[3][1]    

    def p_vect_expr(self,p):
        '''
        vect_expr : vect_expr PLUS vect_expr
                    | vect_expr MINUS vect_expr 
                    | vect_scal_expr
                    | vect_expr PROD scalar_expr 
                    | vect_expr DIV scalar_expr 
                    | LBR vect_expr RBR
                    | vector
        '''

        if( len(p) == 4 ):
            
            if p[2] == '+':
                p[0] = [ p[1][0] + p[3][0] , p[1][1] + p[3][1] ] #declare as array

            elif p[2] == '-':
                p[0] = [ p[1][0] - p[3][0] , p[1][1] - p[3][1] ] #declare as array
    
            elif p[2] == '*':
                p[0] = [ p[1][0] * p[3] , p[1][1] * p[3] ] #declare as array
                
            elif p[2] == '/':
                p[0] = [ p[1][0] / p[3] , p[1][1] / p[3] ] #declare as array
            
            elif p[1] == '(':
                p[0] = p[2]

        else :
            p[0] = p[1]
            
    # SCALAR EXPRESSION
    def p_scalar_expr (self,p):
        '''
        scalar_expr : scalar_expr PLUS scalar_expr 
                        | scalar_expr MINUS scalar_expr
                        | scalar_expr PROD scalar_expr
                        | scalar_expr DIV scalar_expr
                        | MINUS scalar_expr %prec UMINUS
                        | scalar_expr EXP scalar_expr 
                        | LBR scalar_expr RBR
                        | vect_expr PT vect_expr
                        | scalar
        '''

        if( len(p) == 4 ):
            
            if p[2] == '+':
                p[0] = float(p[1] + p[3])
            
            elif p[2] == '-':
                p[0] = float(p[1] - p[3])
            
            elif p[2] == '*':
                p[0] = float(p[1] * p[3])
            
            elif p[2] == '/':
                p[0] = float(p[1] / p[3])
                        
            elif p[2] == '^':
                p[0] = pow(p[1],[3])
            
            elif p[2] == '.':
                p[0] = float((p[1][0] * p[3][0]) + (p[1][1] * p[3][1]))
            
            elif p[1] == '(':
                p[0] = p[1]
        
        elif ( len(p) == 3):
            p[0] = 0 - p[2]

        elif( len(p) == 2 ):
            p[0] = p[1]

    # ASSIGNMENTS
    def p_scalar_assign(self, p):
        '''
        scalar_assign : SCALAR_VAR EQUALS scalar_expr
        '''

        self.symbol_table[p[1]] = p[3]
        print("assignment: " + p[1] + " -> ", end="")
        print(p[3])

    def p_vector_assign (self, p):
        '''
        vector_assign : VECTOR_VAR EQUALS vect_expr
        '''

        self.symbol_table[p[1]] = p[3]
        print("assignment: " + p[1] + " -> [", end="")
        print(p[3][0], end="")
        print(",", end="")
        print(p[3][1], end="")
        print("]")

    def p_scalar (self,p):
        '''
        scalar : CONST
                | SCALAR_VAR
        '''

        if (self.isFloat(p[1])):
            p[0] = float(p[1])

        else:
            p[0] = self.symbol_table[p[1]]
        
    def p_vector (self,p):
        '''
        vector : VECTOR_VAR
                | LBS scalar_expr CM scalar_expr RBS
        '''

        if(p[1] == '['):
            p[0] = [p[2],p[4]]
        
        else :
            p[0] = self.symbol_table[p[1]]

    def p_error(self,p):
        '''
        '''

