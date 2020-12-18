class Pair:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    def __repr__(self):
        return "<" + str(self._first) + " | " + str(self._second) + ">"

    def __eq__(self, other):
        return self._first == other.first and self._second == other.second

class Grammar:
    def __init__(self):
        self._N = []
        self._E = []
        self._P = []

    @staticmethod
    def line_splitter(line: str) -> list:
        return line.strip().split(" ")[2:]

    @property
    def N(self) -> list:
        return self._N

    @property
    def E(self) -> list:
        return self._E

    @property
    def P(self) -> list:
        return self._P

    def filter_P(self, nonTerminal: str) -> list:
        return list(filter(lambda el: el.first == nonTerminal, self._P))

    def read_grammar(self, filename: str) -> None:
        with open(filename, 'r') as f:
            self._N = self.line_splitter(f.readline())
            self._E = self.line_splitter(f.readline())
            f.readline()
            line = f.readline()
            while line:
                tokens = line.strip().split("->")
                if tokens[0] in self._N:
                    pair = Pair(tokens[0], tokens[1])
                    self._P.append(pair)
                    line = f.readline()
                else:
                    raise Exception("NonTerminal doesn't exist!")
