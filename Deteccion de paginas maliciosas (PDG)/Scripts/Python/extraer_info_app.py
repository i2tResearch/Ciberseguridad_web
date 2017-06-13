"""
Autores: Melisa Garcia P. y Jose Luis Osorio Q.
Proyecto de grado: Sistema open source para la deteccion de ataques en paginas web maliciosas
Universidad Icesi, 2017
"""
import datetime
from cachecontrol import CacheControl
import whois
import requests



def longitud_url(url):
    """ Determina la longitud de la url
    url: es la direccion de la pagina web """
    return len(str(url))


def numero_caracteres_especiales(url):
    """ Cuenta la cantidad de caracteres especiales que hay en la url
    url: es la direccion de la pagina web """
    try:
        # cuantas letras hay por linea
        contador_alfabeto = sum(1 for c in url if c.isalpha())
        # cuantos numero hay por linea
        contador_digitos = sum(1 for c in url if c.isdigit())
        caracteres_alfanumericos = contador_digitos + contador_alfabeto
        longitud = len(str(url))  # longitud de la linea
        caracteres_especiales = longitud - caracteres_alfanumericos
    except Exception:
        caracteres_especiales = -1
    return caracteres_especiales


def presencia_direccion_ip(url):
    """ Determina la si la url no tiene un nombre de dominio
    url: es la direccion de la pagina web """
    return url


# https://media.readthedocs.org/pdf/requests-docs-es/latest/requests-docs-es.pdf
def chartset(request):
    """ Conjunto de caracteres que determian la pagina
    request: respuesta de la url"""
    try:
        charset = request.encoding
    except AttributeError as error_atributo:
        charset = "NA"
        print "charset: " + str(error_atributo)
    return charset


def nombre_servidor_web(request):
    """ Nombre del servidor web donde esta alojada la pagina"""
    try:
        cabecera = request.headers
        server = cabecera.get("server")
    except AttributeError as error_atributo:
        server = "NA"
        print "nombre_servidor_web: " + str(error_atributo)
    return server


def http_header_control_cache(request):
    """ Tipo de control de cache
    url: direccion de la pagina web"""
    try:
        cabecera = request.headers
        cache_control = cabecera.get("cache-control")
    except Exception:
        cache_control = "NA"
        print "Error inesperado en la %s no se encontro cache_control" % (url)
    return cache_control


def http_header_content_length(request):
    """ longitud del contenido de la cabecera http de la pagina web
    url: direccion de la pagina web"""
    try:
        cabecera = request.headers
        content_length = cabecera.get("content-length")
    except Exception:
        content_length = "NA"
        print "Error inesperado en la %s no se encontro content_length en la cabecera" % (url)
    return content_length


def whois_reg_date(whois):
    """ Fecha en la que fue registrado el sitio"""
    reg_date = []
    try:
        reg_date = whois.creation_date
        if reg_date != None:
            if isinstance(reg_date, datetime.date):
                reg_date = reg_date
            elif len(reg_date) > 1:
                reg_date = reg_date[0]
    except AttributeError as error_atributo:
        reg_date = "NA"
        print "whois_reg_date: " + str(error_atributo)
    return reg_date


def whois_update_date(whois):
    """ Fecha en la que fue actualizado el sitio
    url: direccion de la pagina web"""
    try:
        update = whois.updated_date
        if update != None:
            if isinstance(update, datetime.date):
                update = update
            elif len(update) > 1:
                update = update[0]
    except AttributeError as error_atributo:
        update = "NA"
        print "whois_update_date: " + str(error_atributo)
    return update

def whois_country(whois):
    """ nombre del pais donde proviene el servicio web
    url: direccion de la pagina web"""
    try:
        country = whois.country
    except AttributeError as error_atributo:
        country = "NA"
        print 'whois_country: ' + str(error_atributo)
    return country


def whois_state_prov(whois):
    """ continente donde proviene el sitio web
    url: direccion del sitio web"""
    try:
        state_prov = whois.state
    except AttributeError as error_atributo:
        state_prov = "NA"
        print "whois_state_prov: " + str(error_atributo)
    return state_prov


def within_domain(whois):
    """ Nombre del dominio de la url
    url: direccion de la pagina web"""
    try:
        domain = whois.domain
    except AttributeError as error_atributo:
        domain = "NA"
        print "within_domain: " + str(error_atributo)

    return domain


def creacion_matriz_aplicacion(ruta_dataset, ruta_matriz_app):
    """ Se encarga de crear una metriz con las caracteristicas de aplicacion """
    with open(name=ruta_dataset, mode='r', buffering=1) as dataset:
        with open(name=ruta_matriz_app, mode='a+') as matriz_app:
            for linea in dataset:
                try:
                    contenido = linea.split(';')
                    id_url = contenido[0]
                    print "##################### Examinando %s ########################" % (id_url)
                    url = contenido[1]
                    request = requests.get(url)
                    details = whois.whois(url)
                    matriz_app.writelines(id_url + ';'
                                          + str(longitud_url(url)) + ';'
                                          + str(numero_caracteres_especiales(url)) + ';'
                                          + str(chartset(request)) + ';'
                                          + str(nombre_servidor_web(request)) + ';'
                                          + str(http_header_control_cache(request)) + ';'
                                          + str(http_header_content_length(request)) + ';'
                                          + str(whois_country(details)) + ';'
                                          + str(whois_state_prov(details)) + ';'
                                          + str(whois_reg_date(details)) + ';'
                                          + str(whois_update_date(details)) + ';'
                                          + str(within_domain(details)) + '\n')
                except Exception, e:
                    print e

RUTA_DATASET = '../../Datasets/Benignos/Procesados/urls_convertidas_5.txt'
RUTA_MATRIZ = '../../Datasets/Benignos/matriz_app_5.csv'
creacion_matriz_aplicacion(RUTA_DATASET, RUTA_MATRIZ)

"""
URL = "http://kuglu.mymag250.co.uk/oluleestos/natseglird/eseersoarg/files/"
REQUEST = requests.get(URL)
DETAILS = whois.whois(URL)
SALIDA = str(longitud_url(URL)) + \
    ';' + str(numero_caracteres_especiales(URL)) + \
    ';' + str(chartset(REQUEST)) + \
    ';' + str(nombre_servidor_web(REQUEST)) + \
    ';' + str(http_header_control_cache(REQUEST)) + \
    ';' + str(http_header_content_length(REQUEST)) + \
    ';' + str(whois_country(DETAILS)) + \
    ';' + str(whois_state_prov(DETAILS)) + \
    ';' + str(whois_reg_date(DETAILS)) + \
    ';' + str(whois_update_date(DETAILS)) + \
    ';' + str(within_domain(DETAILS)) + '\n'
print SALIDA
"""
