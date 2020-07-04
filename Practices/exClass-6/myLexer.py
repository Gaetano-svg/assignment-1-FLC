import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN

class MyLexer():


    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    # list of TOKENS
    tokens = [

        'ARROW', 'MINUS', 'PLUS', 'DIV', 'STAR', 'OB', 'CB',
        'SC', 'C', 'D', 'DD', 'EQ', 'NUMBER', 'WORD', 'ID'

    ]

    t_ignore = r' '
    
    # tokens DEFINITION
    def t_nl(self,t):
        r'(\r|\n|\r\n)|\s|\t'
        pass

    def t_comm(self,t):
        r'\/\/.*'
        pass

    def t_ARROW(self,t):
        r'\-\>'
        return t

    def t_PLUS(self,t):
        r'\+'
        return t

    def t_MINUS(self,t):
        r'\-'
        return t

    def t_STAR(self,t):
        r'\*'
        return t

    def t_DIV(self,t):
        r'\/'
        return t

    def t_OB(self, t):
        r'\('
        return t
    
    def t_CB(self,t):
        r'\)'
        return t
    
    def t_SC(self,t):
        r'\;'
        return t

    def t_C(self,t):
        r'\,'
        return t

    def t_D(self,t):
        r'\.'
        return t

    def t_DD(self,t):
        r'\:'
        return t

    def t_EQ(self,t):
        r'\='
        return t

    def t_comment(self,t):
        r'\/\/.*'
        pass
            
    def t_NUMBER(self,t):
        r'[0-9]+'
        return t
        
    def t_WORD(self,t):
        r'[a-zA-Z]+'
        return t
    
    def t_ID(self,t):
        r'[_a-zA-Z][_a-zA-Z0-9]*'
        return t

    def t_error(self,t):
        r'.'
        print("ERROR (Character not recognized): ", t.value)
        return t
