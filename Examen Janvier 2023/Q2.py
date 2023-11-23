"""
[Q2] C'est un roc... C'est un pic!
Une carte de hauteur est représentée par un tableau à deux dimensions qui contient, pour chaque position (X, Y), une valeur H (la hauteur) correspondante.

image : https://inginious.info.ucl.ac.be/course/LINFO1101-0123/q2/map.png

En Python, ce tableau a la forme d'une liste de listes. Par exemple, la carte illustrée ci-dessus pourrait être représentée par le tableau suivant :

carte = [[2, 3, 1, 3],
         [5, 6, 5, 7],
         [5, 3, 4, 6]]
Dans ce tableau, le pic à la position (X,Y) = (3,1) a une hauteur de carte[1][3] == 7.

Un pic est défini comme une position (X, Y) dont la hauteur est strictement plus grande que celle de toutes ses voisins directs (dans les quatre directions). Dans l'exemple donné, on trouve deux pics:

un pic de hauteur 6 à la position (1, 1) (voisin de (1,0), (0,1), (2,1) et (1,2) de hauteurs respectives 3, 5, 5 et 3, toutes plus petites que 6),
un pic de hauteur 7 à la position (3, 1) (voisin de (3,0), (2,1) et (3,2) de hauteurs respectives 3, 5 et 6, toutes plus petites que 7),
Par contre, il n'y a pas de pic de hauteur 5 à la position (0, 2), car son voisin en (0,1) a une même hauteur de 5.
L'exemple illustre également qu'un pic peut se trouver au bord ou dans un coin du tableau.

Écrivez une fonction Python nombre_pics(tableau) qui prend un tel tableau comme entrée, et qui retourne le nombre de pics trouvés dans la carte de hauteur que représente ce tableau. Vous pouvez supposer que tableau est une matrice rectangulaire, sous forme d'une liste (non vide) de listes (non vides) de tailles identiques, contenant des nombres.

Par exemple, avec un tableau carte tel que défini ci-dessus :

nombre_pics(carte) #Retourne 2  (car carte contient deux pics)
On vous suggère d'implémenter une fonction auxiliaire pour vérifier si une position donnée dans le tableau est un pic.
"""

#Score : 65%

def nombre_pics(tableau):
    """
    pre:  tableau est une matrice rectangulaire non vide de nombres
    post: Retourne le nombre de pics dans le tableau
    """
    r = len(tableau) # row
    c = len(tableau[0]) # column
    count = 0
    for i in range(r) :
        for j in range(c) :
            x = tableau[i][j]
            if r == 1 and c == 1 : # si tableau = [[x]]
                return 1
            elif r == 1 and c > 1 : # si tableau = 1 ligne de plusieur colonnes
                if (i, j) == (r, 0):
                    if tableau[i][j+1] < x :
                        count += 1
                elif (i, j) == (0, c):
                    if tableau[i][j-1] < x:
                        count += 1
                else:
                    try :
                        if (tableau[i][j+1] < x) and (tableau[i][j-1] < x) :
                            count += 1
                    except : 
                        pass
            else :
                if (i, j) == (0, 0) : # si coin sup gauche
                    if (tableau[1][0] < x) and (tableau[0][1] < x):
                        count += 1                
                elif (i, j) == (r, 0) : # coin inf gauche
                    if (tableau[i-1][j] < x) and (tableau[i][j+1] < x):
                        count +=1
                elif (i, j) == (0, c) : # coin sup droit
                    if (tableau[i+1][j] < x) and (tableau[i][j-1] < x) :
                        count += 1
                elif (i, j) == (r, c) : #coin inf droit 
                    if (tableau[i-1][j] < x) and (tableau[i][j-1] < x) :
                        count += 1
                elif (i, j) == (0, j) : # bordure supp
                    if  (tableau[i+1][j] < x) and (tableau[i][j+1] < x) and (tableau[i][j-1] < x) :
                        count += 1
                elif (i, j) == (r, j) : # bordure inf
                    if (tableau[i-1][j] < x) and (tableau[i][j+1] < x) and (tableau[i][j-1] < x) :
                        count += 1
                elif (i, j) == (i, 0) : # bordure gauche
                    try :
                        if (tableau[i+1][j] < x) and (tableau[i-1][j] < x) and (tableau[i][j+1] < x) :
                            count += 1
                    except :
                        pass
                elif (i, j) == (i, c) : # bordure droite
                    if (tableau[i+1][j] < x) and (tableau[i-1][j] < x) and (tableau[i][j-1] < x) :
                        count += 1
                else :
                    try :
                        if (tableau[i+1][j] < x) and (tableau[i-1][j] < x) and (tableau[i][j-1] < x) and (tableau[i][j+1] < x) :
                            count += 1
                    except :
                        pass
    return count

print(nombre_pics([[2,3,1,3]]))    #Imprime 2
print(nombre_pics([[1]]))                              #Imprime 1
print(nombre_pics([[2, 2], [2, 2]]))                   #Imprime 0