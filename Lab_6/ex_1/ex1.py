import ply.lex as lex
import ply.yacc as yacc
import sys

from myLexer import *
from myParser import *

# create objects MY LEXER and MY PARSER
myLex = MyLexer()
myPars = MyParser(myLex)
myLex.init_parser(myPars)

lex = myLex.lexer
parser = myPars.parser

# reading INPUT FILE

file = open('./myFile.txt')
parser.parse(file.read())
