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
        
        'START', 'KBS', 'SERVER', 'TIME', 'DATA', 'S', 'CM', 'C',
        'IP', 'NUMBER', 'SONG', 'DATE', 'HOUR'

    ]

    t_ignore = r' '
    ip_num = r'((2(([0-4][0-9])|(5[0-5])))|(1[0-9][0-9])|([1-9][0-9])|([0-9]))'
    
    # tokens DEFINITION

    def t_START(self,t):
        r'mp3_list'
        return t
        
    def t_KBS(self,t):
        r'Kb\/s'
        return t

    def t_SERVER(self,t):
        r'server'
        return t
    
    def t_TIME(self,t):
        r'time'
        return t
    
    def t_DATA(self,t):
        r'data'
        return t

    def t_C(self,t):
        r'\:'
        return t    

    def t_CM(self,t):
        r'\,'
        return t

    def t_S(self,t):
        r'\;'
        return t

    def t_SONG(self,t):
        r'[a-zA-Z][_a-zA-Z0-9]*\.mp3'
        return t

    def t_DATE(self,t):
        r'((0[1-9])|([1-2][0-9])|(3(0|1)))\/((0[1-9])|(1(0|1|2)))\/(2[0-9][0-9][0-9])'
        return t
    
    def t_HOUR(self,t):
        r'(((0|1)[0-9])|(2[0-3]))\:([0-5][0-9])'
        return t
    
    ip_tag = [ip_num,"\.",ip_num,"\.",ip_num,"\.",ip_num]
    @TOKEN("".join(ip_tag))
    def t_IP(self, t):
        return t

    def t_NUMBER(self,t):
        r'[0-9]+'
        return t

    def t_nl(self,t):
        r'(\n|\r|\r\n)|\s|\t'
        pass

    # every symbol that doesn't match with almost one of the previous tokens is considered an error
    def t_error(self,t):
        r'.'
        print("ERROR:", t.value)
        return t



