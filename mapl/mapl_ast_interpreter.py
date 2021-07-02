class ASTInterpreter:
    def __init__(self):
        self.ast = open("mapl_ast.ast", "r").read()[0:int(len(open("mapl_ast.ast", "r").read())/2)]
        self.lines = []
    
    def gen_string(self):
        ast = self.ast
        line = ""
        for char in ast:
            if char in "\n":
                self.lines.append(line)
                line = ""
            else:
                line += char
        # print(self.lines)
    
    def interpret(self):
        ast = self.ast
        tmpstr = ""
        tmpbool = False
        for line in self.lines:
            if line[0:5] == "print":
                print(line[16:])