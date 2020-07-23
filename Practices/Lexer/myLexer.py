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
        
        'NUMBER',
        'DIV', 'STAR', 'PLUS', 'MINUS',
        'OPEN_BRACKET', 'CLOSE_BRACKET',
        'EQUAL', 'error'

    ]

    # tokens DEFINITION

    def t_NUMBER(self,t):
        r'[1-9][0-9]*'
        print("NUMBER:", t.value)

    def t_PLUS(self,t):
        r'\+'
        print("PLUS")

    def t_MINUS(self, t):
        r'\-'
        print("MINUS")
    
    def t_STAR(self,t):
        r'\*'
        print("STAR")

    def t_DIV(self,t):
        r'\/'
        print("DIV")

    def t_OPEN_BRACKET(self,t):
        r'\('
        print("OPEN_BRACKET")

    def t_CLOSE_BRACKET(self,t):
        r'\)'
        print("CLOSE_BRACKET")

    def t_EQUAL(self,t):
        r'\='
        print("EQUAL\n")

    def t_nl(self,t):
        r'(\n|\r|\r\n)|\s|\t'

    # every symbol that doesn't match with almost one of the previous tokens is considered an error
    def t_error(self,t):
        r'.'
        print("ERROR:", t.value)
        t.lexer.skip(1)
