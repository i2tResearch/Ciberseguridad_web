"""This module provide tools to transform pcaps into nfpcaps and delete them"""
from . import CommonTools
import os



def nfpcapGenerator(locationToSaveNfpcaps, pcapLocation, pcapName):
    print("::::::::::::::::::::::::::::")
    print(":::: TRANSFORMING... ::::")
    print("::::::::::::::::::::::::::::")
    cmd = "nfpcapd -r " + pcapLocation + pcapName + " -l " + locationToSaveNfpcaps
    os.system(cmd)



def renameNfpcaps(location):
    print("::::::::::::::::::::::::::::")
    print(":::: RENAMING... ::::")
    print("::::::::::::::::::::::::::::")
    f = CommonTools.getFilesOfSpecificLocation(location)
    y = 0
    for x in f:
        os.rename(location + x,location + "nfcapd." + str(y))
        y = y+1




def deleteNFpcaps(location):
    cmd = "rm " + location + "*"
    os.system(cmd)