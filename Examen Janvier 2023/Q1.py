"""
[Q1] Deux fois trois égale six
Les nombres entiers peuvent se décomposer en produit de deux nombres. Par exemple, 8 = 1 * 8 = 2 * 4, 12 = 1 * 12 = 3 * 4 = 2 * 6, et le nombre 30 peut se décomposer en :

30 = 1 * 30 = 30 * 1
30 = 2 * 15 = 15 * 2
30 = 3 * 10 = 10 * 3
30 = 5 * 6 = 6 * 5
Écrivez une fonction multiplications(n) qui compte le nombre de décompositions différentes pour un nombre donné n en une multiplication a*b. On ne compte chaque décomposition n = a*b = b*a qu'une seule fois.

Par exemple :

multiplications(5) renvoie 1 (la décomposition 1*5 = 5*1 n'est comptée qu'une fois),
multiplications(30) renvoie 4 (pour les décompositions 1*30, 2*15, 3*10 et 5*6),
multiplications(60) renvoie 6 (pour les décompositions 1*60, 2*30, 3*20, 4*15, 5*12 et 6*10) et
multiplications(4) renvoie 2 (pour la décomposition 1*4 et 2*2).
"""

# SCORE : 100%

def multiplications(n):
    """
    pre:  n est un nombre entier positif
    post: Retourne le nombre de décompositions a,b distinctes
          telles que n == a*b == b*a
    """
    count = 0 
    for i in range(1, n+1):
        if n % i == 0 :
            for j in range(1, n+1):
                if n % j == 0 and i*j == n :
                    if i == j :
                        count += 1
                    count += 1  
    return count//2

## TEst ## 

### Test 1 ###
assert multiplications(30) == 4, "Test 1 failed !"
### Test 2 ###
assert multiplications(5) == 1, "Test 2 failed !"
### Test 3 ###
assert multiplications(60) == 6, "Test 3 failed !"
### Test 4 ###
assert multiplications(15) == 2, "Test 4 failed !"
### Test 5 ###
assert multiplications(4) == 2, "Test 5 failed !"