# Guillaume Gillard
# 17/01/2023

class Figure:
    def __init__(self,x,y,visible=False) :
        """
        @pre x, y sont des entiers représentant des positions sur l'écran
        @post Une figure a été créée avec centre de gravité aux coordonnées x,y.
              Cette figure n'est initialement pas visible
        """
        self.__x = x
        self.__y = y
        self.__visible = visible

    def est_visible(self) :
        """
        @pre -
        @post a retourné la visibilité de cette figure
        """
        return self.__visible
    
    ### Code to complete [START] ###

    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    


class Rectangle(Figure):

    def __init__(self,longueur,largeur,x,y) :
        """
        @pre longueur et largeur sont des entiers positifs
             x, y sont des entiers représentant des positions sur l'écran
        @post un rectangle dont le centre de gravite est en x,y
              et ayant comme longueur lo et comme largeur la a été créé
        """
        super().__init__(x,y)
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self) :
        return str((self.longueur, self.largeur, super().x(), super().y(), super().est_visible()))

    def surface(self):
        return self.longueur * self.largeur

