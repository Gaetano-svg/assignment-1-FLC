import sys

C_BLUE   = 1
C_GREEN  = 2
C_CYAN   = 3
C_RED    = 4
C_WHITE  = 5
C_LBLUE  = 6
C_LGREEN = 7
C_LCYAN  = 8
C_LRED   = 9

switcher = {

    1: 	"<FONT color=00007f>",  #C_BLUE 
    2:  "<FONT color=007f00>",  #C_GREEN
    3:  "<FONT color=007f7f>",  #C_CYAN 
    4:  "<FONT color=7f0000>",  #C_RED
    5:  "<FONT color=White>",   #C_WHITE
    6:  "<FONT color=0000ff>",  #C_LBLUE
    7:  "<FONT color=00ff00>",  #C_LGREEN
    8:  "<FONT color=00ffff>",  #C_LCYAN
    9:  "<FONT color=ff0000>"   #C_LRED

}

def startPrint(argument):
    print("<HTML>")
    print('<Body bgcolor="#ffffff">')
    print('<H2>' + argument + '</H2>')
    print('<CODE>', end='')
    return

def endPrint():
    print()
    print("</CODE></BODY></HTML>")
    return

def colPrint(argument):
    print()
    print (switcher.get(argument), end='')
    return

def textPrint(string):

    for c in string:
        if string == '<':
            print("&lt;", end='')

        elif string == '>':
            print("&gt;", end='')

        elif string == '\n':
            print()
            print("<br>", end='')

        elif string == '&':
            print("&amp;", end='')

        else:
            print(c, end='')

    return

def endtagPrint():

    print("</FONT>", end='')
    return
    
