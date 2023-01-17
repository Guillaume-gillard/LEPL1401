### Code to complete [START] ###

def __eq__(self, p):
    """
        @pre    -
        @post   Retourne true si la paire p est égale à l'objet.
                Retourne false sinon
    """
    if p == None :
        return False
    if self.a == p.a and self.b == p.b :
        return True