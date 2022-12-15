# Guillaume Gillard
# 09/11/2022

### Code to complete [START] ###

def treatment(data):
    data = data.split(" ")
    output = " "
    k = 1
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            k += 1
        else :
            output += data[i] + "*" + str(k) + " "
            k = 1
    output += data[-1] + "*" + str(k)
    return output