"""
[Q5] Il est l'or, Monseignor!
Créez une classe CoffreFort dont les objets représentent un coffre-fort qu'on peut ouvrir (avec un code secret) ou fermer. 
On peut aussi reinitialiser le coffre-fort pour changer le code secret, ou obtenir le trésor contenu dedans mais seulement si le coffre-fort est ouvert.
"""

# Score : 95%

class CoffreFort :

    def __init__(self, code, tresor) :
        """
        @pre:  code et tresor sont des chaînes de caractères représentant,
               respectivement, un code secret pour ouvrir le coffre-fort et
               le secret contenu dans le coffre-fort
        @post: un coffre-fort a été créé et initalisé avec le code donné,
               contenant le trésor donné et est initialement fermé. Ni le code
               ni le trésor sont accessibles de l'extérieur de cet objet.
        """
        self.__open = False
        self.__code = code
        self.__tresor = tresor

    def reinitialiser(self, anciencode, nouveaucode) :
        """
        @pre:  anciencode et nouveaucode sont des chaînes de caractères
               représentant un code secret; cette méthode peut être exécutée peu
               n'importe l'état (ouvert ou fermé) du coffre-fort
        @post: si le code secret actuel du coffre-fort est égal à
               l'anciencode passé en paramètre, le code secret sera remplacé
               par le nouveaucode passé en paramètre et la méthode retourne True;
               sinon rien ne se passe et la méthode retourne False
        """
        if self.__code == anciencode :
            self.__code = nouveaucode 
            return True
        return False

    def ouvrir(self, code) :
        """
        @pre:  -
        @post: Si le code passé en paramètre est égal au code
               actuel du coffre-fort, l'état du coffre-fort change en ouvert;
               si le code passé en paramètre n'est pas le bon, son état ne change pas.
               La méthode retourne True si le coffre-fort est ouvert,
               sinon elle retourne False.
        """
        if self.__code == code :
            self.__open = True
            return True
        return False

    def fermer(self) :
        """
        @pre: -
        @post: L'état du coffre-fort change en fermé (s'il était ouvert,
               ou reste fermé s'il était déjà fermé). La méthode retourne False
               pour indiquer que le coffre-fort est fermé.
        """
        if self.__open :
            self.__open = False
        return False

    def tresor(self) :
        """
        @pre:  -
        @post: si le coffre-fort est ouvert, retourne le tresor contenu
               dedans; sinon retourne None.
        """
        if self.__open :
            return self.__tresor 
        return None
    
### Test 1 ###
coffre = CoffreFort("1234", "mon journal intime")
assert coffre.ouvrir("1234") == True, "Test 1 failed !"
### Test 2 ###
assert coffre.tresor() == "mon journal intime", "Test 2 failed !"
### Test 3 ###
assert coffre.fermer() == False, "Test 3 failed !"
### Test 4 ###
assert coffre.tresor() == None, "Test 4 failed !"
### Test 5 ###
assert coffre.reinitialiser("1234", "4321") == True, "Test 5 failed !"
### Test 6 ###
assert coffre.tresor() == None, "Test 6 failed !"
### Test 7 ###
assert coffre.ouvrir("1234") == False, "Test 7 failed !"
### Test 8 ###
assert coffre.ouvrir("4321") == True, "Test 8 failed !"
### Test 9 ###
assert coffre.tresor() == "mon journal intime", "Test 9 failed !"