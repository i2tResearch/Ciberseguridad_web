import os
from os import walk


def generationOfcsvAuto(start,end, locationOfNfpcaps, locationToSave, myPath):

    for x in range(start, end):

        os.chdir(locationToSave)
        os.system("mkdir " + str(x) + "-csves")

        numberOfFiles = calculateNumberOfFiles(x, myPath)

        for y in range (0,numberOfFiles):
            # Generation of csv
            cmd = "nfdump -r " + locationOfNfpcaps + str(x) + "-nfpcaps/nfcapd." + str(y) + " -o csv > " + locationToSave + str(x) + "-csves/" + str(y)+".csv"
            print(cmd)
            os.system(cmd)


def calculateNumberOfFiles(numberOfCarpet, myPath):
        f = []
        for (dirpath, dirnames, filenames) in walk(myPath + str(numberOfCarpet) + "-nfpcaps/"):
            f.extend(filenames)
            break
        return len(f)


def main():
    start = 81
    end = 82
    myPath = "/home/julioce/Documentos/PDG/PDG-2/Netflows/M/"
    locationOfNfpcaps = "/home/julioce/Documentos/PDG/PDG-2/Netflows/M/"
    locationToSave = "/home/julioce/Documentos/PDG/PDG-2/Datasets/M/"
    generationOfcsvAuto(start,end,locationOfNfpcaps, locationToSave, myPath)


main()