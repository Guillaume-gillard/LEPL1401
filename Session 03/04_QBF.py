### Code to complete [START] ###

def chiffres_pairs(n):
    count = 0
    while n != 0 :
        n = n // 10
        count += 1
    if count % 2 == 0 and count != 0: #si n = 0 => count = 0 et 0%2 = 0 alors que 0 a un nbr impair de chiffres
        return(True)
    else :
        return False