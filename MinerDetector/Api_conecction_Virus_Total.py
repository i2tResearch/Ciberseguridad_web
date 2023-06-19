import os
import requests
import time

URL_SCAN = 'https://www.virustotal.com/vtapi/v2/url/scan'
URL_REPORT = 'https://www.virustotal.com/vtapi/v2/url/report'
URL_MALIGN = []
URL_BENIGN = []
FILE_BENIGN = ""
FILE_MALIGN = ""

# Lee los archivos
def fileRead():
    file = open('/home/steven/Documents/GestorCapture/s/data_status/UrlActivas.txt',"r")
    j = 0
    for i in file.readlines():
        try:
            if i != 0:
                time.sleep(35)
            if j%4 == 0 and i!=0:
                time.sleep(65)
                conection(i)
            else:
                conection(i)
                j+=1
        except:
            dataNo = open("/home/steven/Documents/GestorCapture/s/data_virus_Total/urlNoescanead.txt","a")
            dataNo.write(i)
            dataNo.close()
            pass
      
#Tienes que poner tu api key de Virus Total
def conection(url):
    params = {'apikey': 'eff112509d99ba0ef88682356a0c1f134cb973310a6d3512e9ff13a04437b3f5', 'url':'{}'.format(url)}
    response = urlScan(params)
    params = {'apikey': 'eff112509d99ba0ef88682356a0c1f134cb973310a6d3512e9ff13a04437b3f5', 'resource':'{}'.format(response['scan_id'])}
    response = getReport(params)
    urlIdentification(response)

#Escanesa la url para saber si es benigna o no
def urlScan(params):
    response = requests.post(URL_SCAN, data=params)
    print(response.json())
    return response.json()

# Pides los parametros de la url
def getReport(params):
    response = requests.get(URL_REPORT, params=params)
    return response.json()

#Archivos para guardas
def urlIdentification(response):
    if response['positives']>0:
        print(response['url'])
        FILE_MALIGN = open("/home/steven/Documents/GestorCapture/s/data_virus_Total/urlMalignas.txt","a")
        FILE_MALIGN.write(response['url']+"\n")
        URL_MALIGN.append(str(response['url']))
    else:
        FILE_BENIGN = open("/home/steven/Documents/GestorCapture/s/data_virus_Total/urlBenignas.txt","a")
        FILE_BENIGN.write(response['url']+"\n")
        URL_BENIGN.append(str(response['url']))
#Abre el archivos
def uploadFile():
    FILE_MALIGN = open("urlMalignas.txt","r")
    FILE_BENIGN = open("urlBenignas.txt","r")
    print(FILE_MALIGN,FILE_BENIGN)

def execute():
    #uploadFile()
    fileRead()
    print(URL_MALIGN)
    print(URL_BENIGN)

if __name__ == '__main__':
    execute()
