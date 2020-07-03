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

        'ws',
        'PT', 'SEP1', 'CM', 'SEP2', 'ATOM', 'RO', 'RC', 'VARIABLE'

    ]

    t_ignore = r' '
    
    t_ws = r'([ \t])'

    # tokens DEFINITION

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Compute column.
    # input is the input text string
    # token is a token instance
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
 
    def t_nl(self,t):
        r'(\s|\r)'
        pass

    def t_comm(self,t):
        r'\/\*[^\/\*]*\*\/'
        print("Comment found")
        pass

    def t_RO(self, t):
        r'\('
        return t
    
    def t_RC(self,t):
        r'\)'
        return t

    def t_PT(self, t): 
        r'\.'
        return t

    def t_CM(self, t):
        r'\,'
        return t
    
    def t_SEP1(self,t):
        r'\:\-'
        return t
    
    def t_SEP2(self,t):
        r'\?\-'
        return t
    
    def t_ATOM(self,t):
        r'(((\+|\-)?[0-9]+(\.[0-9]+(e(\+|\-)[0-9]+)?)?)|([a-z][A-Za-z0-9_]*))'
        return t
    
    def t_VARIABLE(self,t):
        r'([A-Z_][A-Za-z0-9_]*)'
        return t
    
    def t_eof(self,t):
        print("EOF reached")
        t.lexer.skip(1)

    def t_error(self,t):
        r'.'
        print("ERROR (Character not recognized): ", t.value)
        return t
