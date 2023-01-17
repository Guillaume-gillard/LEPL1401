#### Code to complete [START] ####

def __str__(self):
    s = "[ "
    current = self.__head
    if current == None :
        return "[ ]"
    while True :
        s += str(current.value()) + " "
        if current.next() == None :
            break
        current = current.next()
    s += "]"
    return s