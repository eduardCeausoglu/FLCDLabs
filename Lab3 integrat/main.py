from src.Scanner import Scanner
from src.model.ST import ST
from src.model.Pif import Pif
from src.Language import Language


if __name__ == '__main__':
    """
    pif = Pif()
    sti = ST()
    stc = ST()
    language = Language()
    scanner = Scanner(pif, sti, stc, language)
    """

    pifPath = "../src/out/Pif.out"
    stiPath = "../src/out/Sti.out"
    stcPath = "../src/out/Stc.out"

    programsPaths = ["../src/in/p1.in", "../src/in/p2.in", "../src/in/p3.in", "../src/in/p1err.in"]
    outPaths = ["../src/out/p1.out", "../src/out/p2.out", "../src/out/p3.out", "../src/out/p1err.out", pifPath, stiPath, stcPath]
    for path in outPaths:      #clear files from last run
        open(path, 'w').close()


    for path in programsPaths:
        pif = Pif()
        sti = ST()
        stc = ST()
        language = Language()
        scanner = Scanner(pif, sti, stc, language)
        outPath = path.replace("in", "out")
        with open (outPath, 'a+') as f:
            f.write(scanner.run(path))

        with open(pifPath, 'a+') as pifFile:
            pifFile.write("\n" + path + "\n")
            #print("\n\n\n\n\n\n\n\n\n" + path + "\n\n\n\n\n\n\n\n\n\n\n")
            pifFile.write(scanner.getPif().toString() or "empty")

        with open(stiPath, 'a+') as stiFile:
            stiFile.write("\n" + path + "\n")
            stiFile.write(scanner.getSti().toString() or "empty")

        with open(stcPath, 'a+') as stcFile:
            stcFile.write("\n" + path + "\n")
            stcFile.write(scanner.getStc().toString() or "empty")
