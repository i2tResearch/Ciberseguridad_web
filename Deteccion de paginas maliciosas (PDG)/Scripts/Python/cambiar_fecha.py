import datetime
with open('../../Datasets/Malignos/matrizAplicacion.csv', mode='r', buffering=1) as matriz:
    with open('../../Datasets/Malignos/matriz_arreglada.csv', mode='w') as matriz_arreglada:
        for line in matriz:
            arr = line.split(';')
            cadena = ''
            for i in range(0, len(arr)):
                if i == 6:
                    whois = arr[6].split('datetime.datetime')
                    whois_arreglado = arr[6]
                    if  len(whois) > 2:
                        temp = whois[1]
                        temp = temp[:-8]
                        whois_arreglado = str(temp.replace(',', '/').split('(')[1])
                    cadena = cadena + whois_arreglado + ';'
                elif i == 7:
                    update = arr[7].split('datetime.datetime')
                    update_arreglado = arr[7]
                    if  len(update) > 1:
                        temp = update[1]
                        temp = temp[:-8]
                        update_arreglado = str(temp.replace(',', '/').split('(')[1])
                    #print update[0]
                    cadena = cadena + update_arreglado + ';'
                else:
                    cadena = cadena + arr[i] + ';'
            matriz_arreglada.writelines(cadena[:-2])
