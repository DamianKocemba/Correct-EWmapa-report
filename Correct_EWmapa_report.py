# -*- coding: utf-8 -*-

#define parameters
path = "C:\\Users\\damia\\OneDrive\\Pulpit\\Python\\poprawa_raportu_EWmapa\\"
raport = "Raport.txt"           #report file to correction
punkty = "osnowa.txt"           #file with coordinates
raport_ok = "results.txt"       #result file

#list of points - number, X, Y
points_list = []
with open(path+punkty) as file_points:
    for line in file_points:
        line = line.split()
        x, y, nr = line[0], line[1], line[4].replace('"', '')
        points_list.append((nr, "({0},{1})".format(x,y)))

for x in points_list:
    print(x)

#file with results
results = open(path+raport_ok, "w")

#read report file which needs to be corrected
with open(path+raport) as file_raport:
    for line in file_raport:
        #find incorrect line in report file
        if "Linia bazowa: " in line:
            line = line.split()
            coordsP1, coordsP2 = line[3][:-1], line[5]
            #find number from list of numbers - based on coordinates
            for point in points_list:
                if point[1] == coordsP1:
                    P1 = point[0]
                    line[2]= "P1: {0}".format(P1)
                if point[1] == coordsP2:
                    P2 = point[0]
                    line[4] = "P2: {0}".format(P2)
            line = ' '.join(str(elem) for elem in line)+"\n"
        results.write(line)
results.close()

