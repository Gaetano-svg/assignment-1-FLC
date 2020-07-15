from myLexer import *
import ply.yacc as yacc


class MyParser:

    # CONSTRUCTOR
    def __init__(self, myLexer):
        print("Parser called")
        self.parser = yacc.yacc(module=self)
        self.lexer = myLexer
        self.table = {}

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    # Ensure our parser understands the correct order of operations.
    # The precedence variable is a special Ply variable.

    # GRAMMAR START

    def p_prog(self,p):
        '''
        prog : header SEP cars SEP race
        '''
    
    # HEADER SECTION 

    def p_header(self,p):
        '''
        header : token1_l TOKEN2 S token1_l TOKEN3 S token1_l
                    | token1_l TOKEN3 S token1_l TOKEN2 S token1_l
        '''
    
    def p_token1_l (self,p):
        '''
        token1_l : token1_l TOKEN1 S 
                | 
        '''

    # Cars section
    def p_cars(self,p):
        '''
        cars : car car 
                | cars car car
        '''
        
    def p_car(self,p):
        '''
        car : QSTRING SO speeds SC
        '''

        s = p[1]
        tab = p[3]

        self.table[s] = tab

    def p_speeds(self,p):
        '''
        speeds : QSTRING EQ UINT MS
                    | speeds CM QSTRING EQ UINT MS
        '''

        if len(p) == 5:
            s = p[1]
            u = p[3]
            map = {}
            map[s] = u
            p[0] = map
        
        elif len(p) == 7:
            u = p[5]
            s = p[3]
            tab = p[1]
            tab[s] = u
            p[0] = tab

    # /****************/
    # /* Race section */
    # /****************/

    def p_race(self,p):
        '''
        race : print_min_max_l performances
        '''

        s = p[2]
        print("WINNER: ",s[0]," ", s[1], " ", s)
    
    # Management of PRINT_MIN_MAX function

    def p_print_min_max_l(self,p):
        '''
        print_min_max_l : 
                            | print_min_max_l min_max
        '''

    def p_min_max(self,p):
        '''
        min_max : MINMAX RO QSTRING RC RO section_names RC S
        '''

        s = p[3]
        m = p[6]
        print("MIN:", m[0], "MAX:", m[1])

    def p_section_names(self,p):
        '''
        section_names : QSTRING
                            | section_names CM QSTRING
        '''

        if len(p) == 2:
            s = p[1]
            car = p[-3]
            
            # HashMap<String, Integer> speeds = parser.table.get(car);
            speeds = self.table[car]
            speed = speeds[s]

            vect = [0,0]
            vect[0] = speed
            vect[1] = speed
            p[0] = vect

        elif len(p) == 4:
            m = p[1]
            s = p[3]
            car = p[-3]
            
            speeds = self.table[car]
            speed = speeds[s]
            vect = [0,0]

            # Update current min and max values
            if speed < m[0]:
                # New min
                vect[0] = speed
                vect[1] = m[1]
            
            elif speed > m[1] :
                # New max
                vect[0] = m[0]
                vect[1] = speed
            
            else: 
                # No change in min and max
                vect[0] = m[0]
                vect[1] = m[1]

            p[0] = vect

    # Part regarding performances

    def p_performances(self,p):
        '''
        performances : QSTRING ARROW parts S
                        | performances QSTRING ARROW parts S
        '''

        if len(p) == 5:
            s = p[1]
            x = p[3]
            print(s)
            print("TOTAL:", x ," s")

            # To detect the winner car
            vect = [0,0]
            vect[0] = s # car name
            vect[1] = x # result

            p[0] = vect
        
        elif len(p) == 6:
            perf = p[1]
            s = p[2]
            x = p[4]
            print(s)
            print("TOTAL:", x, " s")
            vect = [0,0]

            if perf[1] < x:
                vect[0] = perf[0]
                vect[1] = perf[1]
            
            else :
                vect[0] = s
                vect[1] = x
            
            p[0] = vect

    def p_parts(self,p):
        '''
        parts : NT0 part
                | parts PIPE NT1 part
        '''

        if len(p) == 3:
            p[0] = p[2]

        elif len(p) == 5:
            res = p[1]
            x = p[4]

            p[0] = res + x

    def p_NT0(self, p):
        '''
        NT0 : 
        '''

        p[0] = p[-2]

    def p_NT1(self, p):
        '''
        NT1 : 
        '''

        p[0] = p[-4]

    def p_part(self, p):
        '''
        part : PART UINT COL drive_stats
        '''

        x = p[2]
        stat = p[4]

        p[0] = stat

        print("PART", x, ":", stat, "s")

    def p_drive_stats(self, p):
        '''
        drive_stats : QSTRING UINT M
                        | drive_stats CM QSTRING UINT M
        '''

        if len(p) == 4:
            s = p[1]
            u = p[2]
            car = p[-4]
            
            # HashMap<String, Integer> speeds = parser.table.get(car);
            speeds = self.table[car]
            speed = speeds[s]
            result = float(u) / float(speed)
            p[0] = float(result)
        
        elif len(p) == 6:
            stat = p[1]
            s = p[3]
            u = p[4]
            car = p[-8]

            # HashMap<String, Integer> speeds = parser.table.get(car);
            speeds = self.table[car]
            speed = speeds[s]
            result = float(u) / float(speed)
            p[0] = result
            p[0] = p[0] + stat # Accumulate the time in result
