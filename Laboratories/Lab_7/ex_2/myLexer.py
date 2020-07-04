import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN

class MyLexer():


    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)
        self.lexpos = 1

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    # list of TOKENS
    tokens = [

        'TYPE',
        'NUM',
        'ID',
        'TIMES',
        'SO' , 'SC',
        'S', 'CM',
        'EMPTY'

    ]

    t_ignore = r' '

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'(\r|\n|\r\n)+'
        t.lexer.lineno += len(t.value)                
        pass

    # Compute column.
    # input is the input text string
    # token is a token instance
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    # tokens DEFINITION
    def t_nl(self,t):
        r'(\r|\n|\r\n)'
        pass

    def t_COMMENT(self,t):
        r'\/\*([^\*]*|\*+[^\*\/])\*+\/'
        print("Comment found")
        pass

    def t_NUM(self, t):
        r'(([1-9][0-9]*)|0)'
        return t
    
    def t_TYPE(self,t):
        r'((int) | (float) | (double) | (char))'
        return t

    def t_ID(self,t):
        r'[A-Za-z_][0-9A-Za-z_]*'

        return t

    def t_TIMES(self,t):
        r'\*'
        return t

    def t_SO(self,t):
        r'\['
        return t

    def t_SC(self,t):
        r'\]'
        return t

    def t_S(self,t):
        r'\;'
        return t

    def t_CM(self,t):
        r'\,'
        return t
        
    def t_eof(self,t):
        #print("EOF reached")
        t.lexer.skip(1)

    def t_error(self,t):
        r'.'
        print("ERROR (Character not recognized): ", t.value)
        return t

    def EMPTY(self,t):
        r''
        return t