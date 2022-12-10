# Guillaume Gillard 
# 21/10/2022


### Code to complete [START] ###

def maximum_index(lst):
    max = 0
    for element in lst:
        if element > max:
            max = element
    return(lst.index(max))