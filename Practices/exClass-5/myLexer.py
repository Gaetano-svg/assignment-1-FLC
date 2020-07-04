import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN

class MyLexer():


    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)
        self.lexer.begin('INITIAL')

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    # list of TOKENS
    tokens = [
        
        'ID', 'TYPE',
        'CM', 'S',

    ]
    
    # tokens DEFINITION

    def t_CM(self,t):
        r'\,'
        return t

    def t_S(self,t):
        r'\;'
        return t

    def t_TYPE(self,t):
        r'((int)|(float)|(char)|(double))'
        return t

    def t_ID(self,t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        return t

    def t_nl(self,t):
        r'(\n|\r|\r\n)|\s|\t'
        pass

    # every symbol that doesn't match with almost one of the previous tokens is considered an error
    def t_error(self,t):
        r'.'
        print("ERROR:", t.value)
        return t



