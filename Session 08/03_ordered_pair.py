class Pair :
    pass 

class OrderedPair:
    '''
    Représente une paire de deux entiers (représenté en interne par une instance p de la classe Pair).
    Cette paire est considérée comme ordonnée si l'attribut a de p est plus petit ou égal à son attribut b
    '''

    def __init__(self):
        self.p = Pair(0, 0)
        self.ordered = True


### Code to complete [START] ###


    def set_a(self, n_a):
        """
        @pre: None
        @post: donne au premier élément de la paire la nouvelle valeur n_a
        """
        self.p.a = n_a
        self.ordered = self.p.a<=self.p.b


    def set_b(self, n_b):
        """
        @pre: None
        @post: donne au second élément de la paire la nouvelle valeur n_b
        """
        self.p.b = n_b
        self.ordered = self.p.a<=self.p.b
        
