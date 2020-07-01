import ply.lex as lex
import ply.yacc as yacc
import sys

from myLexer import *

# create object MY LEXER

myLex = MyLexer()

# reading INPUT FILE

file1 = open('./myFile.txt').read()

lexer = myLex.lexer

with open('./myFile.txt') as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                pass

        except EOFError:
            break


        