from myLexer import *
from te_node import *
from var_info import *
import ply.yacc as yacc


class MyParser:

    # CONSTRUCTOR
    def __init__(self, myLexer):
        print("Parser called")
        self.parser = yacc.yacc(module=self)
        self.lexer = myLexer
        self.type_table = {}
        self.var_table = {}
        self.colRowTable = {} # table used to store for each row the "starting" lexpos of the lexer -> is used to track the column and row of the current operation

        self.type_table["int"] = te_node.te_make_base(1)
        self.type_table["float"] = te_node.te_make_base(2)
        self.type_table["char"] = te_node.te_make_base(3)
        self.type_table["double"] = te_node.te_make_base(4)

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    def type_lookup(name):
        rv = self.type_table[name]
        return rv

    def add_var(self, name, _type):
        vip = var_info(self)
        print("var", name, ":", end="")
        #_type_node = self.type_table[_type]
        te_node.te_print(_type)
        print("")
        vip.setName(name)
        vip.setType(_type)
        
        try:
            self.var_table[name] = vip
            return 1

        except KeyError:

            return 0
    

    # GRAMMAR START


    def p_Decll(self,p):
        '''
        Decll :  Decll Decl S
                    | empty
        '''
    
    def p_Decll_error(self,p):
        '''
        Decll : Decll error S
        '''

        print ("Error in declaration")

    def p_Decl(self,p):
        '''
        Decl : T Vlist
        '''


    def p_T(self,p):
        '''
        T : TYPE
        '''

        p[0] = te_node.te_make_base(p[1])


    def p_Vlist(self,p):
        '''
        Vlist : V
                | Vlist CM NT0 V
        '''

        p[0] = p[1]

    def p_NT0(self,p):
        '''
        NT0 : empty
        '''

        p[0] = p[-2]

    def p_V(self,p):
        '''
        V : Ptr ID Ary
        '''

        #print("add var p[3]", p[-1])

        self.add_var(p[2], p[3])
        p[0] = p[-1]

    def p_Ptr(self,p):
        '''
        Ptr : empty
                | Ptr TIMES
        '''

        #print("ptr",p[-1])

        if len(p) == 3:
            #print("ptr1", p[1])
            p[0] = te_node.te_make_pointer(p[1])
        
        elif len(p) == 2:
            p[0] = p[-1]
        
    def p_Ary(self,p):
        '''
        Ary : empty
                | Ary SO NUM SC
        '''

        #print("ary", p[-2])

        if len(p) == 5:
            p[0] = te_node.te_make_array(p[3], p[1])
        
        elif len(p) == 2:
            p[0] = p[-2]


    def p_error(self,p):
        '''
        error: empty
        '''

    def p_empty(self,p):
        '''
        empty :
        '''
