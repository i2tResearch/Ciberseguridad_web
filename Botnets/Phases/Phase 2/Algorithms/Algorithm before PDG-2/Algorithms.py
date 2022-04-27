import pyshark
import traceback
import pandas as pd
import openpyxl
from pandas import ExcelWriter
from datetime import datetime
import numpy as np

#check
def tcp_urg_pck(pkt):
    retorno =0
    try:
            if pkt.transport_layer == 'TCP':
                sumo = False
                for lyr in pkt.layers:
                    flagUrg = str(lyr.get_field_value('tcp.flags.urg'))
                    if flagUrg not in 'None' and flagUrg not in '0':
                        if sumo == False:
                            retorno += 1
                            sumo = True
    except AttributeError:
            pass
    except Exception:
            print ('Error en tcp_urg_packet')
    return retorno


#not supported
def source_pck(capture):
    print ("-------Mining Source_PCK-------")
    pkts = []
    for pkt in capture:
        try:
            if pkt.ip.src == 'falta la IP a la que se dirigen los pck':
                pkts.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print ('Error en source_app_packets')
    return pkts

#not supported
def remote_pck(capture):
    print ("-------Mining Remote_PCK-------")
    pkts = []
    for pkt in capture:
        try:
            if pkt.ip.dst == 'falta la ip desde donde llegan los pck':
                pkts.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print ('Error en remote_app_packets')
    return pkts

#check
def duration(pkt, firstPkt):
    time = float(pkt.frame_info.time_epoch)  -  float(firstPkt.frame_info.time_epoch)
    converted = time * 1000 #Convert seconds to miliseconds
    return converted

#not supported
def avg_local_pck_rate(capture):
    time = duration(capture)
    if time not in 'NA':
        resultado = len(source_pck(capture)) / float(time)
    else:
        resultado = 'NA'
    return resultado

#not supported
def avg_remote_pck_rate(capture):
    time = duration(capture)
    if time not in 'NA':
        resultado = len(remote_pck(capture)) / float(time)
    else:
        resultado = 'NA'
    return resultado



#check
def dns(pkt):
    sumo = False
    retorno = 0
    for lyr in pkt.layers:
        if lyr.layer_name in 'dns':
            if(sumo == False):
                retorno += 1
                sumo = True
    return retorno


#check
def tcp(pkt):
    retorno = 0
    if pkt.transport_layer == 'TCP':
        retorno += 1

    return retorno

#check
def udp(pkt):
    retorno = 0
    if pkt.transport_layer == 'UDP':
        retorno += 1
    return retorno

#check
def http(pkt):
    sumo = False
    retorno = 0
    for lyr in pkt.layers:
        if lyr.layer_name in 'http':
            if (sumo == False):
                retorno += 1
                sumo = True
    return retorno


def irc(pkt):
    retorno = 0
    if  pkt.transport_layer == 'TCP' and (pkt[pkt.transport_layer].srcport == '6667'
    or pkt[pkt.transport_layer].dstport == '6667'):
        retorno += 1
    return retorno

#check
def bytes(pkt):
    return (float)(pkt.length)

def getSourcePorts(pkt):
    src_port = 0
    try:
        src_port = pkt[pkt.transport_layer].srcport
    except AttributeError:
        pass
    return src_port

def getDestinationPorts(pkt):
    dst_port = 0
    try:
        dst_port = pkt[pkt.transport_layer].dstport
    except AttributeError:
        pass
    return dst_port

def getIPSource(pkt):
    ip = ""
    try:
       # if pkt.ip.src == 'falta la IP a la que se dirigen los pck':
        ip = pkt.ip.src
    except AttributeError:
        pass
    except Exception:
        print ('Error en source_app_packets')

    return ip

def getIPDestination(pkt):
    ip = ""
    try:
        ip =  pkt.ip.dst
    except AttributeError:
        pass
    except Exception:
        print ('Error en source_app_packets')

    return ip

def splitPcapIntoMiniPcaps(pcap):
    pcaps5Minutes = []
    fiveMinutes = 300000
    treeMinutes = 180000
    pktTemp = []
    isFirstPkt = False
    firstPkt = None
    flag = False
    counter = 0
    for pkt in pcap:
        print("Counter : " + str(counter))
        counter+=1
        if (isFirstPkt == False):
            firstPkt = pkt
            isFirstPkt = True
        temp = duration(pkt, firstPkt)
        if (temp > fiveMinutes):
            firstPkt = pkt
            pcaps5Minutes.append(pktTemp)
            pktTemp = []
            pktTemp.append(pkt)
            flag = False
        else:
            pktTemp.append(pkt)
            flag = True

    if (flag == True):
        if (temp > treeMinutes):
            # Agrega si y solo si es mayor a 3 minutos (180000 en milisegundos)
            pcaps5Minutes.append(pktTemp)

    return pcaps5Minutes


