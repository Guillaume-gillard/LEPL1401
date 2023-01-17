class Item :

    def __init__(self,author,title,serial):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              serial est un entier > 0
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title et comme numéro de série serial
        """
        self.__author = author
        self.__title = title
        self.__serial = serial

    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: [num série] Auteur, Titre
        """
        return "[{}] {}, {}".format(self.__serial,self.__author,self.__title)

### Code to complete [START] ###

    def author(self):
        return self.__author
    
    def title(self):
        return self.__title
    
    def serial(self):
        return self.__serial
    

class CD(Item):
    serie = 100000
    def __init__(self, t, a, d):
        super().__init__(a, t, CD.serie)
        self.__duree = d
        CD.serie += 1
    
    def __str__(self):
        s = "[{}] {}, {} ({} s)".format(self.serial(), self.title(), self.author(), self.__duree)
        return s