# Guillaume Gillard
# 09/11/2022

### Code to complete [START] ###

def binary_search ( name, list_of_names ):
    first = 0
    last = len(list_of_names)-1
    found = False

    while first<=last and not found:
        middle = (first + last)//2
        if list_of_names[middle] == name:
            found = True
        else:
            if name < list_of_names[middle]:
                last = middle-1
            else:
                first = middle+1

    return found