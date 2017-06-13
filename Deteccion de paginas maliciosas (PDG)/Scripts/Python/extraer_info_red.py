#!/usr/bin/python
""" Autor: Jose Luis Osorio Quintero
    Universidad Icesi 2017
    Proyecto de grado: Sistema open source para la deteccion de ataques maliciosas a paginas web
    Este script tiene como funcion la abstracion de caracteristicas
    de un trafico de red obtenido del conjunto de urls.
    Toda las caracteristicas obtenidas para el trafico de red son basadas
    en el articulo Cross-Layer Detection of Malicious Websites"""

import pyshark

IP_HONEYPOT = '192.168.1.10'


def read_file(ruta_archivo):
    """ Lee la ruta del archivo pcap de tcpdump """
    capture = pyshark.FileCapture(ruta_archivo)
    return capture


def tcp_conversation_exchange(captura):  # N1
    """ cuenta la cantidad de paquetes que hay para el protocolo asignado """
    pkts = []
    for pkt in captura:
        try:
            if pkt.transport_layer == 'TCP' and pkt.ip.src == IP_HONEYPOT:
                pkts.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print "Error en tcp_conversartion_exchange"
    return pkts


def dist_remote_tcp_port(captura):  # N2
    """ Numero total de puertos distintos a los puertos TCP """
    numero_puertos = 0
    for pkt in captura:
        try:
            if pkt.transport_layer == 'TCP' and pkt.ip.src == IP_HONEYPOT:
                if pkt['TCP'].dstport != '80':
                    numero_puertos = numero_puertos + 1
        except AttributeError:
            pass
        except Exception:
            print 'Error en dist_remote_tcp_port'
    return numero_puertos


def remote_ips(pkts):  # N3
    """ Numero distinto de direcciones IP conectadas al honeypot """
    numero_ips = []
    for pkt in pkts:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                dst_addr = pkt.ip.dst
                if dst_addr != IP_HONEYPOT:
                    if dst_addr not in numero_ips:
                        numero_ips.append(dst_addr)
        except AttributeError:
            pass
        except Exception:
            print 'Error en remote_ips'
    return numero_ips


def pkt_without_dns(captura):
    """ Almacena en un arreglo todo los paquetes que no son DNS"""
    pkts_temp = []
    pkts_dns = []
    for pkt in captura:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                for lyr in pkt.layers:
                    if lyr.layer_name in 'dns':
                        if pkt not in pkts_dns:
                            pkts_dns.append(pkt)
                if pkt not in pkts_dns and pkt not in pkts_temp:
                    pkts_temp.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en pkt_without_dns'
    return pkts_temp


def app_bytes(pkts):  # N4
    """ Numero de bytes de la capa de aplicacion envia por el honeypot
    hacia el sitio web, no se incluyen los datos de los servidores DNS """
    tamanio_pkt = 0
    for pkt in pkts:
        try:
            tamanio_pkt = tamanio_pkt + int(pkt.captured_length)
        except AttributeError:
            pass
        except Exception:
            print 'Error en app_bytes'
    return tamanio_pkt


def udp_packets(pkts):  # N5
    """ Numero de paquetes UDP, no se incluyen los datos de los DNS """
    pkts_temp = []
    for pkt in pkts:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                for lyr in pkt.layers:
                    if lyr.layer_name in 'udp':
                        if pkt not in pkts_temp:
                            pkts_temp.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en udp_packets'
    return pkts_temp


def tcp_urg_packet(captura):  # N6
    """ Numero de paquetes TCP con la bandera de URG """
    pkts_temp = []
    for pkt in captura:
        try:
            if pkt.transport_layer == 'TCP' and pkt.ip.src == IP_HONEYPOT:
                for lyr in pkt.layers:
                    flag_urg = str(lyr.get_field_value('tcp.flags.urg'))
                    if flag_urg not in 'None' and flag_urg not in '0' and pkt not in pkts_temp:
                        pkts_temp.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en tcp_urg_packet'
    return pkts_temp


def source_app_packets(captura):  # N7
    """ Numero de paquetes enviados por el honeypot hacia el servidor remoto """
    pkts = []
    for pkt in captura:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                pkts.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en source_app_packets'
    return pkts


def remote_app_packets(captura):  # N8
    """ Numero de paquetes enviados por el servidor remoto hacia el honeypot """
    pkts = []
    for pkt in captura:
        try:
            if pkt.ip.dst == IP_HONEYPOT:
                pkts.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en remote_app_packets'
    return pkts


def source_app_bytes(captura):  # N9
    """ volumen en bytes de la comunicacion de honeypot a servidor web """
    tamanio_pkt = 0
    for pkt in captura:
        try:
            if pkt.ip.dst == IP_HONEYPOT:
                tamanio_pkt = tamanio_pkt + int(pkt.captured_length)
        except AttributeError:
            pass
        except Exception:
            print 'Error en source_app_bytes'
    return tamanio_pkt


