from myLexer import *
import ply.yacc as yacc
import sys


class MyParser:

    # CONSTRUCTOR
    def __init__(self,lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        
        self.symbol_table = {}
        print("")

    # DESTRUCTOR
    def __del__(self):
        print("")
        print('Parser destructor called.')

    
    tokens = MyLexer.tokens

    # GRAMMAR START

    def p_prog(self,p):
        '''
        prog : prog_ok
        '''

        print("Syntax Correct")

    def p_prog_ok(self,p):
        '''
        prog_ok : START C mp3_list SERVER C data_time user_list
        '''
    
    def p_mp3_list(self,p):
        '''
        mp3_list : mp3 
                    | mp3_list mp3
        '''
    
    def p_mp3(self,p):
        '''
        mp3 : NUMBER KBS NT1 C NT0 song_list S
        '''

    def p_NT1(self, p):
        '''
        NT1 : 
        '''

        p[0] = int(p[-2])

    def p_NT0(self, p):
        '''
        NT0 : 
        '''

        p[0] = int(p[-4])

    def p_song_list(self,p):
        '''
        song_list : song_list CM song 
                    | song
        '''

    def p_song(self, p):
        '''
        song : SONG NUMBER
        '''
            
        rate = int(p[-3])
        title = p[1]
        length = int(p[2])

        self.symbol_table[title] = length * rate
        # the previous instruction is equivalent to -> parser.symbol_table.put(title, length*rate);

    def p_data_time(self,p):
        '''
        data_time : TIME C HOUR DATA C DATE
                    | DATA C DATE TIME C HOUR 
        '''

        print("OUTPUT: ")

    def p_user_list(self,p):
        '''
        user_list : 
                    | user_list user
        '''
    
    def p_user(self,p):
        '''
        user : ip C songs_list S
        '''

        print("TOTAL:", p[3])

    def p_ip(self,p):
        '''
        ip : IP
        '''

        print(p[1])
    
    def p_songs_list(self, p):
        '''
        songs_list : SONG
                        | songs_list CM SONG
        '''

        if len(p) == 2:
            song_title = p[1]
            length = int(self.symbol_table[song_title])
            print(song_title, length)
            p[0] = length
        
        elif len(p) == 4:
            x = int(p[1])
            song_title = p[3]
            length = int(self.symbol_table[song_title])
            print(song_title, length)
            p[0] = length + x

    def p_error(self, p):
        '''
        '''
