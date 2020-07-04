
class te_node:

    TEBASETYPE = 1
    TEARRAY = 3
    TEPOINTER = 6

    # CONSTRUCTOR
    def __init__(self):
        self.tag = 0
        self.code = 0
        self.left = ''
        self.right = ''
        self.size = 0

    @staticmethod  
    def te_print(node):

        if(isinstance(node, te_node)):
            
            if node.tag == 1 :
                print("[", node.code, "]", end="")
            
            elif node.tag == 3 :
                print("array(", node.size, ",", end="")
                te_node.te_print(node.left)
                print(")", end="")
            
            elif node.tag == 6:
                print("pointer(", end="")
                te_node.te_print(node.left)
                print(") ", end="")
        
        else:
            return

    def toString(self):
        te_print(self)
        return ""

    def setTag(self, tag):
        self.tag = tag

    def setCode(self, code):
        self.code = code

    @staticmethod
    def te_make_base(code):
        p = te_node()
        p.setTag(1)
        p.setCode(code)
        return p
    
    @staticmethod
    def te_make_pointer(base):
        p = te_node()
        p.setTag(6)
        p.left = base
        return p

    @staticmethod
    def te_make_array(size, base):
        p = te_node()
        p.setTag(3)
        p.left = base
        p.size = size

        return p
