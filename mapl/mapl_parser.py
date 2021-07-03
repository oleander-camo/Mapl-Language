class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ast = open("mapl_ast.ast", "w+")
        
    def parse(self):
        tokens = self.tokens
        for t in range(len(tokens)):
            if tokens[t]["type"] == "PRINT":
                self.ast.write("print -> ")
            elif tokens[t]["type"] == "SEMICOLON":
                self.ast.write("\n")
            elif tokens[t]["type"] == "STRING":
                self.ast.write(f"string {tokens[t]['value']}")
            elif tokens[t]["type"] == "NUMBER":
                self.ast.write(f"number {tokens[t]['value']}")
            elif tokens[t]["type"] == "CREATEVAR":
                self.ast.write("createvar -> ")
            elif tokens[t]["type"] == "VAR":
                self.ast.write(f"var {tokens[t]['value']}")
            elif tokens[t]["type"] == "EQUALS":
                self.ast.write(" = ")