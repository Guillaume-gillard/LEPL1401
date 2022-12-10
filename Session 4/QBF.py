# Guillaume Gillard
# 21/10/2022

def positions(p,s):
    """
    pre : p est un pattern, c'est-à-dire une chaîne de
        caractères qui peut contenir des lettres, des chiffres et le caractère '?'
        s contient des lettres et des chiffres mais pas le caractère '?'
    post : retourne une liste des occurrences du pattern p à l'intérieur
        de la chaîne de caractères s. Une occurrence est une sous-chaîne de s
        de même longueur que p qui contient les mêmes caractères que p à
        toutes les positions, '?' peut remplacer tous les caractères.
        en ignorant les majuscules et minuscules
    """

### Code to complete [START] ###

def match(str_1, str_2):
    for i in range(len(str_1)):
        if str_1[i] != "?":
            if str_1[i] != str_2[i]:
                return False
    return(True)
            

def positions(p, s):
    l = []
    s = s.upper()
    p = p.upper()
    for i in range(len(s)-len(p)+1):
        t = s[i:i+len(p)]
        if match(p, t):
            l.append(i)
    return(l)