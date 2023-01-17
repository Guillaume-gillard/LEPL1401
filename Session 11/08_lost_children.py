class Child:
    def is_next_valid():  #return a boolean
        pass
    def next_child():     #return a Child
        pass

    ### Code to complete [START] ###

    def is_every_child_here(first_child):
        current = first_child
        while True :
            if not current.is_next_valid():
                return False
            current = current.next_child()
            if current == first_child :
                return True

