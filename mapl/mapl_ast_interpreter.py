class ASTInterpreter:
    def __init__(self):
        self.ast = open("mapl_ast.ast", "r").read()[0:int(len(open("mapl_ast.ast", "r").read())/2)]
        self.lines = []
        self.symbols = {}
    
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
                if line[9:12] == "var":
                    if line[13:] in self.symbols:
                        print(self.symbols[line[13:]])
                    else:
                        print("varible not defined")
                else:
                    print(line[16:])
            elif line[0:9] == "createvar":
                self.symbols[line[17:line.find('=')-1]] = line[line.find('=')+9:]
            elif line[0:3] == "var":
                if line[4:] in self.symbols:
                    self.symbols[line[4:]]
                else:
                    print("variable not defined")
        # print(self.symbols)