# Guillaume Gillard 
# 21/12/2022

#### Code to complete [START] ####

def marks_from_file(filename):
    with open(filename, "r") as file :
        l = []
        for line in file :
            info = line.split(" ")
            l.append(Student(info[0] , info[1], int(info[2])))
        return l