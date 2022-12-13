# Guillaume Gillard 
# 12/12/2022

from linkedlist import LinkedList, Node 

### Code to complete [START] ###

def remove(self):
    if self.__head is not None : 
        self.__head = self.__head.next()
        self.__length -= 1
        