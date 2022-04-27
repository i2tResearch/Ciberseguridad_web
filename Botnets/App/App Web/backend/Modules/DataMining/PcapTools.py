"""This module provide tools to generate and delete pcaps"""
import pyshark
import os
from scapy.sendrecv import sniff
from scapy.utils import wrpcap


def pcapGenerator(location, timeout=60, packets=5000):
    #capture = pyshark.LiveCapture(interface="any", output_file=location)
    #capture.sniff(timeout=timeout) #seconds
    print("::::::::::::::::::::::::::::")
    print(":::: MINING... ::::")
    print("::::::::::::::::::::::::::::")
    pckts = sniff(count=packets)
    wrpcap(location,pckts)



def deletePcapFIle(location):
    cmd = "rm " + location
    os.system(cmd)


