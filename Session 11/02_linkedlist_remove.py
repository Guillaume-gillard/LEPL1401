# Guillaume Gillard 
# 12/12/2022

from linkedlist import LinkedList, Node 

### Code to complete [START] ###

def remove(self):
    if self.__head is not None : 
        self.__head = self.__head.next()
        self.__length -= 1
    
# No need to point the next() of the removed element to None 
# Python automaticaly remove element wich is not possible to access