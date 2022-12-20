# Code source Questions 5A et 5B

class SudokuPuzzle:
    def __init__(self,dimension) :
        """
        Crée un SudokuPuzzle de dimension `dimension` avec tous les éléments initialisés à 0.
        """
        self.dimension = dimension
        self.carres = [ [ SudokuCarre(x,y,dimension) \
                          for x in range (dimension) ] \
                          for y in range (dimension)]

    def get_carre(self,x,y) :
        """
        Retourne le SudokuCarre qui se trouve à la position (x, y) dans ce Sudoku.
        """
        return self.carres[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le Sudoku.
        """
        s = ""
        for y in range(len(self.carres)) :
            for x in range (len(self.carres[y])) :
                s += str(self.get_carre(x,y))
            s += "\n"
        return s

class SudokuCarre:

    def __init__(self,x,y,dimension) :
        """
        Crée un SudokuCarre de taille `dimension` x `dimension`, avec toutes ses valeurs initialisées à 0.
        """
        self.xcoord_carre = x
        self.ycoord_carre = y
        self.cells = [ [ 0 for x in range(dimension) ]
                        for y in range(dimension) ]

    def set_val(self,x,y,val) :
        """
        Assigne une valeur `val` à la cellule se trouvant à la position (x, y) de ce carré.
        """
        self.cells[y][x] = val

    def get_val(self,x,y) :
        """
        Retourne la valeur qui se trouve à la position (x, y) de ce carré.
        """
        return self.cells[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le contenu de ce carré.
        """
        s = "carré (" + str(self.xcoord_carre) + "," + str(self.ycoord_carre) + ") : "
        s += str(self.cells)
        s += " "
        return s