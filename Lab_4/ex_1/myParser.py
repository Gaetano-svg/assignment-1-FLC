from myLexer import *
import ply.yacc as yacc
import sys


class MyParser:

    # CONSTRUCTOR
    def __init__(self,lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        # static variables initialization
        self.fact_found = 0
        self.error_found = 0

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    # Ensure our parser understands the correct order of operations.
    # The precedence variable is a special Ply variable.

    precedence = (


    )

    # GRAMMAR START

    def p_log_prog(self,p):
        '''
        prog : elements interrogation elements
        '''

        if(self.fact_found != 0 and self.error_found != 1):
            print('Programm correctly recognized')
    
    # DECLARATION

    def p_elements(self,p):
        '''
        elements : 
                    | elements element
        '''

    def p_element(self,p):
        '''
        element : fact
                    | rule
        '''

    def p_fact(self,p):
        '''
        fact : predicate PT
        '''
        
        self.fact_found = 1

    def p_fact_error(self,p):
        '''
        fact : error PT
        '''
        print("Error in a fact ( row:", p[1].lineno, ", column:", self.lexer.find_column(p[1].lexer.lexdata, p[1]),")")
        self.error_found = 1

    def p_rule(self,p):
        '''
        rule : predicate SEP1 predicates PT
        '''
    
    def p_rule_error(self,p):
        '''
        rule : error SEP1 predicates PT
        '''

        print("Error in a rule ( row:", p[1].lineno, ", column:", self.lexer.find_column(p[1].lexer.lexdata, p[1]),")")
        self.error_found = 1

    def p_predicates(self,p):
        '''
        predicates : predicates CM predicate
                    | predicate
        '''
    
    def p_interrogation(self,p):
        '''
        interrogation : SEP2 predicates PT
        '''
    
    def p_interrogation_error(self,p):
        '''
        interrogation : SEP2 error PT
        '''

        print("Error in an interrogation ( row:", p[2].lineno, ", column:", self.lexer.find_column(p[2].lexer.lexdata, p[2]),")")
        self.error_found = 1

    def p_predicate(self,p):
        '''
        predicate : ATOM RO arguments RC 
                | ATOM 
        '''
    
    def p_arguments(self,p):
        '''
        arguments : arguments CM argument 
                    | argument 
        '''
    
    def p_argument(self,p):
        '''
        argument : predicate
                | VARIABLE 
        '''
    
    def p_error(self,p):
        '''
        '''

