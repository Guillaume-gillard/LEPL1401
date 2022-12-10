# Guillaume Gillard
# 02/11/2022 


### Code to complete [START] ###

def gcd(a, b):
    if a > b :
        big = a
    else :
        big = b
    for div in range(1, big+1):
        if a % div == 0 and b % div == 0:
            gcd = div
    return gcd