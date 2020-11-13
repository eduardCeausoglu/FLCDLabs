from src.model.Pair import Pair

class Scanner:
    def __init__(self, pif, sti, stc, language):
        self.pif = pif
        self.sti = sti         #symbol table for identifiers
        self.stc = stc         #symbol table for constants
        self.language = language
        """
        self.pifPath = "../src/out/Pif.out"
        self.stiPath = "../src/out/Sti.out"
        self.stcPath = "../src/out/Stc.out"
        """

    def getPif(self):
        return self.pif

    def getSti(self):
        return self.sti

    def getStc(self):
        return self.stc

    def run(self, path):        #path to the program file to scan
        errors = []             #potential errors

        with open (path) as progrLines:
            for index, line in enumerate(progrLines):
                tokens = self.tokenize(line)
                print(f"path: {path}; line {index} \n {tokens}")
                for token in tokens:
                    if not self.isTokenValid(token):
                        errors.append(f"error at line {index} caused by token: {token}")

                    elif (
                            self.language.isOperator(token) or
                            (self.language.isSeparator(token) and token != " ") or
                            self.language.isReservedWord(token)
                         ):
                        self.pif.add(Pair(token, -1))

                    #elif token not in self.pif and self.language.isConstant(token):
                    elif self.language.isConstant(token):
                        self.stc.insert(token)
                        self.pif.add(Pair(token, self.stc.getIndex(token)))
                    #elif token not in self.pif and self.language.isIdentifier(token):
                    elif self.language.isIdentifier(token):
                        self.sti.insert(token)
                        self.pif.add(Pair(token, self.sti.getIndex(token)))

        return '\n'.join(errors) or "The progr is correct"



    def tokenize(self, line):
        token_list = []
        index = 0
        token = ''

        while index < len(line):

            if self.isPartOfOperator(line[index]):
                possible_operator = self.getOperatorToken(line, index)

                if possible_operator[0] is not None:
                    if len(token):
                        token_list.append(token)
                    index = possible_operator[1]
                    token_list.append(possible_operator[0])
                    token = ''
                else:
                    token += line[index]
                    index += 1


            elif line[index] == '\n':
                if token != '':
                    token_list.append(token)
                index += 1
                token = ''

            elif self.language.isSeparator(line[index]):
                if token != '':
                    token_list.append(token)
                token_list.append(line[index])
                index += 1
                token = ''
            else:
                token += line[index]
                index += 1

        if token != '':
            token_list.append(token)

        return token_list

    def isPartOfOperator(self, part):
        for operator in self.language.getOperators():
            if operator.find(str(part)) != -1:
                return True
        return False

    def getOperatorToken(self, line, position):
        token = line[position]
        start = position
        while position < (len(line)-1) and self.isPartOfOperator(token):
            position += 1
            token += line[position]

        if(position != len(line)-1):
            token = token[:-1]
            position -= 1


        return (token, position+1) if self.language.isOperator(token) else (None, start)

    def isTokenValid(self, token):
        return (self.language.isOperator(token) or
                self.language.isSeparator(token ) or
                self.language.isReservedWord(token) or
                self.language.isIdentifier(token) or
                self.language.isConstant(token))



