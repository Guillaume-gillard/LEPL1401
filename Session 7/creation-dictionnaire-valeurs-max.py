# Guillaume Gillard 
# 15/11/2022


### Code to complete [START] ###

def create_dict_max(l):
    d = {}
    for x, y in l :
        found = False
        big = False
        for key, value in d.items():
            if x == key:
                found = True
                if y > value :
                    big = True
        if found and big or not found:
            d[x] = y
    return d