def remote_app_bytes(captura):  # N10
    """ volumen en bytes de la comunicacion del servidor web al honeypot """
    tamanio_pkt = 0
    for pkt in captura:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                tamanio_pkt = tamanio_pkt + int(pkt.captured_length)
        except AttributeError:
            pass
        except Exception:
            print 'Error en remote_app_bytes'
    return tamanio_pkt


def paginas_visitadas(captura):
    """ cantidad de paginas http encontradas por el sniffer"""
    pkts_temp = []
    for pkt in captura:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                for lyr in pkt.layers:
                    if lyr.layer_name in 'http':
                        if pkt not in pkts_temp:
                            pkts_temp.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en paginas_visitadas'
    return pkts_temp


def duration(captura):  # N11
    """ Tiempo de duracion de la pagina web """
    time = 'NA'
    try:
        pkts_http = paginas_visitadas(captura)[0]
        for lyr in pkts_http.layers:
            timestamp = lyr.get_field_value('tcp.options.timestamp.tsval')
            if str(timestamp) not in 'None':
                time = str(timestamp)
    except IndexError:
        pass
    return time


def avg_local_pkt_rate(captura):  # N12
    """ promedio de paquetes IP por segundo N9/N11 """
    time = duration(captura)
    if time not in 'NA':
        resultado = len(source_app_packets(captura)) / float(time)
    else:
        resultado = 'NA'
    return resultado


def avg_remote_pkt_rate(captura):  # N13
    """ promedio de paquetes IP por segundo N10/N11 """
    time = duration(captura)
    if time not in 'NA':
        resultado = len(remote_app_packets(captura)) / float(time)
    else:
        resultado = 'NA'
    return resultado


def app_packets(captura):  # N14
    """ numero de paquetes IP incluidos los del servidor DNS """
    pkts_temp = []
    for pkt in captura:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                for lyr in pkt.layers:
                    if lyr.layer_name in 'ip':
                        if pkt not in pkts_temp:
                            pkts_temp.append(pkt)
        except AttributeError:
            pass
        except Exception:
            print 'Error en app_packets'
    return pkts_temp


def dns_query_times(captura):  # N15
    """ Lista de capas de DNS queries """
    layers_dns = []
    for pkt in captura:
        try:
            if pkt.ip.src == IP_HONEYPOT:
                for lyr in pkt.layers:
                    if lyr.layer_name in 'dns':
                        layers_dns.append(lyr)
        except AttributeError:
            pass
        except Exception:
            print 'Error en dns_query_times'
    return layers_dns


def dns_response_time():  # N16
    """ tiempo de los servidores DNS """
    return 0


def print_conversation_header(pkt):  # Example
    """ Imprime la cabecera de informacion """
    try:
        protocol = pkt.transport_layer
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        print '%s  %s:%s --> %s:%s' % (protocol, src_addr, src_port, dst_addr, dst_port)
    except AttributeError:
        pass
    except Exception:
        print 'Error en print_conversation_header'


def crear_matriz(ruta_datos, ruta_mtx_trans):
    """ Crea una matriz con las caracteristicas de la capa de transporte
    @param ruta_dataset ruta de los dataset a analizar
    @param ruta_matriz ruta del archivo a crear con la matriz de caracteristicas"""

    ruta_trafico = '../../Datasets/Benignos/Trafico/URL_'
    with open(name=ruta_datos, mode='r', buffering=1) as dataset:
        with open(name=ruta_mtx_trans, mode='a+') as matriz:
            for linea in dataset:
                try:
                    id_url = linea.split(';')[0]
                    print 'Extrayendo la url ' + id_url

                    captura = read_file(ruta_trafico + id_url + '.pcap')
                    matriz.writelines(id_url + ';'
                                      + str(len(tcp_conversation_exchange(captura))) + ';'
                                      + str(dist_remote_tcp_port(captura)) + ';'
                                      + str(len(remote_ips(pkt_without_dns(captura)))) + ';'
                                      + str(app_bytes(pkt_without_dns(captura))) + ';'
                                      + str(len(udp_packets(pkt_without_dns(captura)))) + ';'
                                      + str(len(tcp_urg_packet(captura))) + ';'
                                      + str(len(source_app_packets(captura))) + ';'
                                      + str(len(remote_app_packets(captura))) + ';'
                                      + str(source_app_bytes(captura)) + ';'
                                      + str(remote_app_bytes(captura)) + ';'
                                      + str(duration(captura)) + ';'
                                      + str(avg_local_pkt_rate(captura)) + ';'
                                      + str(avg_remote_pkt_rate(captura)) + ';'
                                      + str(len(app_packets(captura))) + ';'
                                      + str(len(dns_query_times(captura))) + '\n')
                    captura.close()
                except Exception, e:
                    print 'Ocurrio un problema en %s --> %s' % (id_url, str(e))



ruta_dataset = '../../Datasets/Benignos/Procesados/urls_convertidas.txt'
ruta_matriz = '../../Datasets/Benignos/matriz_red.csv'
crear_matriz(ruta_dataset, ruta_matriz)
