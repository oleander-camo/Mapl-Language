class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
    
    def gen_string(self):
        text = self.text
        # print(text)
        tmpstr = ""
        tmpbool = False
        for char in text:
            if char == '"':
                if not tmpbool:
                    tmpbool = True
                else:
                    tmpbool = False
            if char in "\n \t" and not tmpbool:
                char = ''
            tmpstr += char
        text = tmpstr
        return text
    
    def gen_tokens(self):
        text = self.gen_string()
        tmpstr = ""
        tmpbool = False
        for char in text:
            tmpstr += char
            if char == '"':
                if not tmpbool:
                    tmpbool = True
                else:
                    tmpbool = False
                    self.tokens.append({"type": "STRING", "value": tmpstr})
                    tmpstr = ""
                    tmpbool = False
            elif char == '%' and not tmpbool:
                tmpbool = True
            elif char == '%' and tmpbool:
                tmpbool = False
                self.tokens.append({"type": "NUMBER", "value": eval(tmpstr[1:-1])})
                tmpstr = ""
                tmpbool = False
            elif char == ';' and not tmpbool:
                self.tokens.append({"type": "SEMICOLON", "value": tmpstr})
                tmpstr = ""
            elif tmpstr == "print" and not tmpbool:
                self.tokens.append({"type": "PRINT", "value": tmpstr})
                tmpstr = ""
            elif tmpstr == "input" and not tmpbool:
                self.tokens.append({"type": "INPUT", "value": tmpstr})
                tmpstr = ""
            elif tmpstr == "crev" and not tmpbool:
                self.tokens.append({"type": "CREATEVAR", "value": tmpstr})
                tmpstr = ""
            elif char == "@" and not tmpbool:
                self.tokens.append({"type": "VAR", "value": tmpstr})
                tmpstr = ""
            elif char == "=" and not tmpbool:
                self.tokens.append({"type": "EQUALS", "value": tmpstr})
                tmpstr = ""
        return self.tokens