import ply.lex as lex
import ply.yacc as yacc
import sys

from myLexer import *

# create object MY LEXER

myLex = MyLexer()

# reading INPUT FILE

myFile = open(sys.argv[1])

lexer = myLex.lexer

with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                pass

        except EOFError:
            break


        