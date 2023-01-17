
#### Code to complete [START] ####

def remove_from_end(self):
    current  = self.first()
    previous = None
    # list empty
    if current == None :
        return 
    if self.first().next() ==  None :
        self.__length -= 1
        self.__head = None
        return 
    while True :
        if current.next() == None :
            previous.set_next(current.next())
            self.__length -= 1
            return 
        previous = current
        current = current.next()