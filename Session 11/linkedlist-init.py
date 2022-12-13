# Guillaume Gillard
# 11/12/2022

from linkedlist import LinkedList, Node 

### Code to complete [START] ###

def __init__(self, lst):
    self.__length = len(lst)
    self.__head = None 
    for i in range(1, len(lst)+1):
        self.__head = Node(lst[-i], self.__head)