from Parser import *

class Main:
    def __init__(self):
        self._parser = Parser()

    def _read_grammar(self) -> None:
        self._parser.read_grammar("g2.txt")

    @staticmethod
    def _display_options() -> None:
        print("1 Display Terminals")
        print("2 Display Non-terminals")
        print("3 Display Productions")
        print("4 Choose production to do closure")
        print("5 Choose symbol to do goto on state(ClosureLR of S'->S)")
        print("6 Display Canonical Collection")
        print("7 Display LR table")
        #print("8 Parse word")
        #print("9 Parse with table father sibling")

    def _display_table(self, word: str) -> None:
        colCan = self._parser.colcan_LR()
        lrTable = self._parser.create_LR_table(colCan)
        result = self._parser.parsing_alg(lrTable, colCan, word)
        if result is None:
            print("Error")
            return
        table = self._parser.create_table(result)
        for el in table:
            print(el)

    def _display_prod(self) -> None:
        print(self._parser.P)

    def _display_non_terminals(self) -> None:
        print(self._parser.E)

    def _display_terminals(self) -> None:
        print(self._parser.N)

    def _display_goto(self, value: str) -> None:
        goto = self._parser.goto_LR(self._parser.closure_LR(Pair("S'", ". S")), value)
        if len(goto) == 0:
            print("No results")
            return
        print(goto)

    def _parse_word(self, word: str):
        colCan = self._parser.colcan_LR()
        lrTable = self._parser.create_LR_table(colCan)
        result = self._parser.parsing_alg(lrTable, colCan, word)
        if result is None:
            print("Error")
            return
        print(result)

    def _case5(self):
        value = input("input: ")
        self._display_goto(value)

    def _case8(self):
        word = input("input: ")
        self._parse_word(word)

    def _case9(self):
        word = input("input: ")
        self._display_table(word)

    def run(self):
        self._read_grammar()
        Main._display_options()
        options = {1: self._display_terminals, 2: self._display_non_terminals, 3: self._display_prod, 4: lambda: print(self._parser.closure_LR(Pair("S'", ". S"))),
                   5: self._case5, 6: lambda: print(self._parser.colcan_LR()), 7: lambda: print(self._parser.create_LR_table(self._parser.colcan_LR())),
                   8: self._case8, 9: self._case9}
        while True:
            i = int(input("> "))
            if i in options:
                options[i]()
                continue
            break

if __name__ == "__main__":
    app = Main()
    app.run()
