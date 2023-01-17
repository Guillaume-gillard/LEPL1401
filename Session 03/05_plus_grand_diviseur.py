def greatest_divisor(a):

    ### Code to complete [START] ###

    div_1 = 1
    div_2 = 1

    for div in range(2, a+1):
        div_2 = div_1
        if a % div == 0:
            div_1 = div
        if a == div:
            return(div_2)