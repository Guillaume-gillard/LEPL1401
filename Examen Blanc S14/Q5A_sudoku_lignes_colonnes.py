# Guillaume Gillard
# 20/12/2022

from Q5_contexte import SudokuPuzzle, SudokuCarre

def create_valid_m():
    pass

### Code to complete [START] ###

def get_carre_valeurs(self, x, y):    # Ne pas effacer cette ligne
    """
    @pre:  0 ≤ x < N
           0 ≤ y < N
    @post: retourne une liste de toutes les valeurs apparaissant dans le SudokuCarre
           qui se trouve à la position (x, y) du puzzle Sudoku
           Si une valeur apparaît plusieurs fois dans ce carré,
           elle se retrouvera plusieurs fois dans la liste retournée.
    """
    square = self.get_carre(x, y)
    l = []
    for line in square.cells :
        for number in line:
            l.append(number)
    return l

    
    
def get_ligne(self, ligne):    # Ne pas effacer cette ligne
    """
    @pre:  0 ≤ ligne < N * N
    @post: retourne une liste de toutes les valeurs apparaissant
           à une certaine ligne du puzzle Sudoku
           Si une valeur apparaît plusieurs fois sur une ligne
           elle se retrouvera plusieurs fois dans la liste retournée
    """
    l = []
    squares = []
    dim = self.dimension
    square_line = ligne//dim
    line_in_square = ligne%dim
    for i in range(dim) :
        square = self.get_carre(i, square_line)
        for x in range(dim):
            l.append(square.get_val(x, line_in_square))
    return l
   

def get_colonne(self, colonne):    # Ne pas effacer cette ligne
    """
    @pre:  0 ≤ colonne < N * N
    @post: retourne une liste de toutes les valeurs apparaissant
           à une certaine colonne du puzzle Sudoku
           Si une valeur apparaît plusieurs fois sur une colonne
           elle se retrouvera plusieurs fois dans la liste retournée
    """
    l = []
    dim = self.dimension
    square_line = colonne//dim
    column_in_square = colonne%dim
    for i in range(dim) :
        square = self.get_carre(square_line, i)
        for x in range(dim):
            l.append(square.get_val(column_in_square, x))
    return l

#### TESTS ####

p1 = create_valid_m()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 2 3
# 2 3 | 1 4

assert p1.get_carre_valeurs(0, 1) == [4, 1, 2, 3], "Test 1 failled"

assert p1.get_ligne(3) == [2, 3, 1, 4], "Test 2 failled"

assert p1.get_colonne(2) == [3, 4, 2, 1], "Test 3 failled"
