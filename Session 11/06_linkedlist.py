# Guillaume Gillard

class Node():
    def __init__(self, cargo, next):
        self.__cargo  = cargo 
        self.__next = next
    
    def set_next(self, next):
        self.__next = next

    def get_value(self):
        return self.__cargo 
    
    def get_next(self):
        self.__next

class LinkedList():
    def __init__(self):
        self.__head = None
    
    def add(self, new):
        self.__head = Node(new, self.__head)
    
    def get_reverse(self):   # contre intuitif il faut juste imprimer dans l'ordre de la list car elle est deja créée à l'envers
        node = self.__head 
        txt = ""
        while node != None:
            txt += node.get_value()
            node = node.get_next()
        return txt