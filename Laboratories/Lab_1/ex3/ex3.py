import ply.lex as lex
import ply.yacc as yacc
import sys

from Htmllib import *

# EXCLUSIVE-STATE: lex will only return tokens and apply rules defined specifically for that state. 
# INCLUSIVE-STATE:  adds additional tokens and rules to the default set of rules. Thus, lex will return both the tokens defined by default in addition to those defined for the inclusive state. 

# first thing is to create a list of TOKENS
states = (
    ('COMMENT','exclusive'),
)

tokens = [

    'nl',
    'keyword',
    'const',
    'direttive',
    'string',
    'id',
    'point',
    'op',
    'startcomm',
    'comm1',
    'comm2',
    'comm3'

] 

# task DEFINITION

t_COMMENT_comm1 = r'[^\*]+'
t_COMMENT_comm2 = r'\*+[^\*\/]+'
t_COMMENT_comm3 = r'\*+\/'

# must define also an error rule for exclusive state comment
def t_COMMENT_error(t):
    print("Illegal characters (COMMENT): ", t.value)
    t.lexer.skip(1)

t_nl = r'\n|\r|\r\n'
t_keyword              = r'(if|then|else|while|switch|case|do|break|for|return|void|int|float|double|char|long|unsigned|signed)'
t_const                = r'[0-9]+' 
t_direttive            = r'\#(include|define).*'

t_string               = r'\" ~ \"'
t_startcomm             = r'\/\*'

t_id                   = r'[A-Za-z][A-Za-z0-9_]*' 
t_op                   = r'(\+|\-\|\/|\*|\<|\>|\=\=|\>\=|\<\=|\=)' 

t_point = r'.'

def t_error(t):
    print("Illegal characters: ", t.value)
    t.lexer.skip(1)

# reading INPUT FILE

myFile = open(sys.argv[1])

lexer = lex.lex()

startPrint(sys.argv[1])

with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:

                # INITIAL - STATE
                if token.type == 'keyword':
                    colPrint(C_LBLUE)
                    textPrint(token.value)
                    endtagPrint()
                elif token.type == 'const':
                    colPrint(C_LRED)
                    textPrint(token.value)
                    endtagPrint()
                elif token.type == 'direttive':
                    colPrint(C_LGREEN)
                    textPrint(token.value)
                    endtagPrint()
                elif token.type == 'op':
                    colPrint(C_BLUE)
                    textPrint(token.value)
                    endtagPrint()
                elif token.type == 'string':
                    colPrint(C_RED)
                    textPrint(token.value)
                    endtagPrint()
                elif token.type == 'id':
                    colPrint(C_GREEN)
                    textPrint(token.value)
                    endtagPrint()
                elif token.type == 'nl':
                    textPrint(token.value)
                elif token.type == 'point':
                    textPrint(token.value)
                elif token.type == 'startcomm':
                    # begin of comment state
                    lexer.begin('COMMENT')
                    colPrint(C_CYAN)
                    textPrint(token.value)

                # COMMENT - STATE
                elif token.type == 'comm1':
                    textPrint(token.value)
                elif token.type == 'comm2':
                    textPrint(token.value)
                elif token.type == 'comm3':
                    textPrint(token.value)
                    endtagPrint()
                    # begin of initial state
                    lexer.begin('INITIAL')

        except EOFError:
            break

endPrint()