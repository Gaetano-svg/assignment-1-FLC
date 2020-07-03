from myLexer import *
from SymbolType import *
from Expr import *
import ply.yacc as yacc


class MyParser:

    # CONSTRUCTOR
    def __init__(self, myLexer):
        print("Parser called")
        self.parser = yacc.yacc(module=self)
        self.lexer = myLexer
        self.label = 0
        self.symbolType_table = {}
        self.enableSem = True
        self.errorBuffer = ''
        self.outputBuffer = ''
        self.semErrors = 0
        self.semWarnings = 0
        self.synWarnings = 0
        
        self.colRowTable = {} # table used to store for each row the "starting" lexpos of the lexer -> is used to track the column and row of the current operation

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
        ('nonassoc', 'ELSE'),

    )

    def genLabel(self):
        self.label = self.label + 1
        return self.label

    def lookupSymbolType(self, p, indId):
        
        try:
            _type = self.symbolType_table[p[indId]]
            return _type

        except KeyError:

            self.pSemError("Variable \"" + p[indId] + "\" not declared ", p, indId)
            return SymbolType(-1,-1)
        

    # ERROR MANAGEMENT

    def disableSem(self):
        self.enableSem = False
    
    def sem(self):
        return self.enableSem

    def pSemError(self, message, p, index):
        
        _lineno = p.lineno(index)
        _lexpos = self.colRowTable[_lineno]

        self.errorBuffer += "SEM ERROR: line: ( row:" + str(_lineno) + ", column:" + str(p.lexpos(index) - _lexpos) + ") : "+message+"\n"
        self.semErrors += 1
    
    def pSemWarning(self, message, p, index):
        
        _lineno = p.lineno(index)
        _lexpos = self.colRowTable[_lineno]

        self.errorBuffer += "SEM WARNING: line: ( row:" + str(_lineno) + ", column:" + str(p.lexpos(index) - _lexpos) + ") : "+message+"\n"
        self.semWarnings += 1

    def pSynError(self, message, p, index):
        
        _lineno = p.lineno(index)
        _lexpos = self.colRowTable[_lineno]

        print("SYN ERROR: line: ( row:" + str(_lineno) + ", column:" + str(p.lexpos(index) - _lexpos) + ") : "+message+"\n")
        print("Could not continue parsing")
        #self.done_parsing()

    def pSynWarning(self, message, p, index):
        
        _lineno = p.lineno(index)
        _lexpos = self.colRowTable[_lineno]

        self.errorBuffer += "SYN WARNING: ( row:" + str(_lineno) + ", column:" + str(p.lexpos(index) - _lexpos) + ") : "+message+"\n"
        self.synWarnings += 1
        # When there is a syntactic warning semantic is disable to avoid errors due to invalid data structures
        self.disableSem()
    
    #  Functions to dump program output 

    def dump(self, s):
        self.outputBuffer += s

    def dumpln(self, s):
        self.outputBuffer += s + "\n"

    # GRAMMAR START

    def p_prog(self,p):
        '''
        prog : decl_list stmt_list
        '''
        result = self.sem()

        if self.sem():
            if self.semErrors == 0:
                self.dumpln("\tEND")
                print(self.outputBuffer)
        
        else:
            print("\nOUTPUT COULD NOT BE PRODUCED DUE TO ERRORS\n")
        
        print(self.errorBuffer)
        print("Syntactic Errors : ", self.synWarnings)
        print("Semantic Errors  : ", self.semErrors)
        print("Semantic Warnings: ", self.semWarnings)
    
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
                | type var_list error
        '''

        if p[3] == ';':
            self.pSynWarning("Error in declaration", p , 2)

        else:
            self.pSynWarning("Error in declaration, missing ;", p , 2)

    def p_type(self,p):
        '''
        type : INT_TYPE 
                | DOUBLE_TYPE
        '''

        if(self.sem()):
            if (p[1] == 'int'):
                p[0] = 'INT'
            elif (p[1] == 'double'):
                p[0] = 'DOUBLE'

    def p_m_copy(self,p):
        '''
        m_copy : empty
        '''

        # passing inherited TYPE - attribute for variable list
        p[0] = p[-2]

    def p_var_list(self,p):
        '''
        var_list : var 
                    | var_list CM m_copy var
        '''

        if self.sem():
            
            if(len(p) == 4):    # equivalent to RESULT = parser.stack(-2)
                p[0] = p[-1]

            else:               # passing inherited TYPE ATTRIBUTE for variable list
                p[0] = p[1]
    
    def p_var(self,p):
        '''
        var : ID 
                | ID SO INT SC
        '''

        p[0] = p[-1] # inheriting TYPE ATTRIBUTE for variable list
        
        if self.sem():
            if(len(p) == 2):
                self.dumpln("\t" + p[-1] + " " + p[1])

                if p[-1] == 'INT' :
                    self.symbolType_table[p[1]] = SymbolType(0,1)
                elif p[-1] == 'DOUBLE' :
                    self.symbolType_table[p[1]] = SymbolType(1,1)
                    
            elif(len(p) == 5):
                self.dumpln("\t" + p[-1] + " " + p[1] + "[" + p[3] + "]")
                
                if p[-1] == 'INT':
                    self.symbolType_table[p[1]] = SymbolType(0,p[3])
                
                elif p[-1] == 'DOUBLE':
                    self.symbolType_table[p[1]] = SymbolType(1,p[3])
        
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

        self.pSynWarning("Error in statement", p, 1)

    def p_stmt(self,p):
        '''
        stmt : if 
                | while 
                | assignment 
                | print 
                | BO stmt_list BC
        '''
    # error in statement
    def p_stmt_error(self,p):
        '''
        stmt :  BO stmt_list error BC 
                        | BO error BC 
                        | error S 
        '''

        if( len(p) == 5 ):
            self.pSynWarning("Missing ; before } ", p, 3)

        elif ( len(p) == 4):
            self.pSynWarning("Missing ; before } ", p, 1)
            
        else:
            self.pSynWarning("Error in statement", p, 1)

    # Assignment instruction
    def p_assignment(self,p):
        '''
        assignment : id S 
                        | id EQ exp S 
        '''

        if self.sem():
            if(len(p) == 3):
                self.dumpln("\t" + p[1])

            elif(len(p) == 5):
                p[1].checkSymbolTypeAssignment(p, 3)
                self.dumpln("\tEVAL " + p[3].toString() + "\n\tASS " + p[1].toString())

    # error in assignment
    def p_assignment_error(self,p):
        '''
        assignment : id EQ error S 
                        | error EQ exp S 
                        | id EQ exp error
        '''

        if(isinstance(p[1], Expr)):
            if p[4] == ";":
                self.pSynWarning("Error in assignment", p, 3)
                
            else:
                self.pSynWarning("Error in assignment missing ;", p, 4)
        
        else:
            self.pSynWarning("Error in expression", p, 1)

    # Print instruction
    def p_print(self,p):
        '''
        print : PRINT id S
        '''

        if(self.sem()):
            self.dumpln("\tPRINT " + p[2].toString())


    # error in print instruction
    def p_print_error(self,p):
        '''
        print : PRINT error S
        '''

        self.pSynWarning("Error in print instruction ", p, 2)

    # If instruction
    def p_if(self,p):
        '''
        if  :  IF if_condition nt0_if stmt ELSE nt1_if stmt
                | IF if_condition nt0_if stmt
                | IF if_condition nt0_if stmt error nt1_if stmt
        '''

        if(len(p) == 8):
            if(p[5] == 'else' & self.sem()):
                self.dump("L" + str(p[3]) + ":")
            else:
                self.pSynWarning("Error, else expected in if instruction", p, 5)

        elif self.sem():
            self.dump("L" + str(p[3]) + ":")

    def p_if_condition(self,p):
        '''
        if_condition : RO exp RC
        '''

        if(self.sem()):
            p[0] = p[2].toString()
    
    def p_if_condition_error(self,p):
        '''
        if_condition : RO error RC
                        | error exp RC
                        | RO exp error
        '''
        if(p[3] == ')'):
            if(p[1] == '('):
                self.pSynWarning("Error in if condition", p, 2)

            else:
                self.pSynWarning("Error ( expected in if instruction", p, 1)
    
        else:
            self.pSynWarning("Error ) expected in if instruction", p, 3)


    def p_nt0_if(self, p):
        '''
        nt0_if : empty
        '''

        if self.sem():
            p[0] = self.genLabel()
            self.dumpln("\tEVAL " + str(p[-1]) + "\t\t/* if (line " + str(self.lexer.lexer.lineno) + ") */\n\tGOTOF L" + str(p[0]))

    def p_nt1_if(self,p):
        '''
        nt1_if : empty
        '''

        if self.sem():
            p[0] = self.genLabel()
            self.dumpln("\tGOTO L" + p[0])
            self.dump("L" + p[-2] + ":")

    # While instruction
    def p_while(self,p):
        '''
        while : WHILE while_condition nt0_while stmt
        '''
        
        if self.sem():
            l = p[3]
            self.dumpln("\tGOTO L" + str(l[0]))
            self.dump("L" + str(l[1]) + ":")
        

    def p_while_condition(self,p):
        '''
        while_condition : RO exp RC
        '''

        if self.sem():
            p[0] = p[2].toString()

    def p_while_condition_error(self,p):
        '''
        while_condition : RO error RC
                            | error exp RC
                            | RO exp error
        '''
        
        if(p[3] == ')'):
            if(p[1] == '('):
                self.pSynWarning("Error in while condition ", p, 2)

            else:
                self.pSynWarning("Error ( expected in while instruction ", p, 1)
    
        else:
            self.pSynWarning( "Error ) expected in while instruction ", p, 3)

    def p_nt0_while(self,p):
        '''
        nt0_while : empty
        '''

        if(self.sem()):
            x = [self.genLabel(), self.genLabel()]
            p[0] = x
            self.dumpln("L" + str(x[0]) + ":\tEVAL " + p[-1] + "\t\t/* while (line " + str(self.lexer.lexer.lineno) + ") */\n\tGOTOF L" + str(x[1]))
            

    # Expressions

    def p_exp_int (self,p):
        '''
        exp_int : INT
                    | MINUS INT %prec UMINUS
        '''

        if self.sem():
            if(len(p) == 2):
                p[0] = Expr.valTypeConstr(self, p[1], SymbolType(0,1))
            else:
                p[0] = Expr.valTypeConstr(self, "-" + p[2], SymbolType(0,1))

    def p_exp_double (self,p):
        '''
        exp_double : DOUBLE
                    | MINUS DOUBLE %prec UMINUS
        '''

        if self.sem():
            if(len(p) == 2):
                p[0] = Expr.valTypeConstr(self, p[1], SymbolType(1,1))
            else:
                p[0] = Expr.valTypeConstr(self, "-" + p[2], SymbolType(1,1))


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
                | exp_double
                | exp_int
                | id
        '''

        expr = ''

        if len(p) == 2:
            p[0] = p[1]

        elif self.sem():
            if(len(p) == 3):
                if(p[1] == '!'):
                    expr = p[2] + " ! "
                    p[0] = Expr.valTypeConstr(self, expr, p[2].getSymbolType())
            
            elif(len(p) == 4):

                if p[1].toString() == '(' :
                    p[0] = p[2]
                else:
                    p1 = p[1].toString()
                    p3 = p[3].toString()
                    if(p[2] == '&'):
                        expr = p1 + " " + p3 + " & "
                    elif(p[2] == '|'):
                        expr = p1 + " " + p3 + " | "
                    elif(p[2] == '<'):
                        expr = p1 + " " + p3 + " < "
                    elif(p[2] == '>'):
                        expr = p1 + " " + p3 + " > "
                    elif(p[2] == '<=' ):
                        expr = p1 + " " + p3 + " <= "
                    elif(p[2] == '=<'):
                        expr = p1 + " " + p3 + " <= "
                    elif(p[2] == '>=' ):
                        expr = p1 + " " + p3 + " >= "
                    elif(p[2] == '=>'):
                        expr = p1 + " " + p3 + " >= "
                    elif(p[2] == '+' ):
                        expr = p1 + " " + p3 + " + "
                    elif(p[2] == '-'):
                        expr = p1 + " " + p3 + " - "
                    elif(p[2] == '*'):
                        expr = p1 + " " + p3 + " * "
                    elif(p[2] == '/'):
                        expr = p1 + " " + p3 + " / "

                p[0] = Expr.valTypeConstr(self, expr, p[1].checkSymbolType(p, 3))
            
            elif (len(p) == 5):
                if(p[2] == '=' and p[3] == '='):
                    expr = p[1].toString() + " " + p[4].toString() + " == "
                    p[0] = Expr.valTypeConstr(self, expr, p[1].checkSymbolType(p, 4))
        

    def p_exp_error(self,p):
        '''
        exp : RO error RC
        '''

        self.pSynWarning("Error in expression", p, 2)

    def p_id(self,p):
        '''
        id : ID
            | ID SO INT SC
            | ID SO ID SC
        '''

        if self.sem():
            if len(p) == 2:
                p[0] = Expr.idConstr(self, p, 1)

            elif len(p) == 5:
                
                p[0] = Expr.idPosConstr(self, p, 1, 3)

    def p_error(self,p):
        '''
        error: empty
        '''

    def p_empty(self,p):
        '''
        empty :
        '''
