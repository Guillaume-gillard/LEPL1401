### Code to complete [START] ###

def merge(first_list, second_list):
    l = first_list.copy()
    for x, y in second_list :
        for i in range(len(l)):
            if y <= l[i][1] :
                l.insert(i, [x, y])
                break
    return l          