class Node:
    """ Represents a Node in a LinkedList data structure. """

    def __init__(self, cargo=None, next=None):
        """
        Creates a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
               A node can contain a cargo and a reference to another node.
               If none of these are given, the node is initialised with
               empty cargo (None) and no reference (None).
        """
        self.__cargo = cargo
        self.__next  = next

    def value(self):
        """
        @pre:  -
        @post: Returns the value of the cargo contained in this node,
               or None if no cargo was put there.
        """
        return self.__cargo

    def set_value(self,value):
        """
        @pre:  -
        @post: The cargo of this node has been set to value.
        """
        self.__cargo = value

    def next(self):
        """
        @pre:  -
        @post: Returns the next node to which this node refers,
               or None if there is no next node.
        """
        return self.__next

    def set_next(self,node):
        """
        @pre:  -
        @post: The next node of this node has been set to node.
        """
        self.__next = node

    def __str__(self):
        """
        @pre:  self is a (possibly empty) Node object.
        @post: returns a print representation of the cargo contained in this Node.
        """
        return str(self.value())


    def __eq__(self,other):
        """
        Comparator to compare two Node objects by their cargo.
        """
        if other is not None :
            return self.value() == other.value()
        else :
            return False

    def print_list(self):
        """
        Prints the cargo of this node and then recursively
        of each node connected to this one.
        @pre:  -
        @post: Has printed a space-separated list of the form "a b c ... ",
               where "a" is the string-representation of this node,
               "b" is the string-representation of my next node, and so on.
               A space is printed after each printed value.
        """
        print(self.value(), end=" ")     # print my value
        tail = self.next()       # go to my next node
        if tail is not None :    # as long as the end of the list has not been reached
            tail.print_list()    # recursively print remainder of the list

    def print_backward(self):
        """
        Recursively prints the cargo of each node connected to this node (in opposite order),
        and then prints the cargo of this node as last value.
        @pre:  -
        @post: Has printed a space-separated list of the form "... c b a",
               where a is my cargo (self), b is the cargo of the next node, and so on.
               The nodes are printed in opposite order: the last node's value
               is printed first.
        """
        tail = self.next()        # go to my next node
        if tail is not None :     # as long as the end of the list has not been reached
            tail.print_backward() # recursively print remainder of the list backwards
        print(self.value(), end = " ")    # print my value

class LinkedList :
    """ Represents a linked list datastructure. """

    def __init__(self, lst):
        self.__length = len(lst)
        self.__head = None 
        for i in range(1, len(lst)+1):
            self.__head = Node(lst[-i], self.__head)

    def size(self):
        """
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def first(self):
        """
        @pre:  -
        @post: Returns a reference to the head of this linked list,
               or None if the linked list contains no nodes.
        """
        return self.__head

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this LinkedList.
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the LinkedList.
               The length counter has been incremented.
               The head of the list now points to this new node.
               Nothing is returned.
        """
        node = Node(cargo,self.__head)
        self.__head = node
        self.__length += 1

    def print(self):
        """
        Prints the contents of this LinkedList and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

    def print_backward(self):
        """
        Prints the contents of this LinkedList and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the LinkedList's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")
    
    def remove_first(self):
        if self.__head is not None : 
            self.__head = self.__head.next()
            self.__length -= 1

    def add_end(self, s):
        current = self.__head 
        while current.next is not None :
            current = current.next
        newnode = Node(s, current.next)
        current.set_next(newnode)
    
    def print_with_virgule(self):
        s = "[ "
        current = self.__head
        while True :
            s += current.value 
            if current.next() is not None :
                s += " ,"
            if current.next is None :
                s += " ]"
                print(s)
                return s
            current = current.next()
    
    def print_with_separateur(self, sep):
        s = "[ "
        current = self.__head
        while True :
            s += current.value 
            if current.next() is not None :
                s += " " + sep
            if current.next is None :
                s += " ]"
                print(s)
                return s
            current = current.next()


