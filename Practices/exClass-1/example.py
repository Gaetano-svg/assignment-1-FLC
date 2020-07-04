import ply.lex as lex
import ply.yacc as yacc
import sys

from myLexer import *

# create objects MY LEXER and MY PARSER
myLex = MyLexer()

lexer = myLex.lexer

# reading INPUT FILE

with open('./myFile.txt') as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                pass

        except EOFError:
            break

