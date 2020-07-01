import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN

class MyLexer():


    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')

        self.lexer = lex.lex(module=self)
        # initialize all parameters
        self.file = open('output.html', 'w')

        self.numTags    = 0
        self.numTables  = 0
        self.numH1s     = 0
        self.numH2s     = 0
        self.numH3s     = 0
        self.numH4s     = 0
        self.numComm    = 0

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')
        
        # Total number of tags: comments are not considered as tags
        print("Total number of tags: ", self.numTags)
        print("Total number of table tags: ", self.numTables)
        print("Total number of h1 tags: ", self.numH1s)
        print("Total number of h2 tags: ", self.numH2s)
        print("Total number of h3 tags: ", self.numH3s)
        print("Total number of h4 tags: ", self.numH4s)
        print("Total number of comments: ", self.numComm)

        self.file.close()

    # PARAMETERS
    #   file        -> print on file

    numTags = 0
    numTables = 0
    numComm = 0
    numH1s = 0
    numH2s = 0
    numH3s = 0
    numH4s = 0

    def writeOut(self,string):
        self.file.write(string)

    # list of TOKENS

    tokens = [

        'nl',
        'att',
        'id',

    ]

    # tokens DEFINITION

    def t_nl(self,t):
        r'\s|\n|\r|\r\n'
        self.writeOut(t.value)

    t_id = r'([a-zA-Z_][a-zA-Z0-9_]*)'
    t_att = t_id + r'(\=[^ \t\n\r\<\>]*)'

    # COMMENT SECTION
    def t_sofcomm(self,t):
        r'\<\!\-\-(?:.|\n|\r)*?-->'
        self.numComm = self.numComm + 1

    # INITIAL SECTION

    def t_error(self,t):
        print("ERROR (Character not recognized): ", t.value)
        t.lexer.skip(1)
    
    data_table = ['(\<((TABLE)|(table)))(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_table))
    def t_table(self, t):
        self.numTables = self.numTables + 1
        self.writeOut(t.value)
    
    data_head = ['(\<((HEAD)|(head)))(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_head))
    def t_head(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_body = ['(\<(BODY)|(body))(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_body))
    def t_body(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_html = ['(\<(HTML|(html)))(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_html))
    def t_html(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_title = ['(\<((TITLE)|(title)))(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_title))
    def t_title(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_h1 = ['(\<((H1)|(h1)))(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_h1))
    def t_h1(self,t):
        self.numH1s = self.numH1s + 1
        self.writeOut(t.value)
        
    data_h2 = ['(\<h2)(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_h2))
    def t_h2(self,t):
        self.numH2s = self.numH2s + 1
        self.writeOut(t.value)
        
    data_h3 = ['(\<h3)(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_h3))
    def t_h3(self,t):
        self.numH3s = self.numH3s + 1
        self.writeOut(t.value)
            
    data_h4 = ['(\<h4)(\ +', t_att, ')*(\>)']
    @TOKEN("".join(data_h4))
    def t_h4(self,t):
        self.numH4s = self.numH4s + 1
        self.writeOut(t.value)

    data_tablec = ['(\<\/((TABLE)|(table))\>)']
    @TOKEN("".join(data_tablec))
    def t_tablec(self, t):
        self.numTables = self.numTables + 1
        self.writeOut(t.value)

    data_headc = ['(\<\/((HEAD)|(head))\>)']
    @TOKEN("".join(data_headc))
    def t_headc(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_bodyc = ['(\<\/((BODY)|(body))\>)']
    @TOKEN("".join(data_bodyc))
    def t_bodyc(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_htmlc = ['(\<\/((HTML)|(html))\>)']
    @TOKEN("".join(data_htmlc))
    def t_htmlc(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)
    
    data_titlec = ['(\<\/((TITLE)|(title))\>)']
    @TOKEN("".join(data_titlec))
    def t_titlec(self,t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_h1c = ['(\<\/((H1)|(h1))\>)']
    @TOKEN("".join(data_h1c))
    def t_h1c(self,t):
        self.numH1s = self.numH1s + 1
        self.writeOut(t.value)
        
    data_h2c = ['(\<\/((H2)|(h2))\>)']
    @TOKEN("".join(data_h2c))
    def t_h2c(self,t):
        self.numH2s = self.numH2s + 1
        self.writeOut(t.value)
        
    data_h3c = ['(\<\/((H3)|(h3))\>)']
    @TOKEN("".join(data_h3c))
    def t_h3c(self,t):
        self.numH3s = self.numH3s + 1
        self.writeOut(t.value)
            
    data_h4c = ['(\<\/((H4)|(h4))\>)']
    @TOKEN("".join(data_h4c))
    def t_h4c(self,t):
        self.numH4s = self.numH4s + 1
        self.writeOut(t.value)

    data_tag = ['\<',t_id,'((" "|\t)+',t_att,')*(\>)']
    @TOKEN("".join(data_tag))
    def t_tag(self, t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    data_tagc = ['\<\/',t_id,'\>']
    @TOKEN("".join(data_tagc))
    def t_tagc(self, t):
        self.numTags = self.numTags + 1
        self.writeOut(t.value)

    def t_other(self,t):
        r'.'
        self.writeOut(t.value)

 