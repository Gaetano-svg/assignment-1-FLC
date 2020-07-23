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

        'nl',
        'NAME',
        'ISBN', 'INT', 'LETTER', 'DATE','ARROW',
        'CL', 'LI', 'LS', 'AV', 'BO', 'SO', 'SEP', 'CM', 'S'
    ]

    # tokens DEFINITION

    t_ignore = r' '
        
    def t_nl(self,t):
        r'(\s|\n|\r|\r\n)'
        pass
        
    def t_ARROW(self,t):
        r'\-\>'
        return t
    
    def t_ISBN(self,t):
        r'([0-9]{2}\-[0-9]{2}\-[0-9A-Fa-f]{5}\-[A-Za-z0-9])'
        return t
    
    def t_CL(self,t):
        r'\:'
        return t
    
    def t_CM(self,t):
        r'\,'
        return t

    def t_S(self,t):
        r'\;'
        return t

    def t_LI(self,t):
        r'LI'
        return t
    
    def t_LS(self,t):
        r'LS'
        return t
    
    def t_AV(self,t):
        r'AV'
        return t
    
    def t_BO(self,t):
        r'BO'
        return t
    
    def t_SO(self,t):
        r'SO'
        return t
    
    def t_SEP(self,t):
        r'\%\%'
        return t

    def t_NAME(self,t):
        r'(\"[A-Za-z0-9\s\.\,\:]+\")'
        return t

    def t_LETTER(self,t):
        r'[A-Za-z]'
        return t

    data_date = [r'(0[1-9]|[1-2][0-9]|3[0-1])\/', r'(0[1-9]|1[0-2])\/', r'([0-9]{4})']
    @TOKEN("".join(data_date))
    def t_DATE(self,t):
        return t

    def t_INT(self,t):
        r'[1-9][0-9]*'
        return t
    
    def t_eof(self,t):
        print("EOF reached")
        t.lexer.skip(1)

    def t_error(self,t):
        r'.'
        print("ERROR (Character not recognized): ", t.value)
        t.lexer.skip(1)
