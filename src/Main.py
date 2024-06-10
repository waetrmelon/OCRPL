import Lexxer

Directory = "C:\\Users\\shmid\\Documents\\Programming\OCRLang\\tests\\Variables.ocrl"

with open(Directory) as f:
    Contents = f.read().splitlines()

Lexxer.Tokenize(Contents)