# Guillaume Gillard
# 20/11/2022


class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def opposite(self):
        """
        @pre  -
        @post Retourne une nouvelle instance de Pair dont les deux
              éléments sont les opposés de ceux de cette paire-ci.
              L'instance appelante reste inchangée.
        """

### Code to complete [START] ###

        nx = -self.a
        ny = -self.b
        return Pair(nx, ny)

