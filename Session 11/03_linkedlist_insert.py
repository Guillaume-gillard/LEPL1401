class Node :
    pass

### Code to complete [START] ###

def insert(self, s):
    current = self.__head 
    if current == None :
        current = Node(s, current)
        self.__head = current
    elif s < current.value() :
        current = Node(s, current)
        self.__head = current
    else :
        while True :
            if current.next() == None:
                current.set_next(Node(s, current.next()))
                break
            elif s < current.next().value():
                
                current.set_next(Node(s, current.next()))
                break   
            current = current.next()
    self.__length += 1
    return
        