# Guillaume Gillard

class Client:
    """
    Un client. Chaque client a un nom d'utilisateur (supposé unique,
    par exemple adresse email) et un code pin qui est stocké comme un entier.
    """
    def __init__(self, name, pin):
        self.userName = name
        self.pin = pin

    def getUserName(self):
        return self.userName

    def getPin(self):
        return self.pin

    def setPin(self, pin):
        self.pin = pin

    def __str__(self):
        return self.userName + "(" + str(self.pin) + ")"

class ClientList:
    """Une liste de clients"""

    # un noeud de la liste
    class Node:
        def __init__(self, client, prev):
            self.data = client
            self.link = prev

    def __init__(self):
        self.last = None

    def __str__(self):
        pass

    def update(self, name, pin):
        """
        pre: name != None, la liste contient au plus un élément dont le username
             est `name`.
        post: Si un client dont le username est name est déjà présent, met à jour
              son code pin, sinon ajoute à la liste un nouveau client ayant `name`
              comme username et `pin` comme code pin.
        """
    
    ### Code to complete [START] ###
    
        current = self.last
        while True :
            if current == None :
                client = Client(name, pin)
                self.last = self.Node(client, None)
                return
            if current.link == None :
                client = Client(name, pin)
                self.last = self.Node(client, self.last)
                return
            if current.data.getUserName() == name :
                current.data.setPin(pin)
                return
            current = current.link

   
#### TESTS ####

cl = ClientList()
cl.update("alice", 1234)
print(cl)   # test avec assert pas possible ici car on a pas le code de la methode str
            

