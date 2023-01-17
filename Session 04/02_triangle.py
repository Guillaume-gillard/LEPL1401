### Code to complete [START] ###

def triangle(n):
    l = []
    for i in range(n+1):
        s = []
        for x in range(i+1):
            s.append(x)
        l.append(s)
    return(l)