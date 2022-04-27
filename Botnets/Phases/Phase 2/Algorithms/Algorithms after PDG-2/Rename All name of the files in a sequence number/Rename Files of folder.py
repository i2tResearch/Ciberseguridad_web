import os
from os import walk

def renameFilesAlg(mypath, start, end):

    for z in range(start, end):
        print("Vamos aqui:" + str(z))
        f = []
        for (dirpath, dirnames, filenames) in walk(mypath + str(z) + "-nfpcaps/"):
            f.extend(filenames)
            break

        y = 0
        for x in f:
            os.rename("/home/julioce/Documentos/PDG/PDG-2/Netflows/M/"+str(z) +"-nfpcaps/" + x,
                          "/home/julioce/Documentos/PDG/PDG-2/Netflows/M/" + str(z)+ "-nfpcaps/nfcapd." + str(y))
            y = y+1


def main():
    start = 81
    end = 82
    mypath = "/home/julioce/Documentos/PDG/PDG-2/Netflows/M/"
    renameFilesAlg(mypath,start,end)


main()