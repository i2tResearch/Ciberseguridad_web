from __future__ import print_function
import os


#Aqui debe ir la ruta de la carpeta donde se encuentran los .pcap
path = ' '

files = os.listdir(path)
file = open(path+'rutas.txt', "w")

for name in files:

    file.write(path+name+'\n')

file.close()
