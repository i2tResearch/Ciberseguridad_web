"""Autor: Jose Luis Osorio Quintero
   Unviersidad Icesi, 2017"""


def convert_dataset(archivo_entrada, archivo_salida, contador):
    """ Agrega un identificador a las urls que hay en el dataset, el identificador,
        es un numero que va en incremento"""
    number = 0
    with open(archivo_entrada, mode='r', buffering=1) as file_urls:
        with open(archivo_salida, mode='w') as dataset:
            for line in file_urls:
                number = number + 1
                dataset.writelines("D" + `contador` + "_" +
                                   `number` + ";" + line)


def only_domain(archivo_entrada, archivo_salida):
    """ Extrae un solo dominio por url """
    temp = ''
    with open(archivo_entrada, mode='r', buffering=1) as file_urls:
        with open(archivo_salida, mode='w') as dataset:
            for url in file_urls:
                domain = url.split('/')[2]
                if domain != temp:
                    print domain
                    temp = domain
                    dataset.writelines(url)


def counter_domain(primera_entrada, segunda_entrada, archivo_salida):
    """ cuenta cuantos subdominios tiene un determinado dominio """
    counter = 0
    with open(primera_entrada, mode='r', buffering=1) as format_urls:
        with open(segunda_entrada, mode='r', buffering=1) as file_urls:
            with open(archivo_salida, mode='w') as dataset:
                for url_format in format_urls:
                    domain_format = url_format.split('/')[2]
                    for url in file_urls:
                        domain = url.split('/')[2]
                        if domain_format == domain:
                            counter = counter + 1
                            print `counter` + " --> " + domain_format
                        else:
                            dataset.writelines(`counter`+ ";" + url_format)
                            counter = 0

"""
path = ""
namefile = ""
for index in range(0,5):
	input_path = "../recursos/dataset_"+ `index` + ".txt" 
	output_path = "../recursos/format_dataset"+ `index` + ".txt" 
	counter_path = "../recursos/conteo_dataset"+ `index` + ".txt"
	convert_path  = "../recursos/convert_dataset" + `index` + ".txt"
	only_domain(input_path,output_path)
	counter_domain(output_path,input_path,counter_path)
"""
