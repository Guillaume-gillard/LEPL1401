# Guillaume Gillard
# 20/12/2022

from Q5_contexte import SudokuPuzzle, SudokuCarre

def create_correct_m():
    pass

def create_not_correct_col():
    pass

def create_not_correct_line():
    pass

def create_not_correct_square():
    pass

### Code to complete [START] ###

def est_correct(self):    
    """
    @pre:  ce Sudoku est bien formé, de dimension self.dimension
    @post: retourne un booléen
           True si le puzzle est correct
           False sinon
    """
    dim = self.dimension
    # verifying square :
    for i in range(dim):
        for x in range(dim):
            value = self.get_carre_valeurs(i, x)
            for i in range(dim-1):
                if value[i] in value[i+1:]:
                    return False
    # verifying line and column 
    for i in range(dim*dim): 
        line = self.get_ligne(i)
        column = self.get_colonne(i)
        for i in range((dim*dim)-1):
                if line[i] in line[i+1:] or column[i] in column[i+1:]:
                    return False
    return True 

#### TESTS ####

p1 = create_correct_m()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 2 3
# 2 3 | 1 4

p2 = create_not_correct_col()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 3 2
# 2 3 | 4 1

p3 = create_not_correct_line()
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 1 4
# 2 3 | 2 3

p4 = create_not_correct_square()
# 3 1 | 4 2
# 2 3 | 1 4
# ---------
# 1 4 | 2 3
# 4 2 | 3 1

print(p1.est_correct())
assert p1.est_correct() == True, "Test 1 failled" # TEST 1

assert p2.est_correct() == False, "Test 2 failled" # TEST 2

assert p3.est_correct() == False, "Test 3 failled" # TEST 3

assert p4.est_correct() == False, "Test 4 failled" # TEST 4

        