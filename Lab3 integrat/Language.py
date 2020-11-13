import re

class Language:
    def __init__(self):
        self.operators = ["+", "-", "*", "/", "%", ">", "<", "=", ">=", "<=", "!=", "and", "or", "not", ":"]
        self.separators = ["(", ")", "[", "]", "{", "}", ";", " ", "\n", "\t"]
        self.reservedWords =["int", "float", "bool", "if", "elif", "else", "for", "to", "start", "end", "read", "write"]

    def getOperators(self):
        return self.operators

    def getSeparators(self):
        return self.separators

    def getReservedWords(self):
        return self.reservedWords

    def isOperator(self, str):
        return str in self.operators

    def isSeparator(self, str):
        return str in self.separators

    def isReservedWord(self, str):
        return str in self.reservedWords

    def isIdentifier(self, str):
        return re.match("^[a-zA-Z][a-zA-Z0-9]{0,255}", str) is not None

    def isConstant(self, str):
        return self.isBoolean(str) or self.isInteger(str)

    def isBoolean(self, str):
        return (str is "True") or (str is "False")

    def isInteger(self, str):
        return str.isnumeric() and re.match("^[1-9][0-9]{0,18}", str) is not None

