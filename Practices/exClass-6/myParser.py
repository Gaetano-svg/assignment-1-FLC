from myLexer import *
from Attrib import *
import ply.yacc as yacc


class MyParser:

    # CONSTRUCTOR
    def __init__(self, myLexer):
        print("Parser called")
        self.parser = yacc.yacc(module=self)
        self.lexer = myLexer
        
        self.classHash = {}
        
        print("")
        print("Achieved scores.")
        
    # DESTRUCTOR
    def __del__(self):
        print("")
        print('Parser destructor called.')


    tokens = MyLexer.tokens
   

    # GRAMMAR START

    def p_prog(self,p):
        '''
        prog : definitions D descriptions
        '''
    
    # DEFINITIONS

    def p_definitions(self,p):
        '''
        definitions : definitions definition
                        | definition
        '''
    
    def p_definition(self,p):
        '''
        definition :  OB attrib_list CB ARROW ident
        '''

        idName = p[5]
        attribHash = p[2]

        # The attribute HashMap is completed...
	    # it can be inserted inside the hashTable
        self.classHash[idName] = attribHash

        # the previous instruction is equivalent to -> parser.classHash.put(idName,attribHash);

    def p_attrib_list(self,p):
        '''
        attrib_list :  attrib_list C attrib
                        | attrib
        '''

        if len(p) == 4:

            attribHash = p[1] # the HashMap created previously
            attrib = p[3]
            name = attrib.getName()
            weight = attrib.getWeight()

            attribHash[name] = weight
            # the previous instruction is equivalent to -> attribHash.put(attrib.name, attrib.weight);

            p[0] = attribHash

        else : 
            # A new HashMap is created to insert the attributes
            hash = {}
            # Current attribute is inserted inside the HashMap
            attrib = p[1]
            name = attrib.getName()
            weight = attrib.getWeight()

            hash[name] = weight
            # the previous instruction is equivalent to -> hash.put(attrib.getName(), attrib.getWeight());

            p[0] = hash

    def p_attrib(self,p):
        '''
        attrib : ident DD NUMBER
        '''

        # Pass an object of the attribute type
        a = p[1]
        b = p[3]

        p[0] = Attrib(a,b)

    # DESCRIPTIONS

    def p_descriptions (self,p):
        '''
        descriptions : descriptions description
                        | 
        '''

    def p_description (self,p):
        '''
        description : ident DD scores EQ sentence SC 
        '''

        print(", ", p[3])

    # The V terminal has the function of the sum operator
    def p_scores(self,p):
        '''
        scores : scores NT0 C valutation
                    | valutation
        '''

        if len(p) == 5:
            # I sum the valuations of the present product
            val1 = int(p[1])
            val2 = int(p[4])
            p[0] = val1 + val2
        
        elif len(p) == 2:
            p[0] = p[1]

    def p_NT0(self,p):
        '''
        NT0 : 
        '''

        p[0] = p[-3]

    def p_valutation(self,p):
        '''
        valutation : point ident
        '''

        identClass = p[-2]

        # I search inside the hash table the entry related to the current class(identClasse)
        hash = self.classHash[identClass]

        # I search inside the hash HashMap the weight associated to the current attribute
        punt = int(p[1])
        name = p[2]
        weight = int(hash[name])

        # Compute the operation
        p[0] = weight * punt

    def p_point(self,p):
        '''
        point : STAR
                | PLUS
                | DIV
                | MINUS
        '''

        if p[1] == '*':
            p[0] = 3
        
        elif p[1] == '+':
            p[0] = 2

        elif p[1] == '/':
            p[0] = 1

        elif p[1] == '-':
            p[0] = 0

    # ELEMENTARY GRAMMAR

    def p_sentence(self,p):
        '''
        sentence : sentence sentence_elem
                    | sentence_elem
        '''

        if len(p) == 3:
            print("", p[2], end="")
        
        elif len(p) == 2:
            print(p[1], end="")

    def p_sentence_elem(self,p):
        '''
        sentence_elem : WORD
                        | NUMBER
        '''

        p[0] = p[1]
    
    def p_ident(self,p):
        '''
        ident : ID
                | WORD
        '''

        p[0] = p[1]

    def p_error(self,p):
        '''
        error: empty
        '''
