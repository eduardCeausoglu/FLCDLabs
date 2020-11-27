from Parser import Parser

def printMenu(parser):

    print('1. Grammar')
    print('2. Non terminals')
    print('3. Terminals')
    print('4. Starting Symbol')
    print('5. All productions')
    print('6. Specific production')
    print('0. Exit')

    msg = int(input("choice: \n\t>"))
    if(msg == 0):
        print("bye")
        return False
    if msg == 1:
        print(parser.toString())
    elif msg == 2:
        print(parser.nonTerminals)
    elif msg == 3:
        print(parser.terminals)
    elif msg == 4:
        print(parser.startingSymbol)
    elif msg == 5:
        for key in parser.productions.keys():
            print(str(key) + '->' + str(parser.productions[key]))
    elif msg == 6:
        string = input("string: \n\t>")
        try:
            print(parser.getProductionsOfNonTerminals(string))
        except Exception as exception:
            print(exception)
    return True


def main():
    parser = Parser()
    fileName = 'file.txt'
    parser.readFile(fileName)
    try:
        parser.validate()
    except Exception as exception:
        print(exception)
        return

    ok = True
    while(ok):
        ok = printMenu(parser)




if __name__ == '__main__':
    main()