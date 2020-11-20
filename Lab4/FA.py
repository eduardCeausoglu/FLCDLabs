class FA:
    def __init__(self):
        self.Q = []  #set of all states
        self.E = []  #set of costs
        self.F = []  #set of all final states
        self.S = {}  #the route
        self.q0 = ''  #initial node
        self.Transitions = {}  #list of transitions
        self.filePath = "../data/fa.in"

    def getQ(self):
        return self.Q

    def getE(self):
        return self.E

    def getQ0(self):
        return self.q0

    def getF(self):
        return self.F

    def getS(self):
        return self.S

    def accept(self, sequence):
        currentState = self.q0
        for char in sequence:
            pair = (currentState, char)
            if pair not in self.S.keys():
                return False
            else:
                currentState = self.S[pair][0]
        return True

    def isDFA(self):
        for nodes in self.S.values():
            if len(nodes) > 1:
                return False
        return True

    def readFile(self):
        with open(self.filePath, "r") as f:
            self.Q = f.readline().split()[2:]
            self.E = f.readline().split()[2:]
            input = f.readline()
            self.q0 = input[5:len(input)-1]
            self.F = f.readline()[3:]
            f.readline() # skip a line

            lines = f.readlines()
            for line in lines:
                input = line.replace("->", ",")
                input = input.replace(" ", "")
                processed = input.split(",")
                final = []
                for token in processed:
                    if token.find("\n"):
                        final.append(token.replace("\n", ""))
                    else:
                        final.append(token)
                pair = (final[0], final[1])
                if pair in self.S.keys():
                    self.S[pair].append(final[2])
                else:
                    self.S[pair] = [final[2]]










