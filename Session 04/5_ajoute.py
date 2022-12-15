# Guillaume Gillard
# 21/10/2022


### Code to complete [START] ###

def ajoute(l, v):
    for element in l:
        if v not in l:
            l.append(v)
    return(l)