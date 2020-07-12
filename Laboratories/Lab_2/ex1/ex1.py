import ply.lex as lex
import ply.yacc as yacc
import sys

# list of TOKENS

tokens = [

    'nl',
    'ws',
    'id',
    'integer', 'double',
    'BO', 'BC' , 'SO', 'SC', 'RO', 'RC',
    'EQ', 'PLUS', 'MINUS', 'STAR', 'DIV', 'MIN', 'MAJ',
    'MIN_EQ', 'MAJ_EQ', 'EQ_MAJ', 'EQ_MIN',
    'AND', 'OR', 'NOT', 
    'INTTYPE', 'DOUBLETYPE',
    'print', 'if', 'while', 'else', 'C', 'S'

]

# list of STATES -> used only the one to catch comments
states = (
    ('COMMENT','exclusive'),
) 

# tokens DEFINITION

t_nl = r'\n|\r|\r\n'

t_ws            = r'[\ \t]'
t_id            = r'[A-Za-z_][A-Za-z0-9_]*'
t_integer       = r'([1-9][0-9]*|0)'
t_double        = r'(([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+))(e|E(\+|\-)?[0-9]+)?'


def t_print(t):
    r'print'
    print('PRINT ', end='')

def t_if(t):
    r'if'
    print('IF ', end='')

def t_while(t):
    r'while'
    print('WHILE ', end='')

def t_else(t):
    r'ELSE'
    print('ELSE ', end='')

def t_S(t):
    r'\;'
    print('S ', end='')

def t_C(t):
    r'\,'
    print('C ', end='')

def t_RO(t):
    r'\('
    print("RO ", end='')

def t_RC(t):
    r'\)'
    print("RC ", end='')  

def t_BO(t):
    r'\{'
    print("BO ", end='')

def t_BC(t):
    r'\}'
    print("BC ", end='')
    
def t_SO(t):
    r'\['
    print("SO ", end='')

def t_SC(t):
    r'\]'
    print("SC ", end='')

def t_EQ(t):
    r'\='
    print("EQ ", end='')

def t_PLUS(t):
    r'\+'
    print("PLUS ", end='')

def t_MINUS(t):
    r'\-'
    print("MINUS ", end='')

def t_MIN(t):
    r'\<'
    print("MIN ", end='')

def t_MAJ(t):
    r'\>'
    print("MAJ ", end='')

def t_MIN_EQ(t):
    r'\<\='
    print("MIN_EQ ", end='')

def t_EQ_MIN(t):
    r'\=\<'
    print("EQ_MIN ", end='')

def t_MAJ_EQ(t):
    r'\>\='
    print("MAJ_EQ ", end='')

def t_EQ_MAJ(t):
    r'\('
    print("EQ_MAJ ", end='')

def t_AND(t):
    r'\&'
    print("AND ", end='')

def t_OR(t):
    r'\|'
    print("OR ", end='')

def t_NOT(t):
    r'\!'
    print("NOT ", end='')

def t_INTTYPE(t):
    r'int'
    print("INT_TYPE", end=' ')

def t_DOUBLETYPE(t):
    r'double'
    print("DOUBLE_TYPE", end=' ')

# COMMENT STATE
    
def t_INITIAL_comm(t):
    r'\/\*'
    t.lexer.begin('COMMENT')

def t_COMMENT_end(t):
    r'\*\/'
    t.lexer.begin('INITIAL')

def t_COMMENT_body(t):
    r'.'
    pass

def t_COMMENT_nl(t):
    r'(\n|\r|\r\n)|\s|\t'
    pass

def t_COMMENT_error(t):
    r'.'
    print("ERROR:", t.value)
    return t

def t_STAR(t):
    r'\*'
    print("STAR ", end='')

def t_DIV(t):
    r'\/'
    print("DIV ", end='')

def t_error(t):
    r'.'
    print("SCANNER ERROR: ", t.value)
    t.lexer.skip(1)


# reading INPUT FILE

myFile = open(sys.argv[1])

lexer = lex.lex()

with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                if(token.type == 'id'):
                    print("ID:", token.value, end=' ')
                elif(token.type == 'integer'):
                    print("INT:", token.value, end=' ')
                elif(token.type == 'double'):
                    print("DOUBLE:", token.value, end=' ')
                elif(token.type == 'ws'):
                    pass
                elif( token.type == 'nl'):
                    pass

        except EOFError:
            break

print()
        