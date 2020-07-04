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
        
        'NUMBER', 'PLUS', 'MINUS',
        'OBRACKET', 'CBRACKET',
        'EQUAL', 'nl', 

    ]

    # tokens DEFINITION

    def t_NUMBER(self,t):
        r'[1-9][0-9]*'
        print("NUMBER:", t.value)
        return t

    def t_PLUS(self,t):
        r'\+'
        print("PLUS")
        return t

    def t_MINUS(self, t):
        r'\-'
        print("MINUS")
        return t

    def t_OBRACKET(self,t):
        r'\('
        print("OPEN_BRACKET")
        return t

    def t_CBRACKET(self,t):
        r'\)'
        print("CLOSE_BRACKET")
        return t

    def t_EQUAL(self,t):
        r'\='
        print("EQUAL")
        return t

    # every symbol that doesn't match with almost one of the previous tokens is considered an error
    def t_error(self,t):
        r'.'
        print("ERROR:", t.value)
        return t

    def t_nl(self,t):
        r'(\n|\r|\r\n)|\s'
        pass
