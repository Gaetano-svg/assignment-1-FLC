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
        
        'ID', 'EURO', 'INT',
        'CM', 'S', 'C', 'SEP',

    ]
    
    # list of STATES -> used only the one to catch comments
    states = (
        ('COMMENT','exclusive'),
    ) 

    # tokens DEFINITION

    def t_ID(self,t):
        r'[a-zA-Z]+'
        return t

    def t_EURO(self,t):
        r'[0-9]*\.[0-9][0-9]'
        return t

    def t_INT(self,t):
        r'([1-9][0-9]*)|0'
        return t

    def t_CM(self,t):
        r'\,'
        return t

    def t_S(self, t):
        r'\;'
        return t

    def t_C(self,t):
        r'\:'
        return t

    def t_SEP(self,t):
        r'\%'
        return t

    def t_nl(self,t):
        r'(\n|\r|\r\n)|\s|\t'
        pass

    # every symbol that doesn't match with almost one of the previous tokens is considered an error
    def t_error(self,t):
        r'.'
        print("ERROR:", t.value)
        return t
    
    # COMMENT STATE
    
    def t_INITIAL_comm(self,t):
        r'\/\*'
        self.lexer.begin('COMMENT')

    def t_COMMENT_end(self,t):
        '\*\/'
        self.lexer.begin('INITIAL')

    def t_COMMENT_body(self,t):
        r'.'
        pass

    def t_COMMENT_nl(self,t):
        r'(\n|\r|\r\n)|\s|\t'
        pass

    def t_COMMENT_error(self,t):
        r'.'
        print("ERROR:", t.value)
        return t


