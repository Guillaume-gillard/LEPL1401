# Guillaume Gillard

def plus_frequent(l):
    """
    pre: `l` est une liste, len(l) > 0
    post: retourne l'élément qui se trouve le plus grand nombre de fois
        dans la liste `l` (nombre d'ocurrences égales au sens de ==).  Si
        plusieurs éléments différents apparaissent un plus grand nombre égal
        de fois, retourne le premier apparaissant dans la liste.
    """

    #### Code to complete [START] ####

    count = 0
    best = None
    for item in l :
        best_prev = count
        count = l.count(item)
        if best_prev < count :
            best = item 
    return best

#### TESTS ####

assert plus_frequent([1,2,3,1,2,2]) == 2, "Test 1 failled" # TEST 1
assert plus_frequent([1,1,2,2,2,1,3,3,3,3,4,3]) == 3, "Test 2 failled" # TEST 2
assert plus_frequent([1,2]) == 1, "Test 3 failled" # TEST 3