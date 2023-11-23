"""
[Q3] Des chiffres et des lettres
Étant donné une chaîne de caractères constituée de lettres et d'espaces (pas de ponctuation), l'objectif de cette question est de créer un dictionnaire dans lequel les clés sont chaque mot distinct de la chaîne d'origine et la valeur associée est le nombre de fois que ce mot apparaît dans la chaîne d'origine.

Par exemple:

Si la chaîne est "Un chasseur sachant chasser sans son chien est un bon chasseur et ce chasseur sait chasser sans chien", le dictionnaire serait {'Un': 1, 'chasseur': 3, 'sachant': 1, 'chasser': 2, 'sans': 2, 'son': 1, 'chien': 2, 'est': 1, 'un': 1, 'bon': 1, 'et': 1, 'ce': 1, 'sait': 1}.
Si la chaîne est "Si ton tonton tond ton tonton ton tonton sera tondu", le dictionnaire serait {'Si': 1, 'ton': 3, 'tonton': 3, 'tond': 1, 'sera': 1, 'tondu': 1}.
Pour rappel, vous pouvez utiliser la fonction str.split.
"""

# Score 100%

def nombres_mots(s):
    """
    pre:  s est une chaîne de caractères
    post: Retourne un dictionnaire qui à chaque mot distinct de s
          associe le nombre d'occurences du mot dans s
    """
    d = {}
    for word in s.split():
        if word in d.keys():
            d[word] += 1
        else :
            d[word] = 1
    return d

### Test 1 ###
assert nombres_mots("Un chasseur sachant chasser sans son chien est un bon chasseur et ce chasseur sait chasser sans chien") \
== {'Un': 1, 'chasseur': 3, 'sachant': 1, 'chasser': 2, 'sans': 2, 'son': 1, 'chien': 2, 'est': 1, 'un': 1, 'bon': 1, 'et': 1, 'ce': 1, 'sait': 1} \
, " Test 1 failed !"
### Test 2 ###
assert nombres_mots("Si ton tonton tond ton tonton ton tonton sera tondu") == {'Si': 1, 'ton': 3, 'tonton': 3, 'tond': 1, 'sera': 1, 'tondu': 1}, " Test 2 failed !"
### Test 3 ###
assert nombres_mots("") == {}, "Test 3 failled !"