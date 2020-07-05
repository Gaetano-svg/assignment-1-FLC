import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN

class MyLexer():


    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    # list of TOKEN
    tokens = [

        'nl',
        'ws',
        'ASSOP', 'RELOP', 'LOGOP', 'SIGN_MODIFIER', 'LENG_MODIFIER', 'STORAGE_SPEC', 'TYPE',
        'STRINGCONST', 'CONST', 'ID', 'VOID', 
        'RBCLOSED', 'RBOPEN', 'CBOPEN', 'CBCLOSED', 'SBOPEN' , 'SBCLOSED',
        'DIVIDE', 'TIMES', 'PLUS', 'MINUS', 'EQUALS', 'INCR', 'DECR', 'MOD',
        'IF', 'ELSE', 'WHILE', 'SWITCH', 'CASE', 'FOR', 'RETURN', 'DEFAULT', 'BREAK',
        'SEMICOLON', 'COMMA', 'COLON'

    ]

    # list of STATES -> used only the one to catch comments
    states = (
        ('COMMENT','exclusive'),
    )

    # tokens DEFINITION
    
    def t_RBOPEN(self, t):
        r'\('
        return t
    
    def t_RBCLOSED(self,t):
        r'\)'
        return t

    def t_ASSOP(self,t):
        r'((\+\=)|(\-\=)|(\*\=)|(\/\=))'
        return t

    def t_RELOP(self,t):
        r'((\=\=)|(\>\=)|(\<\=)|(\<)|(\>)|(\!\=))'
        return t
    
    def t_LOGOP(self,t):
        r'((\|\|)|(\&\&))'
        return t
    
    def t_SIGN_MODIFIER(self,t):
        r'((signed)|(unsigned))'
        return t

    def t_LENG_MODIFIER(self,t):
        r'((long)|(short))'
        return t
        
    def t_STORAGE_SPEC(self,t):
        r'((extern)|(register)|(auto)|(static))'
        return t

    def t_TYPE(self,t):
        r'((int)|(long)|(short)|(float)|(double)|(char))'
        return t

    def t_STRINGCONST(self,t):
        r'(\"([^\n\r\"]+|\\\")*\")'
        return t

    def t_CONST(self,t):
        r'(([0-9]+)|((([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+))(e|E(\+|\-)?[0-9]+)?))'
        
        return t

    def t_VOID(slef,t):
        r'void'
        return t

    def t_nl(self,t):
        r'(\s|\n|\r|\r\n)'
        pass

    def t_ws(self,t):
        r'([ \t]+)'
        pass

    def t_directive(self,t):
        r'(\#((include)|(define)).*\n)'
        pass

    def t_CBOPEN(self,t):
        r'\{'
        return t

    def t_CBCLOSED(self,t):
        r'\}'
        return t

    def t_SBOPEN(self,t):
        r'\['
        return t

    def t_SBCLOSED(self,t):
        r'\]'
        return t

    def t_EQUALS(self,t):
        r'\='
        return t

    def t_INCR(self,t):
        r'\+\+'
        return t

    def t_PLUS(self,t):
        r'\+'
        return t

    def t_DECR(self,t):
        r'\-\-'
        return t

    def t_MINUS(self,t):
        r'\-'
        return t

    def t_MOD(self,t):
        r'\%'
        return t

    def t_IF(self,t):
        r'if'
        return t

    def t_WHILE(self,t):
        r'while'
        return t

    def t_ELSE(self,t):
        r'else'
        return t

    def t_SWITCH(self,t):
        r'switch'
        return t

    def t_CASE(self,t):
        r'case'
        return t

    def t_FOR(self,t):
        r'for'
        return t
    
    def t_RETURN(self,t):
        r'return'
        return t

    def t_DEFAULT(self,t):
        r'default'
        return t

    def t_BREAK(self,t):
        r'break'
        return t

    def t_SEMICOLON(self,t):
        r'\;'
        return t

    def t_COMMA(self,t):
        r'\,'
        return t

    def t_COLON(self,t):
        r'\:'
        return

    def t_ID(self,t):
        r'([A-Za-z_][A-Za-z0-9_]*)'
        return t
    
    def t_eof(self,t):
        print("EOF reached")
        t.lexer.skip(1)

    # COMMENT STATE
    
    def t_INITIAL_comm(self,t):
        r'\/\*'
        self.lexer.begin('COMMENT')

    def t_COMMENT_end(self,t):
        '\*\/'
        self.lexer.begin('INITIAL')

    def t_COMMENT_body(self,t):
        r'.'
        pass

    def t_COMMENT_nl(self,t):
        r'(\n|\r|\r\n)|\s|\t'
        pass

    def t_COMMENT_error(self,t):
        r'.'
        print("ERROR:", t.value)
        return t

    def t_TIMES(self,t):
        r'\*'
        return t

    def t_DIVIDE(self,t):
        r'\/'
        return t

    def t_error(self,t):
        print("ERROR (Character not recognized): ", t.value)
        t.lexer.skip(1)