def crearMatrizOptimizado(generalRoute,matrizSaveRoute,type):

    "@Param GeneralRoute : Especifica la ruta donde se encuentran los pcaps a analizar ejemplo : Resource/Beningnos/"
    "@Param matrizSaveRoute : Especifica la ruta donde se ira guardando el excel con los datos generados , ejemplo : Resource/BeningDataset"
    "@Param type : 0 si es benigno o 1 si es maligno"
    srcIps = []
    dstIps = []
    srcPorts = []
    dstPorts = []

    namePcap = []
    tcpUrg = []
    mduration= []
    mdns = []
    mtcp = []
    mudp = []
    mbytes= []
    mnumberPck = []
    mtype = []
    mhttp = []
    mirc = []
    comienzo = 183
    fin = 184
    for i in range(comienzo,fin):#Cambiar desde el rango que desea realizar
        print(str(i))
        cap = pyshark.FileCapture(generalRoute + str(i) + '.pcap')  # Mover si es Malignos o Beningnos
        pcaps5Minutes = splitPcapIntoMiniPcaps(cap)
        print("Cantidad de Splits obtenidos : " + str(len(pcaps5Minutes)))
        cap.close()
        for x in range(0,len(pcaps5Minutes)):
            pcap = pcaps5Minutes[x]
            isFirstPkt = False
            tempTcpUrg=0
            tempDuration = 0
            tempDns= 0
            tempTcp= 0
            tempUdp= 0
            tempHttp= 0
            tempBytes= 0
            tempNumberPkt = 0
            tempIrc = 0
            firstPkt = None
            if(len(pcaps5Minutes) > 1):
                namePcap.append("Capture" + str(i)+"."+str(x))
                print("Name PCAP : Capture" + str(i)+"."+str(x))
            else:
                namePcap.append("Capture" + str(i))
                print("Name PCAP : Capture" + str(i))
            for pkt in pcap:
                if (isFirstPkt == False):
                    firstPkt = pkt
                    isFirstPkt = True

                tempTcpUrg += tcp_urg_pck(pkt);
                tempDuration = duration(pkt, firstPkt)
                tempDns += dns(pkt)
                tempTcp += tcp(pkt)
                tempUdp += udp(pkt)
                tempHttp += http(pkt)
                tempBytes += bytes(pkt)
                tempIrc += irc(pkt)
                tempNumberPkt += 1

                if ((getIPSource(pkt) not in srcIps) and (getIPSource(pkt) != "")):
                    srcIps.append(getIPSource(pkt))

                if ((getSourcePorts(pkt) not in srcPorts) and (getSourcePorts(pkt) != 0)):
                    srcPorts.append(getSourcePorts(pkt))

                if ((getIPDestination(pkt) not in dstIps) and (getIPDestination(pkt) != "")):
                    dstIps.append(getIPDestination(pkt))

                if ((getDestinationPorts(pkt)not in dstPorts) and (getDestinationPorts(pkt) != 0)):
                    dstPorts.append(getDestinationPorts(pkt))


            tcpUrg.append(str(tempTcpUrg))
            mduration.append(str(tempDuration))
            mdns.append(str(tempDns))
            mtcp.append(str(tempTcp))
            mudp.append(str(tempUdp))
            mhttp.append(str(tempHttp))
            mbytes.append(str(tempBytes))
            mnumberPck.append(str(tempNumberPkt))
            mirc.append(str(tempIrc))
            mtype.append(type)  # 0 Benignos, 1 Malignos

            df = pd.DataFrame(
                data={"Name PCAP": namePcap,"TCP URG": tcpUrg, "Duration": mduration, "DNS": mdns, "TCP": mtcp, "UDP": mudp, "HTTP": mhttp,
                      "Bytes": mbytes, "Number of Packages": mnumberPck,"IRC": mirc ,"Type": mtype})
            writer = ExcelWriter(matrizSaveRoute + '(' + str(i) + ')' + '.xlsx')
            df.to_excel(writer, 'Hoja de datos', index=False)
            writer.save()

            saveDstIps(dstIps,x,i,type)
            saveDstPorts(dstPorts,x,i,type)
            saveSrcIps(srcIps,x,i,type)
            saveSrcPorts(srcPorts,x,i,type)
            srcIps = []
            dstIps = []
            srcPorts = []
            dstPorts = []



        print("Termino Capture" + str(i))



def saveDstIps(dstIps,x,i,type):

    if type == "0":
        f = open('Datasets/DST_IPs/Benigno_DST_IPs ' + str(i) + "." + str(x) + '.txt', 'w')
    else:
        f = open('Datasets/DST_IPs/Maligno_DST_IPs ' + str(i) + "." + str(x) + '.txt', 'w')
    for i in range(0,len(dstIps)):
        f.write(dstIps[i] + '\n')
    f.close()

