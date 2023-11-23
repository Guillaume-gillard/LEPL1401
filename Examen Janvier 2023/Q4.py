"""
[Q4] Qui sera le prochain Picsou ?
Supposons qu'on vous donne un fichier contenant une liste de personnes uniques, et pour chaque personne combien d'argent elle a gagné au cours des derniers mois. Le fichier a le format suivant :

Sophie
4000
200
5000
Lisa
4500
3000
2000
300
Jean
Stéphanie
300
6000
Dans ce format, nous avons une liste de personnes, pour chacune desquelles un nom est donné suivi d'une liste (éventuellement vide) de nombres entiers positifs représentant les gains de cette personne. La liste des gains se termine lorsqu'un nouveau nom est trouvé ou lorsque le fichier se termine. Chaque ligne du fichier contient un seul nom ou un seul nombre, et chaque ligne qui ne représente pas un nombre entier est considérée comme un nom.

Écrivez une fonction max_personne(nom_fichier) qui lit le fichier de nom donné et retourne le nom de la personne qui a gagné le plus, en d'autres mots pour qui la somme des gains est la plus grande. En cas d'égalité, la fonction renvoie le premier nom rencontré.

Si le fichier est vide ou si le fichier n'existe pas, la fonction renvoie une chaîne de caractères vide. Si le fichier n'est pas vide, vous pouvez supposer qu'il commence par le nom d'une personne.

Pour notre exemple, pour Sophie la somme est 9200, pour Lisa 9800, pour Jean 0 et pour Stéphanie 6300. Donc pour ce fichier, la fonction doit retourner le nom "Lisa" (sans "\n").
"""

# SCore : 20% 

def max_personne(nom_fichier):
    """
    pre:  nom_fichier est un nom de fichier (potentiellement vide ou inexistant)
          suivant le format décrit ci-dessus
    post: Retourne le nom de la personne pour laquelle la somme de l'argent gagné est
          la plus élevée, sans \n. En cas d'égalité de somme gagnée, le nom de la personne
          à égalité rencontré en premier dans l'ordre de lecture du fichier est retourné.
          Si le fichier est vide ou inexistant, retourne une chaine de caractère vide
    """
    try :
        with open(nom_fichier, "r") as file :
            picsou = ""
            best_amount = 0
            name = ""
            amount = 0
            for info in file:
                try :
                    amount += int(info)
                except : 
                    if amount > best_amount :
                        picsou = name
                        best_amount = amount
                    name = info 
                    amount = 0
            return picsou
    except :
        return ""
    
### Test 1 ###
f = open("list.txt", "w")
f.write("""Sophie
4000
200
5000
Lisa
4500
3000
2000
300
Jean
Stéphanie
300
6000
""")
f.close()
assert print(max_personne("list.txt")) == print("Lisa"), "Test 1 failed !"
### Test 2 ### 
assert print(max_personne("fail")) == print(""), "Test 2 failed !"