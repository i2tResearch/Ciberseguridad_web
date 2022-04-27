from os import walk


def joiningAllCvs(path, start, end, dataName, nameSummary):
    flag = 0
    counter = 0
    fout = open(dataName, "a")
    summary = open(nameSummary,"a")
    for x in range (start, end):
        print("Va en : " + str(x))
        numberOfFiles = calculateNumberOfFiles(x, path) - 1
        for y in range (0,numberOfFiles):
            f = open(path + str(x) + "-csves/" + str(y) + ".csv")
            for line in f:
                if counter == 0:
                    if "ts" in line:
                        if flag == 0:
                            line = "References," + line
                            fout.write(line)
                            flag = 1
                    elif "Summary" in line:
                        counter = 2
                    else:
                        line = str(x) + "-csves/" + str(y) + ".csv," + line
                        fout.write(line)
                elif counter == 1 :
                    line = str(x) + "-csves/" + str(y) + ".csv," + line
                    summary.write(line)
                    counter = counter -1

                else :
                    counter = counter-1
            f.close()  # not really needed
    fout.close()
    summary.close()


def calculateNumberOfFiles(numberOfCarpet, myPath):
        f = []
        for (dirpath, dirnames, filenames) in walk(myPath + str(numberOfCarpet) + "-csves/"):
            f.extend(filenames)
            break
        return len(f)

def main():
    start =1
    end = 31
    dataName = "/home/botnets/Documentos/Botnets/PDG/PDG-2/Datasets/Consolidado_Maligno/1-31-allMaligns.csv"
    nameSummary = "/home/botnets/Documentos/Botnets/PDG/PDG-2/Datasets/Consolidado_Maligno/1-31-MalignSummaries.csv"
    path = "/home/botnets/Documentos/Botnets/PDG/PDG-2/Datasets/Malignos/"
    joiningAllCvs(path,start,end,dataName,nameSummary)


main()