from myLexer import *
import ply.yacc as yacc
import sys


class MyParser:

    # CONSTRUCTOR
    def __init__(self,lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    
    tokens = MyLexer.tokens


    # GRAMMAR START
    def p_expr_list(self,p):
        '''
        expr_list : expr_list expr
                    | expr
        '''

    def p_expr(self,p):
        '''
        expr : e EQUAL
        '''

        print("PARSER: expression recognized")

    def p_e(self,p):
        '''
        e : e PLUS t
            | e MINUS t
            | t
        '''      

    def p_t(self,p):
        '''
        t : OBRACKET e CBRACKET
                | NUMBER
        '''

    def p_error(self,p):
        '''
        '''

