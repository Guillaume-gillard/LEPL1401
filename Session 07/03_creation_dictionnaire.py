### Code to complete [START] ###

def create_dict(l):
    d = {}
    for x, y in l :
        found = False
        for key in d:
            if x == key :
                found = True
        if found :
            d[x] += [y]
        else :
            d[x] = [y]
    return d