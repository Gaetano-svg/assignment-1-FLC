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

    precedence = (
        ('left', 'LOGOP'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'DIVIDE', 'TIMES', 'MOD'),
        ('left', 'INCR', 'DECR'),
        ('nonassoc', 'IFX'),
        ('nonassoc', 'ELSE')
    )

    # GRAMMAR START

    def p_prog_ok(self,p):
        '''
        prog_ok : dec_prot_list function_list
    	            | function_list
        '''
        print("Program correctly recognized")
        
    def p_dec_prot_list(self,t):
        '''
        dec_prot_list : dec_prot_list dec_prot
    	                    | dec_prot
        '''

    def p_dec_prot(self,t):
        '''
        dec_prot : decl
    	                | function_prot
        '''
        
    def p_function_list(self,p):
        '''
        function_list : function 
                            | function_list function
        '''

    def p_function_decl(self,p):
        '''
        function_decl : type pointer RBOPEN parameter_list RBCLOSED
                            | void ID RBOPEN parameter_list RBCLOSED
                            | STORAGE_SPEC type pointer RBOPEN parameter_list RBCLOSED
                            | STORAGE_SPEC void ID RBOPEN parameter_list RBCLOSED
        '''

    def p_function_prot(self,p):
        '''
        function_prot : function_decl SEMICOLON 
        '''
        
    def p_function(self,p):
        '''
        function : function_decl CBOPEN function_body CBCLOSED
        '''

    def p_function_body(self,p):
        '''
        function_body : empty
    	                | decl_list stmt_list
        '''
    
    def p_parameter_list(self,p):
        '''
        parameter_list : parameter_list COMMA parameter
                            | parameter
                            | void
        '''

    def p_parameter(self,p):
        '''
        parameter : type pointer
    	                | type pointer SBOPEN SBCLOSED
        '''
        
    def p_decl_list(self,p):
        '''
        decl_list : decl 
                        | decl_list decl
        '''
    def p_decl(self,p):
        '''
        decl : type id_list SEMICOLON
    	        | STORAGE_SPEC type id_list SEMICOLON
        '''
    
    def p_id_list(self,p):
        '''
        id_list : id_list COMMA ident
    	            | ident
        '''

    def p_ident(self,p):
        '''
        ident : pointer
                    | pointer SBOPEN CONST SBCLOSED
                    | pointer EQUALS CONST
                    | pointer EQUALS MINUS CONST
                    | pointer SBOPEN SBCLOSED EQUALS CBOPEN const_list CBCLOSED
                    | pointer SBOPEN SBCLOSED EQUALS CBOPEN string_const_list CBCLOSED
        '''

    def p_pointer(self,p):
        '''
        pointer : TIMES pointer
    	            | ID
        '''

    def p_const_list(self,p):
        '''
        const_list : const_list COMMA CONST
    	                | CONST
        '''

    def p_string_const_list(self,p):
        '''
        string_const_list : string_const_list COMMA STRINGCONST
	                            | STRINGCONST
        '''

    def p_void(self,p):
        '''
        void : VOID 
                | empty
        '''

    def p_type(self,p):
        '''
        type : SIGN_MODIFIER TYPE
                    | LENG_MODIFIER TYPE
                    | SIGN_MODIFIER LENG_MODIFIER TYPE
                    | LENG_MODIFIER
                    | TYPE
        '''

    def p_stmt_list(self,p):
        '''
        stmt_list : stmts 
                    | empty
        '''

    def p_stmts(self,p):
        '''
        stmts : stmts stmt
    	            | stmt
        '''

    def p_block(self,p):
        '''
        block : CBOPEN stmt_list CBCLOSED
        '''

    def p_stmt(self,p):
        '''
        stmt : assign_stmt SEMICOLON
                    | if_stmt
                    | while_stmt
                    | block
                    | BREAK SEMICOLON
                    | return_stmt SEMICOLON
                    | for_stmt
                    | switch_stmt
                    | SEMICOLON
        '''

    def p_assign_stmt(self,p):
        '''
        assign_stmt : ID EQUALS expr
                        | ID ASSOP expr
                        | expr
        '''

    def p_term(self,p):
        '''
        term : ID
                | CONST
                | ID RBOPEN arg_list RBCLOSED
                | ID SBOPEN CONST SBCLOSED
                | ID SBOPEN ID SBCLOSED
        '''
    
    def p_arg_list(self,p):
        '''
        arg_list : args 
                    | empty
        '''

    def p_args(self,p):
        '''
        args : args COMMA arg
    	            | arg
        '''

    def p_arg(self,p):
        '''
        arg : term
    	        | STRINGCONST
        '''


    def p_expr(self,p):
        '''
        expr :  expr PLUS expr
                    | expr MINUS expr
                    | expr DIVIDE expr
                    | expr TIMES expr
                    | expr MOD expr
                    | expr INCR
                    | INCR expr
                    | expr DECR
                    | DECR expr
                    | RBOPEN expr RBCLOSED
                    | MINUS expr
                    | PLUS expr
                    | term
        '''
    
    def p_if_stmt(self,p):
        '''
        if_stmt : IF RBOPEN cond RBCLOSED stmt  %prec IFX
    	            | IF RBOPEN cond RBCLOSED stmt ELSE stmt
        '''

    def p_cond(self,p):
        '''
        cond : cond LOGOP cond
                    | RBOPEN cond RBCLOSED
                    | comparison
                    | expr 
        '''

    def p_comparison(self,p):
        '''
        comparison : expr RELOP expr
        '''

    def p_while_stmt(self,p):
        '''
        while_stmt : WHILE RBOPEN cond RBCLOSED stmt 
        '''

    def p_for_stmt(self,p):
        '''
        for_stmt : FOR RBOPEN expr_list SEMICOLON cond SEMICOLON expr_list RBCLOSED stmt 
        '''

    def p_expr_list(self,p):
        '''
        expr_list : expr_list COMMA assign_stmt
    	                | assign_stmt
        '''

    def p_return_stmt(self,p):
        '''
        return_stmt : RETURN expr
    	                | RETURN
        '''

    def p_switch_stmt(self,p):
        '''
        switch_stmt : SWITCH RBOPEN ID RBCLOSED CBOPEN case_list CBCLOSED
    	                | SWITCH RBOPEN ID RBCLOSED CBOPEN case_list default_stmt CBCLOSED
        '''

    def p_case_list(self,p):
        '''
        case_list : case_list case_stmt
    	                | case_stmt
        '''

    def p_case_stmt(self,p):
        '''
        case_stmt : CASE CONST COLON stmt_list
        '''

    def p_default_stmt(self,p):
        '''
        default_stmt : DEFAULT COLON stmt_list 
        '''
    
    def p_error(self,p):
        '''
        error : 
        '''
        print("Syntax error")

    def p_empty(self,p):
        '''
        empty :
        '''
        p[0] = None
