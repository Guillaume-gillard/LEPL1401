# Guillaume Gillard
# 21/10/2022

def average(list):

    ### Code to complete [START] ###
    average = 0
    count = 0
    if len(list) == 0 :
        return(None)
    for element in list:
        average += element
        count +=1
    return(average/count)
