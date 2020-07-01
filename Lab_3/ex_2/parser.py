from lexer import *
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

    # GRAMMAR START

    def p_file(self,p):
        '''
        file : authors_list SEP loans_list
        '''

        print('File correctly recognized')
    
    def p_authors_list(self,p):
        '''
        authors_list : authors_list author_entry 
                        | author_entry
        '''
    
    def p_author_entry(self,p):
        '''
        author_entry : NAME ARROW books S
        '''

    def p_books(self,p):
        '''
        books : books CM book 
                | book
        '''

    def p_book(self,p):
        '''
        book : ISBN CL NAME CL INT CL collocation 
                | ISBN CL NAME CL INT
        '''
    
    def p_collocation(self,p):
        '''
        collocation : l_g INT LETTER 
                        | l_g INT
        '''
    
    def p_lg(self,p):
        '''
        l_g : LI AV 
                | LI SO 
                | LS AV 
                | LS SO 
                | LS BO
        '''
        
    def p_loans_list(self,p):
        '''
        loans_list : loans_list loan_entry 
                        | loan_entry
        '''

    def p_loan_entry(self,p):
        '''
        loan_entry : NAME CL loan_books S
        '''
    
    def p_loan_books(self,p):
        '''
        loan_books : loan_books CM DATE ISBN 
                        | DATE ISBN
        '''
    
    def p_error(self,p):
        print("Syntax error at ", p)

    def p_empty(self,p):
        '''
        empty :
        '''
        p[0] = None
