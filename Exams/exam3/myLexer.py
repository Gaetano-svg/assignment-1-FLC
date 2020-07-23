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
        'ws',
        'date', 'odd_number',
        'TOKEN1', 'TOKEN2', 'TOKEN3',
        'QSTRING', 'UINT', 'SEP', 'MINMAX', 
        'PART', 'M', 'MS', 'ARROW', 
        'RC', 'RO', 'SO' , 'SC',
        'EQ', 'PIPE', 'S', 'CM', 'COL',
        'CPP_COMMENT', 

    ]

    # tokens DEFINITION

    t_odd_number = r'((\- (3[135]) | ([12][13579]) | ([13579]) ) | [13579] | [1-9][13579] | [12][0-9][13579] | (3(([0-2][13579])|(3[13]))) )'

    token1_head = [r'((\%\%\%\%\%(\%\%)*) | ( ((\*\*) | (\?\?\?)){2,3} ))', t_odd_number]
    @TOKEN("".join(token1_head))
    def t_TOKEN1(self,t):
        return t

    t_date = r'((2015\/12\/(1[2-9] | 2[0-9] | 3[01])) | 2016\/(01\/(0[1-46-9] | [12][0-9] | 3[01]) | 02\/(0[1-9] | [12][0-9]) | 03\/(0[1-9] | 1[0-3])) )'

    token2_head = [t_date, r'(\-|\+)', t_date]
    @TOKEN("".join(token2_head))
    def t_TOKEN2(self,t):
        return t

    def t_TOKEN3(self,t):
        r'\$( (1(0|1){2,4}) | (10( (1000) | (0(0|1){3}) )) )'
        return t

    def t_UINT(self,t):
        r'((0)|([1-9][0-9]*))'
        return t

    def t_SEP(self,t):
        r'\#\#(\#\#)+'
        return t

    def t_MINMAX(self,t):
        r'PRINT_MIN_MAX'
        return t

    def t_MS(self,t):
        r'm\/s'
        return t

    def t_M(self,t):
        r'm'
        return t

    def t_ARROW(self, t):
        r'\-\>'
        return t

    def t_RO(self, t):
        r'\('
        return t
    
    def t_RC(self,t):
        r'\)'
        return t

    def t_SO(self,t):
        r'\{'
        return t

    def t_SC(self,t):
        r'\}'
        return t

    def t_EQ(self,t):
        r'\='
        return t

    def t_PIPE(self,t):
        r'\|'
        return t

    def t_S(self,t):
        r'\;'
        return t

    def t_CM(self,t):
        r'\,'
        return t

    def t_COL(self,t):
        r'\:'
        return t

    def t_PART(self,t):
        r'PART'
        return t

    def t_CPP_COMMENT(self,t):
        r'\/\/.*'
        pass

    def t_nl(self,t):
        r'(\r|\n|\r\n|\s|\t)'
        pass

    def t_QSTRING(self,t):
        r'("[^"]*")|(\'[^\']*\')'
        return t

    def t_error(self,t):
        r'.'
        print("Scanner Error: ", t.value)
        return t
