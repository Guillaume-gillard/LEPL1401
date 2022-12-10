# Guillaume Gillard
# 28/10/2022

### Code to complete [START] ###

def count(events, i, j):
    coord = (i,j)
    count = 0
    for x in events :
        if coord == x :
            count += 1
    return count