# Guillaume Gillard 
# 12/12/2022

class Node():
    pass
class LinkedList():
    pass

### Code to complete [START] ###

def remove(self):
    if self.__head is not None : 
        self.__head = self.__head.next()
        self.__length -= 1
        