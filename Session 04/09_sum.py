def sum(list):

### Code to complete [START] ###

    sum = 0
    for i in list :
        try  :
            if float(i) :
                sum += i
        except :
            pass
    return(sum)
