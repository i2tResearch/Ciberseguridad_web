import os

def generationOfNpcapsAuto(start,end, locationOfPcaps, locationsToSaveNfpcaps, netflowsLocation):

    for x in range(start, end):
        # Generation of dir that contains the nfpcaps generated with the name of the pcap
        os.chdir(netflowsLocation)
        os.system("mkdir " +  str(x) + "-nfpcaps")

        # Generation nfpcap
        cmd = "nfpcapd -r " + locationOfPcaps + str(x) + ".pcap -l " + locationsToSaveNfpcaps + str(x) + "-nfpcaps/"
        print(cmd)
        os.system(cmd)


def main():
    start = 81
    end = 82
    netflowsLocation = "/home/julioce/Documentos/PDG/PDG-2/Netflows/M/"
    locationOfPcaps = "/home/julioce/Documentos/PDG/PDG-2/PCAPS/M/"
    locationsToSaveNfpcaps = "/home/julioce/Documentos/PDG/PDG-2/Netflows/M/"
    generationOfNpcapsAuto(start,end,locationOfPcaps,locationsToSaveNfpcaps, netflowsLocation)


main()