### Code to complete [START] ###

class Employe :
    def __init__(self, n, s):
        self.nom = n
        self.salaire = s    
   

    def __str__(self):
        info = "{} : {}".format(self.nom, self.salaire)
        return info
    
    
    def augmente(self, augm):
        pourcent = 1 + (augm)/100
        new_salary = self.salaire * pourcent
        self.salaire = new_salary