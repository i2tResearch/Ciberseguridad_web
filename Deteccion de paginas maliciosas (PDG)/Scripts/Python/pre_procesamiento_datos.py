from urls_activas import is_alive
""" importa el script que determina si una url esta activa"""
from procesar_urls import convert_dataset
from examinar_urls import examinate_with_thug

RUTA_IS_ALIVE = '../urls_vivas.txt'
RUTA_DATASET_CONVERT = '../urls_convertidas.txt'

def procesamiento_dataset(ruta, contador):
    """ Se encarga de pre procesar cada una de las urls hasta obtener el
    trafico de red que mas adelante servira para extrer las caracteristicas """
    print 'Ejecutando scripts de urls_activas...'
    is_alive(ruta, RUTA_IS_ALIVE) # verifica que las url estan vivas
    print '------ finalizacion de proceso url activas ------------- \n'
    convert_dataset(RUTA_IS_ALIVE, RUTA_DATASET_CONVERT, contador)
    print 'Se agrego un identificador a las urls... \n'
    print 'Iniciando honeypot y sniffer'
    examinate_with_thug(RUTA_DATASET_CONVERT)
    print 'Finalizacion de captura de trafico...'
