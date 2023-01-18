def load_matrix(filename):
    """
    pre: `filename` est un nom de fichier
    post: retourne une matrice rectangulaire M x N dont le contenu est donné
        dans le fichier `filename`.

    le format du fichier est :
        première ligne : le nombre de lignes M
        deuxième ligne : le nombre de colonnes N
        lignes suivantes : une ligne par élément au format "I,J VAL"
            où 0 <= I < M et 0 <= J < N
            et VAL est le réel en ligne I et colonne J de la matrice

    Les éléments non repris dans le fichier sont initialisés à 0.0.

    En cas d'erreur (exception d'entrée/sortie, fichier non lisible,
    mauvais format) retourne None.
    """
    ### Code to complete [START] ###
    try : 
        with open(filename, "r") as file :
            line = file.readlines()
            dim = [int(line[0]), int(line[1])]
            matrix = [[0 for i in range(dim[0])] for j in range(dim[1])] 
            for item in line[2:]:
                info = item.split()
                coord = info[0].split(",")
                matrix[int(coord[0])][int(coord[1])] = float(info[1]) 
            return matrix
    except :
        return None

#### TESTS ####    

f = open("mat.txt", "w")
f.write("""\
3
3
0,0 10
1,1 20
0,2 30
""")
f.close()
assert load_matrix("mat.txt") == [[10.0, 0.0, 30.0], [0.0, 20.0, 0.0], [0.0, 0.0, 0.0]], " Test 1 failled" # TEST 1
assert load_matrix("fail") == None, "Test 2 failled" # TEST 2