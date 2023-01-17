def solution(a, b, c):
    """
    pre:  a, b et c sont 3 nombres réels
    post: la valeur de retour de cette fonction dépend du nombre
          de solutions de l'équation ax^2 + bx + c = 0.
    - 0 solution: retourne la liste vide
    - 1 solution: retourne une liste contenant la solution de l'équation
    - 2 solutions: retourne une liste contenant les deux solutions,
                  la plus petite solution en première place
    """
    pass

### Code to complete [START] ###

def solveur(eq_list):
    sol = []
    for eq in eq_list:
        a = eq[0]
        b = eq[1]
        c = eq[2]
        sol.append(solution(a, b, c))
    return sol