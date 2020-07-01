import ply.lex as lex
import ply.yacc as yacc
import sys

from lexer import *
from parser import *

# create objects MY LEXER and MY PARSER
myLex = MyLexer()
myPars = MyParser()

lex = myLex.lexer
parser = myPars.parser

# reading INPUT FILE

file = ''

with open('./myFile.txt') as fp:
    for line in fp:
        try:
            file = file + line

        except EOFError:
            break

parser.parse(file)
