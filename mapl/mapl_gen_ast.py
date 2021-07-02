from sys import argv

from mapl_lexer import *
from mapl_parser import *

lexer = Lexer(open(argv[1], "r").read())
print(lexer.gen_tokens())
parser = Parser(lexer.gen_tokens())
parser.parse()

print("Generated the AST... ")