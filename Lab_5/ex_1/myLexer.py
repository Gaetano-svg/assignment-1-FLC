import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN

class MyLexer:

    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    # list of TOKENS
    tokens = [

        'ws', 'nl',
        'CONST',
        'VECTOR_VAR', 'SCALAR_VAR', 'EQUALS', 'PV', 'PT', 'CM', 'EXP', 'QP',
        'RBS', 'LBS', 'RBR', 'LBR', 'PROD', 'DIV', 'MINUS', 'PLUS'

    ]

    t_ignore = r' '
    
    t_ws = r'([ \t])'
 
    def t_nl(self,t):
        r'(\r|\n|\r\n)'
        pass

    def t_CONST(self,t):
        r'(\-)?[0-9]+(\.[0-9]+((e|E)(\+|\-)?[0-9]+)?)?'
        return t

    def t_VECTOR_VAR(self, t):
        r'[A-Z]'
        return t

    def t_SCALAR_VAR(self, t):
        r'[a-z]'
        return t

    def t_EQUALS(self, t):
        r'\='
        return t

    def t_PV(self, t):
        r'\;'
        return t
    
    def t_PT(self, t):
        r'\.'
        return t

    def t_CM(self, t):
        r'\,'
        return t

    def t_EXP(self, t):
        r'\^'
        return t

    def t_QP(self, t):
        r'\?'
        return t

    def t_RBS(self, t):
        r'\]'
        return t
    
    def t_LBS(self,t):
        r'\['
        return t

    def t_RBR(self, t): 
        r'\)'
        return t

    def t_LBR(self, t):
        r'\('
        return t
    
    def t_PROD(self,t):
        r'\*'
        return t
    
    def t_DIV(self,t):
        r'\/'
        return t
    
    def t_MINUS(self,t):
        r'\-'
        return t
    
    def t_PLUS(self,t):
        r'\+'
        return t
    
    def t_eof(self,t):
        print("EOF reached")
        t.lexer.skip(1)

    def t_error(self,t):
        r'.'
        print("ERROR (Character not recognized): ", t.value)
        return t
