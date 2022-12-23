# Guillaume Gillard
# 23/12/2022

### Code to complete [START] ###

### Question 1: Ecriture de coordonnées ###

def write_coordinates(filename, l):
    with open(filename, "w") as file :
        for i in range(len(l)):
            file.write(str(l[i][0]) + "," + str(l[i][1]) + "\n")

### Question 2: Lecture de coordonnées ###

def read_coordinates(filename):
    with open(filename, "r") as file:
        l = []
        for line in file :
            info = line.split(",")
            l.append((float(info[0]), float(info[1])))
        return l