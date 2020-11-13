class Pair:
    def __init__(self, v1, v2):
        self.var1 = v1
        self.var2 = v2

    def getVar1(self):
        return self.var1
    def setVar1(self, v1):
        self.var1 = v1
    def getVar2(self):
        return self.var2
    def setVar2(self, v2):
        self.var2 = v2

    def toString(self):
        return f"({self.var1}, {self.var2})"
