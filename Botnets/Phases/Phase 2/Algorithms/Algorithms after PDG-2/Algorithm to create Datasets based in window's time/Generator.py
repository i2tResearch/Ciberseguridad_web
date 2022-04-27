from os import walk
import operator
import numpy as np


def generator(start,end ,Type, dataname, path_csvs):
    #VARS
    reference = ""
    flag = 0
    counter = 0
    header = "Name,Netflows,First_Protocol,Second_Protocol,Third_Protocol,p1_d,p2_d,p3_d,duration,max_d,min_d,#packets,Avg_bps,Avg_pps,Avg_bpp,#Bytes,#sp,#dp,first_sp,second_sp,third_sp,first_dp,second_dp,third_dp,p1_ip,p2_ip,p3_ip,p1_ib,p2_ib,p3_ib,Type\n"
    fout = open(dataname, "a")

    for x in range(start, end):
         print("va en " + str(x))
         numberOfFiles = calculateNumberOfFiles(x, path_csvs) - 1
         for y in range(0, numberOfFiles):
             netflows = 0
             lduration = []
             protocols = {}
             packets = 0
             avg_bps = 0
             avg_pps = 0
             avg_bpp = 0
             bytes = 0
             sourcePorts = {}
             destinationPorts = {}
             lipkt = []
             libyt = []
             f = open(path_csvs + str(x) + "-csves/" + str(y) + ".csv")
             reference = str(x) + "-csves/" + str(y) + ".csv"
             for line in f:
                 if counter == 0:
                     if "ts" in line:
                         if flag == 0:
                             fout.write(header)
                             flag = 1
                     elif "Summary" in line:
                         counter = 2
                     else:
                        temp = line.split(",")
                        lduration.append(float(temp[2]))
                        lipkt.append(float(temp[11]))
                        libyt.append(float(temp[12]))
                        if temp[5] in sourcePorts:
                            sourcePorts[temp[5]] = sourcePorts[temp[5]] + 1
                        else:
                            sourcePorts[temp[5]] = 1
                        if temp[6] in destinationPorts:
                            destinationPorts[temp[6]] = destinationPorts[temp[6]] + 1
                        else:
                            destinationPorts[temp[6]] = 1
                        if temp[7] in protocols:
                            protocols[temp[7]] = protocols[temp[7]] + 1
                        else:
                            protocols[temp[7]] = 1

                 elif counter == 1:
                     temp = line.split(",")
                     netflows = temp[0]
                     bytes = temp[1]
                     packets = temp[2]
                     avg_bps = temp[3]
                     avg_pps = temp[4]
                     avg_bpp = temp[5].replace("\n","")

                     sourcePorts = sorted(sourcePorts.items(), key=operator.itemgetter(1), reverse=True)
                     destinationPorts = sorted(destinationPorts.items(), key=operator.itemgetter(1), reverse=True)
                     protocols = sorted(protocols.items(), key=operator.itemgetter(1), reverse=True)

                     counter = counter -1

                 else:
                     counter = counter - 1
             f.close()

             duration = np.array(lduration)
             ipkt = np.array(lipkt)  # 11
             ibyt = np.array(libyt)  # 12

             sum_d = str(np.sum(duration, axis=0))
             d_max = str(np.amax(duration))
             d_min = str(np.amin(duration))

             p1_d = str(np.percentile(duration,25))
             p2_d = str(np.percentile(duration,50))
             p3_d = str(np.percentile(duration,75))
             p1_ip = str(np.percentile(ipkt,25))
             p2_ip = str(np.percentile(ipkt,50))
             p3_ip = str(np.percentile(ipkt,75))
             p1_ib = str(np.percentile(ibyt,25))
             p2_ib = str(np.percentile(ibyt,50))
             p3_ib = str(np.percentile(ibyt,75))

             number_sp = str(len(sourcePorts))
             number_dp =  str(len(destinationPorts))

             first_protocol = protocols[0][0]
             second_protocol = ""
             third_protocol = ""
             lg = len(protocols)
             if lg > 1:
                 second_protocol = protocols[1][0]
             if lg > 2:
                 third_protocol = protocols[2][0]


             first_sp = sourcePorts[0][0]
             lg = len(sourcePorts)
             second_sp = ""
             third_sp = ""
             if lg > 1:
                 second_sp = sourcePorts[1][0]
             if lg > 2:
                third_sp= sourcePorts[2][0]

             first_dp = destinationPorts[0][0]
             lg = len(destinationPorts)
             second_dp = ""
             third_dp = ""
             if lg > 1:
                second_dp = destinationPorts[1][0]
             if lg > 2:
                third_dp = destinationPorts[2][0]

             liner = reference +","+ netflows +","+ first_protocol +","+ second_protocol +","+ third_protocol +","+ p1_d+ "," + p2_d + "," + p3_d +","+ sum_d +","+ d_max +","+ d_min +","+packets +","+ avg_bps +","+ avg_pps +","+ avg_bpp +","+bytes +","+ number_sp +","+ number_dp +","+ first_sp + "," + second_sp + "," + third_sp + "," + first_dp + "," + second_dp + "," + third_dp + "," + p1_ip +","+p2_ip +","+ p3_ip +","+ p1_ib +","+ p2_ib +","+ p3_ib + "," + Type + "\n"
             fout.write(liner)
    fout.close()


def calculateNumberOfFiles(numberOfCarpet, myPath):
        f = []
        for (dirpath, dirnames, filenames) in walk(myPath + str(numberOfCarpet) + "-csves/"):
            f.extend(filenames)
            break
        return len(f)

def main():
    start =81
    end = 82
    type = "Malign"
    dataName = "/home/julioce/Documentos/PDG/PDG-2/Datasets/MalignTimeWindows(unb).csv"
    path_csvs = "/home/julioce/Documentos/PDG/PDG-2/Datasets/M/"
    generator(start,end,type,dataName,path_csvs)


main()