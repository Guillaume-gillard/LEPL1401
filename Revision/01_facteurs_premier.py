### Code to complete [START] ###
def is_prime(n) :
    """
    Pre:  n est un entier strictement positif
    Post : return True si n est un nombre premier False sinon
    """
    if n <= 1 :
        return False 
    for i in [j for j in range(2, n)] :
        if n % i == 0 :
            return False
    return True 


def facteurs(n):
    """
    Pre:  n est un entier strictement positif
    Post: retourne un entier représentant le nombre de facteurs premiers de n
    """
    count = 0
    for i in [j for j in range(1, n+1)]:
        if is_prime(i):
            while n % i == 0:
                n = n / i
                count += 1 
    return count 