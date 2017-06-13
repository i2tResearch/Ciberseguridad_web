#!/usr/bin/python
""" Autor:  Jose Luis Osorio Quintero
    Universidad Icesi 2017
    Este script tiene como funcion la obtencion del trafico de red
    de un conjunto de urls, tambien se obtiene informacion de la
    capa de aplicacion """
import subprocess
import re

def examinate_with_thug(ruta):
    """ Examina un archivo de url por medio de un honeypot
    @param ruta ruta del archivo que contiene las urls """
    with open(ruta) as file_urls:
        for line in file_urls:
            url = re.compile(";").split(line)
            if len(url) >= 2:
                try:
                    print "Examinane " + url[1] + " into " + url[0]
                    sniffer(4, "../trafico/URL_" + url[0])
                    cmd = "thug -n" + url[0] + " " + url[1]
                    subprocess.call(cmd, shell=True)
                except Exception, e:
                    print "Error for " + url[1] + ": " + str(e)


def sniffer(tiempo, nombre_archivo):
    """ Hace la captura de trafico por medio de tcpdump
    @param tiempo tiempo en segundos que se dejara ejecutando el sniffer
    @param nombre_archivo ruta donde se guardara el arcivo pcap del sniffer """
    cmd = "tcpdump -G " + `tiempo` +" -W 1 -w " + \
        nombre_archivo + ".pcap -i enp0s3 &"
    subprocess.call(cmd, shell=True)
