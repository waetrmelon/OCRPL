class AssignmentNode():
    def __init__(self, AssignmentName, AssignmentValue) -> None:
        self.AssignmentName = AssignmentName
        self.AssignmentValue = AssignmentValue 
    def __repr__(self) -> str:
        return " Assignment Node -> Name: ({}) Value: ({}) ".format(self.AssignmentName, self.AssignmentValue)

class Parser():
    def __init__(self, Tokens) -> None:
        self.Tokens = Tokens
        self.CurrentTokenIndex = -1

    def AdvanceToken(self, amount=1):
        self.CurrentTokenIndex += amount
        if self.CurrentTokenIndex < len(self.Tokens):
            self.CurrentToken = self.Tokens[self.CurrentTokenIndex]

    def TokenPeek(self):
        if self.CurrentTokenIndex + 1 < len(self.Tokens):
            return self.Tokens[self.CurrentTokenIndex+1]
        return None

    def AssignmentRule(self):
        if self.CurrentToken.TokenType == "Misc":
            if self.TokenPeek().TokenType == "Character" and self.TokenPeek().TokenValue == "=":
                AssignmentName = self.CurrentToken.TokenValue
                self.AdvanceToken(2)
                AssignmentValue = []
                while self.CurrentToken.TokenType != "NewLine" and self.CurrentToken.TokenValue != r"\n":
                    AssignmentValue.append(self.CurrentToken)
                    self.AdvanceToken()
                self.ast.append(AssignmentNode(AssignmentName, AssignmentValue))

    def GenerateAST(self):
        self.AdvanceToken()
        
        self.ast = []
        print("-" * 25)
        while self.CurrentTokenIndex < len(self.Tokens):

            self.AssignmentRule()
            self.AdvanceToken()


        for node in self.ast:
            print(node)

        print("-" * 25 + "\nFinished Parsing\n" + "-" * 25 )
        return self.ast

def Parse(Tokens):
    return Parser(Tokens).GenerateAST()