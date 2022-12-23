# Guillaume Gillard
# 23/12/2022

### Code to complete [START] ###

def equal(l, d):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != d.get((i, j), 0) : #get method get the value at the specified key if there is no value it return the value we set here 0
                return False
    return True