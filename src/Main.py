import Lexxer
import Parser
Directory = r"/home/emir/Documents/GitHub/OCRPL/tests/Variables.ocrl"

with open(Directory) as f:
    Contents = f.read().splitlines()

Tokens = Lexxer.Tokenize(Contents)
Ast = Parser.Parse(Tokens)