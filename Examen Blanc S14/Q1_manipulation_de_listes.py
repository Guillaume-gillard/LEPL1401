# Guillaume Gillard
# 19/12/2022


### Code to complete [START] ###

def mix(l):    
    """
    @pre:    l est une liste d'entiers
            la taille n de cette liste est un nombre pair
    @post:   retourne une liste r d'entiers
            la liste retournée r a la même taille n
            pour chaque index 0 ≤ i < n où i est pair on a la
            correspondance suivante entre les deux listes :
                r[i] = l[i//2]
                r[i+1] = l[n-1-(i//2)]
    """
    r = []
    n = len(l)
    for i in range(0, n, 2):
        if i == n-1 :
            r.append(l[i//2])
            break
        r.append(l[i//2])
        r.append(l[n-1-(i//2)])
    return r

##### TESTS ######

assert mix([1, 2, 3, 4]) == [1, 4, 2, 3], "Test 1 failled"  # TEST 1