import random
data = []

#Divide un archivo de url de forma random, en diferentes archivos
def fileRead():
    file = open("moderna_procesada.txt","r")
    j = 0
    x = 0
    for i in file.readlines():
        i = i.replace('\n','')
        data.append(i)
    random.shuffle(data)

    for i in data:
        if j % 1000 == 0 and j!=0:
            x = x+1
            print(f"/----- file{x}finish -----/")
        file_save = open(f"data{x}.txt",'a')
        file_save.write(i+'\n')
        file_save.close()
        j = j+1
        

def main():
    fileRead()
main()