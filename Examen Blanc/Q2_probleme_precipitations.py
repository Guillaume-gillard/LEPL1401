# Guillaume Gillard

def rainfall(l):
    """
    pre: l est une liste de nombres, len(l) > 0, l contient un élément 9999.
    post: retourne la moyenne des éléments dans la liste l jusqu'à l'élément 9999
        non compris.  Si des éléments sont négatifs, ils sont traités comme valant 0.
    """

    ### Code to complete [START] ###

    mean = 0
    count = 0
    somme = 0
    for item in l :
        if item == 9999:
            break 
        if item > 0 :
            somme += item 
        count += 1
    mean = somme/count 
    return mean

#### TESTS ####

assert rainfall([100,50,50,250,200,9999]) == 130, "Test 1 failled" # TEST 1

assert rainfall([2, 2]) == 2, "Test 2 failled" # TEST 2

assert rainfall([-1, -3]) == 0, "Test 3 failled" # TEST 3