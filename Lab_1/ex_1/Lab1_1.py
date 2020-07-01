import ply.lex as lex
import ply.yacc as yacc
import sys

# list of TOKENS

tokens = [

    'nl',
    'letter',
    'digit',
    'id',
    'path'

]

# tokens DEFINITION

t_nl = r'\n|\r|\r\n'

t_letter = r'[^\n\r\\/:*?\"<> |0-9]'
t_digit  = r'[0-9]'
t_id     = r'('+t_digit+'|'+t_letter+')+'

t_path = r'^(' + t_letter + r':)?(\\)?(' + t_id + r'\\)*' + t_id + r'("."' + t_id + r')?$'

t_ignore = r'^.+$'

def t_error(t):
    print("Illegal characters: ", t.value)
    t.lexer.skip(1)

# reading INPUT FILE

file1 = open('./myFile.txt').read()

lexer = lex.lex()

with open('./myFile.txt') as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                if token.type == 'path':
                    print("Path Correct: ", token.value)

        except EOFError:
            break


        