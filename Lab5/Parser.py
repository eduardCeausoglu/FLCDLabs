class Parser:
    def __init__(self):
        self.nonTerminals = []
        self.terminals = []
        self.startingSymbol = ''
        self.productions = {}

    def tokenize(self, string):
        return string.strip().split(' ')

    def readFile(self, fileName):
        with open(fileName, 'r') as f:
            self.nonTerminals = self.tokenize(f.readline())
            self.terminals = self.tokenize(f.readline())
            self.startingSymbol = self.tokenize(f.readline())[0]
            for line in f:
                content = line.split('-')
                key = content[0].strip()
                values = content[1].split('|')
                self.productions[key] = []
                for val in values:
                    lst = []
                    for v in val.strip().split(' '):
                        lst.append(v)
                    self.productions[key].append(lst)


    def validate(self):
        return self.validateStartingSymbol() and self.validateProductions()

    def validateStartingSymbol(self):
        if self.startingSymbol not in self.terminals:
            print(self.startingSymbol + " was not found in terminals list")
            return False
        return True

    def validateProductions(self):
        for key, val in self.productions.items():
            if key not in self.nonTerminals:
                print(str(key) + " key was not found in non terminals list")
                return False
            for entry in val:
                for element in entry:
                    if element not in self.nonTerminals and element not in self.terminals:
                        print(str(element) + " was not found in terminals list or non terminals list")
                        return False
        return True

    def getProductionsOfNonTerminals(self, nonTerminal):
        if nonTerminal in self.nonTerminals:
            return self.productions[nonTerminal]
        else:
            print("invalid non terminal, " + nonTerminal + "not found in non terminals list")



    def toString(self):
        s=''
        s += "Non terminals: " + str(self.nonTerminals)
        s += "\nTerminals: " + str(self.terminals)
        s += "\nStarting Symbol: " + self.startingSymbol + '\n'
        for key in self.productions.keys():
            s += str(key) + '->' + str(self.productions[key]) + '\n'

        return s
