from typing import Optional

from Grammar import *

class Parser:
    def __init__(self):
        self._grammar = Grammar()

    @property
    def N(self) -> list:
        return self._grammar.N

    @property
    def E(self) -> list:
        return self._grammar.E

    @property
    def P(self) -> list:
        return self._grammar.P

    def read_grammar(self, filename: str):
        self._grammar.read_grammar(filename)

    @staticmethod
    def find_string(lst: list, string: str) -> int:
        for i in range(len(lst)):
            if lst[i] == string:
                return i
        return -1

    def closure_LR(self, analysis: Pair) -> list:
        tokens = [analysis.first, analysis.second]
        P = list()
        P.append(Pair(tokens[0], tokens[1]))
        size = 0
        while size < len(P):
            size = len(P)
            filteredP = P.copy()
            for pair in filteredP:
                index = self.find_string(pair.second.split(" "), '.')
                if index != -1 and index < len(pair.second.split(" ")) - 1:
                    nonT = pair.second.split(" ")[index + 1]
                    filteredB = self._grammar.filter_P(nonT)
                    filteredB = map(lambda p: Pair(p.first, '. ' + p.second), filteredB)
                    for pairB in filteredB:
                        if pairB not in P:
                            P.append(pairB)
        return P

    def goto_LR(self, productions: list, symbol: str) -> list:
        nestedList = []
        productions = map(lambda el: Pair(el.first, el.second.replace(". " + symbol, symbol + " .")),
                          filter(lambda el: (". " + symbol) in el.second, productions))
        for pair in productions:
            nestedList.extend(self.closure_LR(pair))
        return nestedList

    def includedForEach(self, C: list, goToRes: list) -> bool:
        return any(self.included(states, goToRes) for states in C)

    @staticmethod
    def included(C: list, goToRes: list) -> bool:
        return all(elem in C for elem in goToRes)

    def colcan_LR(self) -> list:
        C = list()
        C.append(self.closure_LR(Pair("S'", ". S")))
        dirty = True
        while dirty:
            dirty = False
            filteredC = C.copy()
            for state in filteredC:
                for elem in self.N + self.E:
                    goToRes = self.goto_LR(state, elem)
                    print(self.goto_LR(state, elem))

                    if len(goToRes) != 0 and not self.includedForEach(C, goToRes):
                        C.append(goToRes)
                        dirty = True
        return C

    def _has_reduce(self, state: list) -> int:
        for el in state:
            if el.second.split(" ")[-1] == '.':
                return self._grammar.P.index(Pair(el.first, el.second[0:-2]))
        return -1

    def create_LR_table(self, states: list) -> dict:
        lrTable = {}

        for position, state in zip(range(len(states)), states):
            if Pair("S'", "S .") in state:
                lrTable[position] = Pair("acc", {})
            elif (self._has_reduce(state)) != -1:
                lrTable[position] = Pair("reduce " + str(self._has_reduce(state)), {})
            else:
                lrTable[position] = Pair("shift", {})
                for el in self.N + self.E:
                    goToRes = self.goto_LR(state, el)
                    if len(goToRes) != 0:
                        lrTable[position].second[el] = states.index(goToRes)


        return lrTable

    def parsing_alg(self, lrTable: dict, C: list, word: str) -> Optional[list]:
        state = C[0]
        alpha = []
        beta = []
        phi = []
        alpha.append("0")
        parse = word.split(" ")
        for p in parse:
            beta.append(p)

        while True:
            position = int(alpha[-1])
            if lrTable[position].first == "shift":
                a = beta.pop(0)
                state = self.goto_LR(state, a)
                alpha.append(a)
                alpha.append(str(C.index(state)))
            elif lrTable[position].first == "reduce":
                phi.append(lrTable[position].first[:7])
                reducer = int(phi[-1])
                production = self.P[reducer]
                for i in range(2 * len(production.second.split(" "))):
                    alpha.pop()
                state = self.goto_LR(C[int(alpha[-1])], production.first)
                alpha.append(production.first)
                alpha.append(str(C.index(state)))
            else:
                if lrTable[position].first == "acc":
                    return list(reversed(phi))
                return None


    def create_table(self, productions: list) -> list:
        table = list()
        table.append(Pair("S", Pair(-1, -1)))
        kStack = []
        k = 0
        index = 0
        kStack.append(k)
        for production in productions:
            k = kStack.pop()
            while table[k].first not in self.N:
                k += 1
                index += 1
            prod = self.P[int(production)]
            i = 0
            if prod.second.split(" ")[i] in self.N:
                kStack.append(index + 1)
            index += 1
            table.append(Pair(prod.second.split(" ")[i], Pair(k, -1)))
            i += 1
            while i < len(prod.second.split(" ")):
                if prod.second.split(" ")[i] in self.N:
                    kStack.append(index + 1)
                index += 1
                table.append(Pair(prod.second.split(" ")[i], Pair(k, index)))
        return table