def saveDstPorts(dstPorts,x,i,type):
    if type == "0":
        f = open('Datasets/DST_Ports/Benigno_DST_Ports ' + str(i) + "." + str(x) + '.txt', 'w')
    else:
        f = open('Datasets/DST_Ports/Maligno_DST_Ports ' + str(i) + "." + str(x) + '.txt', 'w')

    for i in range(0, len(dstPorts)):
        f.write(dstPorts[i]+ '\n')
    f.close()

def saveSrcIps(srcIps,x,i,type):
    if type == "0":
        f = open('Datasets/SRC_IPs/Benigno_SRC_IPs ' + str(i) + "." + str(x) + '.txt', 'w')
    else:
        f = open('Datasets/SRC_IPs/Maligno_SRC_IPs ' + str(i) + "." + str(x) + '.txt', 'w')

    for i in range(0, len(srcIps)):
        f.write(srcIps[i]+ '\n')
    f.close()

def saveSrcPorts(srcPorts,x,i,type):

    if type == "0":
        f = open('Datasets/SRC_Ports/Benigno_SRC_Ports '+str(i)+"."+  str(x) + '.txt', 'w')
    else:
        f = open('Datasets/SRC_Ports/Maligno_SRC_Ports '+str(i)+"."+  str(x) + '.txt', 'w')
    for i in range(0, len(srcPorts)):
        f.write(srcPorts[i] + '\n')
    f.close()

def loadAndCreateTxtFull(ruta,comienzo, fin,saveRoute):
    datos = []
    for i in range(comienzo,fin):
        ##ruta = DST_IPs/Benigno_DST_IPs
        r = ruta + str(i)+".0.txt"
        print(r)
        datos.append(r+"\n")
        f = open(r, 'r')
        readlines = f.readlines()
        for y in readlines:
            if(y != ""):
                datos.append(y)

    f.close()
    f = open(saveRoute, 'w')
    for m in range(0,len(datos)):
        if(datos[m] != ""):
         f.write(datos[m])
    f.close()

def loadAndGetNumericVariablesExcelWithDataset(route):


    # cargar los data sets
    data = pd.read_excel(route, header=0,sep=';', encoding='utf-8')
    print(data.dtypes)
    print("estructura del data")
    print(data.head(100))

    print("filas y columnas")
    print(data.shape)

    print("Despues de castear a numeric")
    data = data.apply(pd.to_numeric, errors='coerce')
    print(data.head(100))

    print("analisis cuantitativo de los datos")
    print(data.describe(include = 'all'))

    # sns.pairplot(data, hue="C")
    #plt.show()

def loadAndCreateExcelFull(ruta,comienzo,fin,saveRoute,type,indicador):
    nameOfCapture = []
    ips = []
    Type = []
    if (indicador == -1):
        for i in range(comienzo, fin):
            ##ruta = DST_IPs/Benigno_DST_IPs
            r = ruta + str(i) + ".0.txt"
            print(r)
            f = open(r, 'r')
            readlines = f.readlines()
            for y in readlines:
                nameOfCapture.append(r)
                ips.append(y)
                Type.append(type)

        f.close()

    else:
        print("entro al else")
        for i in range(comienzo, fin):
            ##ruta = DST_IPs/Benigno_DST_IPs
            r = ruta + str(indicador) + "."+str(i)+".txt"
            print(r)
            f = open(r, 'r')
            readlines = f.readlines()
            for y in readlines:
                nameOfCapture.append(r)
                ips.append(y)
                Type.append(type)

        f.close()

    df = pd.DataFrame(data={"Name PCAP": nameOfCapture, "Ports": ips, "Type": type})
    writer = ExcelWriter(saveRoute)
    df.to_excel(writer, 'Hoja de datos', index=False)
    writer.save()

#cap = pyshark.FileCapture('Resource/0.pcap', "w")
#print(duration(cap))

#PARA HACER LOS DATASETS

#---
rutaGeneral = 'PCAPS/Benignos/'
rutaSalvado = 'Datasets/Dataset Benigno/Dataset'
#crearMatrizOptimizado(rutaGeneral,rutaSalvado,"0")# o 0 si es benigno
#print('finalize')
#---



#saveRoute = 'Datasets/DST_IPs/Maligno_DST_IPs_FULL.txt'
saveRoute = 'Datasets/DST_Ports/Benigno_DST_Ports_FULL_183.xlsx'
ruta = 'Datasets/DST_Ports/Benigno_DST_Ports '
# ruta, comienzo, fin, ruta salvado, tipo, indicador
loadAndCreateExcelFull(ruta,0,10,saveRoute,0,183)
print("finalize")






#PARA CARGAR LOS DATASETS
#---

rutaDataset = 'Resource/Beningn Dataset.xlsx'
#Resource/Malingn Dataset.xlsx
#loadAndGetNumericVariablesExcelWithDataset(rutaDataset)
#otroMetodo(rutaDataset)
#print('finalize')

#---

