from myLexer import *
import ply.yacc as yacc
import sys


class MyParser:

    # CONSTRUCTOR
    def __init__(self,lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        
        self.symbol_table = {}

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    
    tokens = MyLexer.tokens


    # GRAMMAR START

    # RULES SECTION
    def p_prog(self,p):
        '''
        prog : products SEP receipts
        '''

    # FIRST SECTION
    def p_products(self,p):
        '''
        products : products product
                    | product
        '''
    
    def p_product(self,p):
        '''
        product : ID EURO S
        '''

        # equivalent to {: parser.symbolTable.put(x, price); :}
        self.symbol_table[p[1]] = p[2]

    # SECOND SECTION
    def p_receipts(self,p):
        '''
        receipts : receipts receipt
                    | 
        '''

    def p_receipt(self,p):
        '''
        receipt : ID C purchasedProducts S
        '''

        print(p[1], ":", p[3], "EURO")

    def p_purchasedProducts(self,p):
        '''
        purchasedProducts : purchasedProducts CM purchasedProduct
                                | purchasedProduct
        '''

        if len(p) == 4:
            x = float(p[1])
            y = float(p[3])
            p[0] = x+y
        
        elif len(p) == 2:
            p[0] = float(p[1])

    def p_purchasedProduct(self,p):
        '''
        purchasedProduct : INT ID
        '''

        quantity = float(p[1])
        prod = float(self.symbol_table[p[2]])
        p[0] = quantity * prod

    def p_error(self,p):
        '''
        '''