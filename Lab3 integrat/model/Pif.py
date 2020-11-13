class Pif:
    def __init__(self):
        self.info = []

    def getInfo(self):
        return self.info

    def add(self, item):
        ok = True
        for entry in self.info:
            if entry.getVar1() == item.getVar1() and entry.getVar2() == item.getVar2():
                ok = False
        if ok :
            self.info.append(item)

    def toString(self):
        s = ''
        for item in self.info:
            s += item.toString() + "\n"
        return s