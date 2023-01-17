is_prime = True
n = ...             #Un entier supérieur à 1

### code to complete [START] ###

for div in range(2, n):
    if div != n and n % div == 0:
        is_prime = False 
        break # car si il existe un div qui n'est pas n, n d'office pas premier 