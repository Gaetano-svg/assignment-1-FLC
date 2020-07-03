from myLexer import *
import ply.yacc as yacc


class MyParser:

    # CONSTRUCTOR
    def __init__(self):
        print("Parser called")
        self.parser = yacc.yacc(module=self)

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    # Ensure our parser understands the correct order of operations.
    # The precedence variable is a special Ply variable.

    precedence = (

        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'NOT'),
        ('left', 'MIN', 'MAJ', 'MIN_EQ', 'EQ_MIN', 'MAJ_EQ', 'EQ_MAJ', 'EQ'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'STAR', 'DIV'),
        ('left', 'UMINUS'),
        ('nonassoc', 'IFX'),
        ('nonassoc', 'ELSE')

    )

    # GRAMMAR START

    def p_prog(self,p):
        '''
        prog : decl_list stmt_list
        '''

        print('Programm correctly recognized')
    
    # DECLARATION

    def p_decl_list(self,p):
        '''
        decl_list : decl_list decl 
                    | 
        '''
    
    def p_decl(self,p):
        '''
        decl : type var_list S
        '''

    def p_type(self,p):
        '''
        type : INT_TYPE 
                | DOUBLE_TYPE
        '''

    def p_var_list(self,p):
        '''
        var_list : var 
                    | var_list CM var
        '''
    
    def p_var(self,p):
        '''
        var : ID array
        '''
    
    def p_array(self,p):
        '''
        array : empty
                | array SO INT SC
        '''
    
    # INSTRUCTIONS

    def p_stmt_list(self,p):
        '''
        stmt_list : stmt_list stmt 
                    | stmt 
        '''
    
    def p_stmt(self,p):
        '''
        stmt : if 
                | while 
                | assignment 
                | print 
                | BO stmt_list BC
        '''

    # Assignment instruction
    def p_assignment(self,p):
        '''
        assignment : id S 
                        | id EQ exp S 
        '''
    
    # Print instruction
    def p_print(self,p):
        '''
        print : PRINT id S
        '''
    
    # If instruction
    def p_if(self,p):
        '''
        if  : IF if_condition stmt %prec IFX
                | IF if_condition stmt ELSE stmt
        '''
    
    def p_if_condition(self,p):
        '''
        if_condition : RO exp RC
        '''

    # While instruction
    def p_while(self,p):
        '''
        while : WHILE while_condition stmt
        '''

    def p_while_condition(self,p):
        '''
        while_condition : RO exp RC
        '''

    # Expressions
    def p_exp(self,p):
        '''
        exp :   exp AND exp
                | exp OR exp
                | NOT exp
                | exp EQ EQ exp
                | exp MIN exp
                | exp MAJ exp
                | exp MAJ_EQ exp
                | exp EQ_MAJ exp
                | exp MIN_EQ exp
                | exp EQ_MIN exp
                | exp PLUS exp
                | exp MINUS exp
                | exp STAR exp
                | exp DIV exp
                | RO exp RC
                | id
                | INT
                | DOUBLE
                | MINUS INT %prec UMINUS
                | MINUS DOUBLE %prec UMINUS
        '''

    def p_id(self,p):
        '''
        id : ID
            | ID SO INT SC
            | ID SO ID SC
        '''

    def p_error(self,p):
        print("Syntax error at ", p)

    def p_empty(self,p):
        '''
        empty :
        '''
        #p[0] = None
