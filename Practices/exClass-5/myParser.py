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

    # RULES SECTION
    def p_goal(self,p):
        '''
        goal : list_decl
        '''

        print("PARSER: Recognized grammar!!")

    def p_list_decl(self,p):
        '''
        list_decl : 
                    | list_decl decl 
        '''
    
    def p_decl(self,p):
        '''
        decl : TYPE lid S
        '''

        print("PARSER: Found declaration of type:", p[2])
        
    # added a copy-rule -> trying to put the p[-1] inside the p[2] symbol (the previous CM symbol) has no result
    # defining two different productions for the "lid" symbol has no result; it seems that the parser see only
    
    def p_lid(self,p):
        '''
        lid : ID CM r_copy lid
                | ID 
        '''

        p[0] = p[-1]
        print("PARSER: var(", p[1], ",", p[0], ")")

    def p_r_copy(self,p):
        '''
        r_copy : 
        '''
        p[0] = p[-3]
