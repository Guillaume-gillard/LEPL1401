# Guillaume Gillard
# 09/11/2022


def racine_carree(n):
    """
    Calcule une racine carree
    pre: n est un nombre réel
         n >= 0
    post: retourne la racine carrée réelle de n
    """


### Code to complete [START] ###


def rho(a,b,c):
    delta = (b**2)-4*a*c
    return(delta)


def n_solutions(a, b, c):
    if rho(a, b, c) < 0 :
        return 0
    elif rho(a, b, c) == 0:
        return 1
    return 2


def solution(a, b, c):
    if rho(a, b, c) == 0:
        sol = -b/(2*a)
        return(sol)
    else :
        x1 = (-b-racine_carree(rho(a, b, c)))/(2*a)
        x2 = (-b+racine_carree(rho(a, b, c)))/(2*a)
        if x1 < x2:
            return x1
        return x2