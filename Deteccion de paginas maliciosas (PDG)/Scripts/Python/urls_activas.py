#!/usr/bin/python
"""Autor: Jose Luis Osorio Quintero
   Unviersidad Icesi, 2017

   Este script se encarga de verificar si determinada URL sigue aun en funcionamiento,
   para eso parte de un dataset con las URL a examinar, al analizar cada una este las
   guarda en una nuevo dataset de nombre "dataset_#.txt".

   Entrada: "url_#.txt" ejemplo "http://example.com"
   Salida: "dataset_#.txt" si la url sigue en funcionamiento la guarda
   """
from socket import error as SocketError
import subprocess
import urllib2
import errno

def fping(contador, file_dataset):
    """ Identifica si la pagina sigue en funcionamiento usando el comando fping
    que verifica las paginas por el protocolo ICMP
    precondicion: los archivos solo deben tener solo la url y cada una de ellas debe
    contador: ultimo numero que se encuentra en el nombre del archivo
    file_dataset: ruta del arhivo a analizar sin el index
    poscondicion: genera un nuevo archivo con el resultado de las paginas
    """
    cmd = "mkdir " + "dataset_"+ `contador`
    subprocess.call(cmd, shell=True)
    path = "fping_result_"+ `contador`
    cmd = "fping -f" +  file_dataset + " >> " + path + "/fping_result_"+ `contador`+ ".txt"
    subprocess.call(cmd, shell=True)

def is_alive(file_dataset, output_dataset):
    """ Descripcion: identifica si la pagina sigue en funcionamiento usando la libreria urllib2
    consulta si la pagina funciona por el comando http
    contador: es el indice del archivo a examinar
    file_dataset: es la ruta del archivo
    """
    with open(file_dataset, mode='r', buffering=1) as file_urls:
        with open(output_dataset, mode='w') as dataset:
            for url in file_urls:
                try:
                    urllib2.urlopen(url)
                    print url + "is alive"
                    dataset.writelines(url)
                except urllib2.HTTPError, e:
                    print e.code
                except urllib2.URLError, e:
                    print e.args
                except SocketError as e:
                    if e.errno != errno.ECONNRESET:
                        raise # Not error we are looking for
                except:
                    print "Error pagina --> " + url
                print "Fin del dataset..................................."

