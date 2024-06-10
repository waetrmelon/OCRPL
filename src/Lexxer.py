CHARACTERS = list("=()")
DIGITS = list("1234567890.")
SYNTAX = ["print"]

class Token():
    def __init__(self, TokenType, TokenValue) -> None:
        self.TokenType = TokenType
        self.TokenValue = TokenValue
    def __repr__(self) -> str:
        return " Token -> Type: ({}) Value: ({}) ".format(self.TokenType, self.TokenValue)

class Tokenizer():
    def __init__(self, FileContent) -> None:
        self.FileContent = FileContent
        self.CurrentCharacterIndex = -1
        self.CurrentLineIndex = -1
        self.CurrentLine = ""
        self.CurrentCharacter = ""

    def AdvanceCharacter(self):
        self.CurrentCharacterIndex += 1
        if self.CurrentCharacterIndex < len(self.CurrentLine):
            self.CurrentCharacter = self.CurrentLine[self.CurrentCharacterIndex]

    def AdvanceLine(self):
        self.CurrentLineIndex += 1
        if self.CurrentLineIndex < len(self.FileContent):
            self.CurrentCharacterIndex = -1
            self.CurrentLine = self.FileContent[self.CurrentLineIndex]

    def ProduceString(self):
        String = ""
        self.AdvanceCharacter()

        while self.CurrentCharacter != "\"" and self.CurrentCharacterIndex < len(self.CurrentLine):
            String += self.CurrentCharacter
            self.AdvanceCharacter()

        self.AdvanceCharacter()
        self.GeneratedTokens.append(Token("String", String))

    def ProduceNumber(self):
        Number = ""

        while self.CurrentCharacter in DIGITS and self.CurrentCharacterIndex < len(self.CurrentLine):
            Number += self.CurrentCharacter
            self.AdvanceCharacter()

        if Number == ".":
            self.GeneratedTokens.append(Token("CallMethod", "."))
            return

        if Number.count(".") > 1:
            self.GeneratedTokens.append(Token("Misc", Number))
            return
        elif Number.count(".") == 1:
            self.GeneratedTokens.append(Token("Float", float(Number)))
            return
        else:
            self.GeneratedTokens.append(Token("Integer", int(Number)))
    
    def ProduceExtraCharacters(self):
        if self.ExtraCharacters == "": return
        if self.ExtraCharacters in SYNTAX:
            self.GeneratedTokens.append(Token("Syntax", self.ExtraCharacters))
            self.ExtraCharacters = ""
        else:
            self.GeneratedTokens.append(Token("Misc", self.ExtraCharacters))
            self.ExtraCharacters = ""


    def LexicalAnalysis(self):
        self.AdvanceLine()
        self.AdvanceCharacter()


        self.GeneratedTokens = []
        self.ExtraCharacters = ""

        while self.CurrentLineIndex < len(self.FileContent):
            print("-" * 25)
            print("-> " + self.CurrentLine)
            print("-" * 25)

            while self.CurrentCharacterIndex < len(self.CurrentLine):

                print(": \'" + self.CurrentCharacter + "\'")


                if self.CurrentCharacter == " ": self.AdvanceCharacter()
                elif self.CurrentCharacter in CHARACTERS:
                    self.ProduceExtraCharacters()
                    self.GeneratedTokens.append(Token("Character", self.CurrentCharacter))
                    self.AdvanceCharacter()
                elif self.CurrentCharacter in DIGITS:
                    self.ProduceExtraCharacters()
                    self.ProduceNumber()
                elif self.CurrentCharacter == "\"" or self.CurrentCharacter == "\'":
                    self.ProduceExtraCharacters()
                    self.ProduceString()
                else:
                    self.ExtraCharacters += self.CurrentCharacter 
                    self.AdvanceCharacter() 
            
            self.AdvanceLine()
            self.AdvanceCharacter()
            self.GeneratedTokens.append(Token("NewLine", "\\n"))
            
            print("-" * 25 + "\nFinished Lexical Analysis\n" + "-" * 25 )

        for token in self.GeneratedTokens:
            print(token)
        return self.GeneratedTokens

def Tokenize(Contents):
    return Tokenizer(Contents).LexicalAnalysis()