"""
[Q6] Il y a un noeud en trop dans cette liste!
Nous vous fournissons la classe DoubleLinkedList représentant une liste doublement chaînée. 
On vous demande d'implémenter une classe BoundedLinkedList, par héritage de la classe DoubleLinkedList, qui se comporte comme une DoubleLinkedList mais avec la contrainte additionnelle qu'elle admet un nombre maximal de noeuds. 
Le nombre maximal est donné en paramètre de la méthode __init__. Si le nombre maximal est déjà atteint lorsqu'on ajoute un noeud en tête de liste, on élimine le dernier noeud en queue de liste pour maintenir le maximum.

La classe DoubleLinkedList est partiellement donnée ci-après. Vous trouverez ensuite la classe BoundedLinkedList dont vous devrez compléter les méthodes __init__ et add_to_start.
"""

#Score 100%


class DoubleLinkedList :
    """
    DoubleLinkedList représente une structure de données de type
    liste doublement chaînée, où chaque noeud a une référence vers
    son noeud suivant et précédent.
    """

    def __init__(self):
        """
        @pre:  -
        @post: Une nouvelle liste vide a été initialisée.
        """
        # code non fourni

    def size(self):
        """
        @pre:  -
        @post: Retourne le nombre de noeuds (éventuellement zéro) contenus dans cette liste.
        """
        # code non fourni

    def first(self):
        """
        @pre:  -
        @post: Retourne la cargaison du premier noeud de cette DoubleLinkedList,
               ou None si la liste chaînée ne contient encore aucun noeud.
        """
        # code non fourni

    def last(self):
        """
        @pre:  -
        @post: Retourne la cargaison du dernier noeud de cette DoubleLinkedList,
               ou None si la liste chaînée ne contient encore aucun noeud.
        """
        # code non fourni

    def add_to_start(self, cargo):
        """
        @pre:  -
        @post: Ajoute un nouveau noeud avec une cargaison donnée au début de cette liste.
        """
        # code non fourni

    def remove_last(self):
        """
        @pre:  -
        @post: Supprime le dernier noeud de cette liste, s'il existe.
        """
        # code non fourni

    def __str__(self):
        """
        @pre:  -
        @post: Produit une chaîne de caractères représentant le contenu de cette liste.
        """
        # code non fourni

class BoundedLinkedList(DoubleLinkedList) :
    
    
    def __init__(self,maxsize) :
        """
        @pre:  maxsize > 0 est le nombre maximal de noeuds que la liste peut contenir
        @post: La taille maximale __max est initialisée à maxsize.
               Une nouvelle liste vide a été initialisée.
        """
        super().__init__()
        self.__max = maxsize

    def add_to_start(self, cargo) :
        """
        @pre:  --
        @post: un nouveau noeud avec une cargaison donnée est ajouté au début de
               la liste.  Si la liste contenait déjà son nombre maximal de noeuds,
               le dernier noeud (en queue de la liste) est supprimé.
        """
        super().add_to_start(cargo)
        if super().size() > self.__max :
            super().remove_last()

### Test 1 ###
l = BoundedLinkedList(3) #Créer une liste BoundedLinkedList avec taille maximale de 3 noeuds
l.add_to_start(4)        #Ajouter un noeud avec comme cargaison la valeur 4
assert l.size() == 1, "Test 1 failed !"
### Test 2 ###
l.add_to_start(3)        #Ajouter un noeud avec comme cargaison la valeur 3
assert l.size() == 2, "Test 2 failed !"
### Test 3 ###
l.add_to_start(2)        #Ajouter un noeud avec comme cargaison la valeur 2
assert l.size() == 3, "Test 3 failed !"
### Test 4 ###
l.add_to_start(1)        #Ajouter un noeud avec comme cargaison la valeur 3
assert l.size() == 3, "Test 4 failed !"
### Test 5 ###
assert l.last() == 3, "Test 5 failed !"
### Test 6 ###
assert l.first() == 1, "Test 6 failed !"
### Test 7 ###
l.add_to_start(0)        #Ajouter un noeud avec comme cargaison la valeur 2
assert l.size() == 3, "Test 7 failed !"
### Test 8 ###
assert l.last() == 2, "Test 8 failed !"
### Test 9 ###
assert l.first() == 0, "Test 9 failed !"