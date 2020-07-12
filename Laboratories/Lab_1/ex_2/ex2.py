import ply.lex as lex
import ply.yacc as yacc
import sys

# list of TOKENS

tokens = [

    'nl',
    'schema',
    'firstlevel',
    'ipaddresscomp',
    'port',
    'escape',
    'ipaddress',
    'name',
    'domain',
    'url',
    
]

# tokens DEFINITION

t_nl = r'\n|\r|\r\n'

t_schema        = r'(http|ftp|gopher|https|nntp|file)'
t_firstlevel    = r'(it|com|gov|edu|net|uk|fr|de|ne|jp|ch)'
t_ipaddresscomp = r'([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])'
t_port          = r'([1-9][0-9]{0,3})'
t_escape        = r'(\%[0-9A-F][0-9A-F])'

t_ipaddress     = r'((' + t_ipaddresscomp + r'\.){3}' + t_ipaddresscomp + r')'
t_name          = r'(([^\n\r\%\/\<\>\:\.\\\#]|' + t_escape + r')+)'
t_domain        = r'(' + t_name + r'\.' + t_name + r'(\.' + t_name + r')*\.' + t_firstlevel + r')'

t_ignore = r'.*'
t_url = t_schema + r':\/\/(' + t_domain + r'|' + t_ipaddress + r')(:' + t_port + r')?(\/' + t_name + r')*((\/)|(' + r'\.' + t_name + r'(\#' + t_name + r')?))?'

def t_error(t):
    print("Illegal characters: ", t.value)
    t.lexer.skip(1)

# reading INPUT FILE

myFile = open(sys.argv[1])

lexer = lex.lex()

with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                if token.type == 'url':
                    print("Correct URL: ", token.value,token.type)
                elif token.type != 'nl':
                    print("Uncorrect URL: ", token.value)

        except EOFError:
            break
   