from src.FA import FA

def printMenu(fa):
    menu = ''
    menu += "1. Display the set of states\n" + "2. Display the alphabet\n" + "3. Display the initial state\n" + "4. Display the set of final states\n" + "5. Display all of the transitions\n" + "6. Check sequence\n"
    print(menu)
    while (True):
        choice = int(input("choice: \n\t>"))
        if choice == 1:
            printSetOfStates(fa)
        elif choice == 2:
            printAlphabet(fa)
        elif choice == 3:
            printInitialState(fa)
        elif choice == 4:
            printFinalStates(fa)
        elif choice == 5:
            printTransitions(fa)
        elif choice == 6:
            if fa.isDFA():
                sequence = input('please input sequence to be tested: \n\t')
                if fa.accept(sequence):
                    print('Sequence accepted!')
                else:
                    print('Sequence not accepted!')
            else:
                print('fa is not a deterministic finite automaton!')


def printSetOfStates(fa):
    print(fa.getQ())

def printAlphabet(fa):
    print(fa.getE())

def printInitialState(fa):
    print(fa.getQ0())

def printFinalStates(fa):
    print(fa.getF())

def printTransitions(fa):
    for key in fa.getS():
        transition = str(key) + ' -> ' + str(fa.getS()[key])
        print(transition)

if __name__ == '__main__':

    fa = FA()
    fa.readFile()
    printMenu(fa)




