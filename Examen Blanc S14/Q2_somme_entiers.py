# Guillaume Gillard 
# 19/12/2022

### Code to complete [START] ###

def combien(n):    
    """
    @pre:  n est un nombre entier > 0
    @post: retourne le nombre de series d’entiers consecutifs
           strictement positifs dont la somme est egale a n
    """
    count = 0
    for i in range(1, n+1):
        sum = 0
        for x in range(i, n+1):
            sum += x
            if sum == n :
                count += 1
                break
            if sum > n :
                break
    return count

#### TESTS ######

assert combien(100) == 3, "test 1 failled"  # TEST 1
assert combien(5) == 2, "test 2 failled"    # TEST 2
assert combien(0) == 0, "test 3 failled"    # TEST 3 
assert combien(1) == 1, "test 4 failled"    # TEST 4
