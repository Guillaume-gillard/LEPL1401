a_list = ... #list to sort
sorted_list = ... #store in this variable the sorted version of the list

### Code to complete [START] ###

def sorting(a_list):
    tri = [a_list[0]]
    for x in a_list[1:]:
        if x < tri[0]:
            tri = [x] + tri
        elif x >= tri[len(tri)-1]:
            tri += [x]
        else :
            for place in range(len(tri)):
                if tri[place] <= x and x <= tri[place+1]:
                    tri = tri[:place+1] + [x] + tri[place+1:]
                    break
    return tri
              
sorted_list = sorting(a_list)
            