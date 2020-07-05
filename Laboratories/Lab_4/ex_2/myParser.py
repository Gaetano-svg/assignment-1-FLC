from myLexer import *
import ply.yacc as yacc


class MyParser:

    # CONSTRUCTOR
    def __init__(self, myLexer):
        print("Parser called")
        self.parser = yacc.yacc(module=self)
        self.lexer = myLexer

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
        ('nonassoc', 'ELSE'),

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

    # error in declaration
    def p_decl_error(self,p):
        '''
        decl : type error S
        '''
        print("Error in declaration ( row:", p[2].lineno, ", column:", self.lexer.find_column(p[2].lexer.lexdata, p[2]),")")

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

    # error in statement
    def p_stmt_list_error(self,p):
        '''
        stmt_list : error stmt 
        '''
        print("Error in statement ( row:", p[1].lineno, ", column:", self.lexer.find_column(p[1].lexer.lexdata, p[1]),")")

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
    # error in statement
    def p_stmt_error(self,p):
        '''
        stmt :  BO stmt_list error BC 
                | BO error BC 
                | error S 
        '''
        if( len(p) == 5 ):
            print("Missing ; before } at ( row:", p[3].lineno, ", column:", self.lexer.find_column(p[3].lexer.lexdata, p[3]),")")

        elif ( len(p) == 4):
            print("Missing ; before } at ( row:", p[2].lineno, ", column:", self.lexer.find_column(p[2].lexer.lexdata, p[2]),")")
            
        else:
            print("Error in statement ( row:", p[1].lineno, ", column:", self.lexer.find_column(p[1].lexer.lexdata, p[1]),")")

    # error in assignment
    def p_assignment_error(self,p):
        '''
        assignment : id EQ error S 
                        | error EQ exp S 
        '''
        # p[1] == None ---> error
        
        # print(p[1], p[2], p[3], p[4])
        if (p[3] != None and p[1] == None):
            if(p[1] == None):
                print("Error in assignment ( row:", p[3].lineno, ", column:", self.lexer.find_column(p[3].lexer.lexdata, p[3]),")")
            else:
                print("Error in assignment ( row:", p[1].lineno, ", column:", self.lexer.find_column(p[1].lexer.lexdata, p[1]),")")
        
        elif(p[3] == None and p[1] != None):
            if(p[3] == None):
                print("Error in expression ( row:", p[1].lineno, ", column:", self.lexer.find_column(p[1].lexer.lexdata, p[1]),")")
            else:
                print("Error in expression ( row:", p[3].lineno, ", column:", self.lexer.find_column(p[3].lexer.lexdata, p[3]),")")
        
            #print("Error in expression ( row:", p[2].lineno, ", column:", self.lexer.find_column(p[2].lexer.lexdata, p[2]),")")
    
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
        '''
        error: empty
        '''

    def p_empty(self,p):
        '''
        empty :
        '''
