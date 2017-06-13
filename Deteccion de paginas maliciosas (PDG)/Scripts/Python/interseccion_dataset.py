def intersecion(ruta_1, ruta_2, archivo_red, archivo_app):
    with open(ruta_1, mode='r', buffering=1) as app:
        with open(ruta_2, mode='r', buffering=1) as red:
            with open(archivo_app, mode='w', buffering=1) as salida_app:
                with open(archivo_red, mode='w', buffering=1) as salida_red:
                    for line_app in app:
                        id_app = line_app.split(';')[0]
                        print id_app
                        for line_red in red:
                            id_red = line_red.split(';')[0]
                            print id_app + ' ----------------------- ' + id_red
                            if id_app == id_red:
                               # salida_app.writelines(line_app)
                               # print id_red + ' -- ' + id_app
                                salida_red.writelines(line_red)


RUTA_RED = '../../Datasets/Benignos/matriz_red_benigno.csv'
RUTA_APP = '../../Datasets/Benignos/matriz_app_benigno.csv'
SALIDA_RED = '../../Datasets/Benignos/mrb.csv'
SALIDAD_APP = '../../Datasets/Benignos/mab.csv'
intersecion(RUTA_APP,RUTA_RED,SALIDA_RED,SALIDAD_APP)