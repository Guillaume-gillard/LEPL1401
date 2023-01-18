# Guillaume Gillard

# Question 1: Node

class Node():
    def __init__(self, s, prev=None, next=None):
        self.__text = s
        self.__previous = prev
        self.__next = next
    
    def get_previous(self):
        return self.__previous
    
    def get_next(self):
        return self.__next
    
    def set_previous(self, previous):
        self.__previous = previous
    
    def set_next(self, next):
        self.__next = next

    def get_text(self):
        return self.__text
    
    def set_text(self, s):
        self.__text = s
    
# Question 2: Double LinkedList

class Tape ():
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__pointer = None
        self.__length = 0
    
    def next(self):
        if self.__pointer.get_next() == None :
            return None
        self.__pointer = self.__pointer.get_next()
        return self.__pointer.get_text()
    
    def previous(self):
        if self.__pointer.get_next() == None :
            return None
        self.__pointer = self.__pointer.get_previous()
        return self.__pointer.get_text()
    
    def get_length(self):
        return self.__length
    
    def add(self, s):
        if self.__length == 0 :
            self.__head = Node(s, None)
            self.__last = self.__head
            self.__pointer = self.__head
        self.__last.set_next(Node(s, self.__last.get_next()))
        self.__last.get_next().set_previous(self.__last)
        self.__last == self.__last.get_next()
        self.__pointer = self.__last.__previous
    
    def write(self, s):
        if self.__length == 0 :
            return 
        self.__pointer.set_text(s)
    
    def read(self):
        if self.__pointer != None:
            return self.__pointer.get_text()
        return 

    
    

