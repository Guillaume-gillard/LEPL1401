# Guillaume Gillard
# 14/10/2022

def interests(base, y, x):

    ### Code to complete [START] ###

    new_base = base
    for year in range(x):
        new_base = new_base * (1+y/100)
    return(new_base)
