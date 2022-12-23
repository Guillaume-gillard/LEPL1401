# Guillaume Gillard
# 23/12/2022


#### Code to complete [START] ####

class Animal():
    
    def __init__(self, name, diurnal=None, legs=None, asleep=False):
        self.name = name  
        self.diurnal = diurnal
        self.nb_legs = legs
        self.asleep = asleep
    
    
    def sleep(self): 
        if self.asleep :
            raise RuntimeError("Your animal is already sleeping")
        self.asleep = True
    
    
    def wake_up(self):
        if not self.asleep :
            raise RuntimeError("Your animal is not sleeping")
        self.asleep = False

class Lion(Animal):
    def __init__(self, n):
        super().__init__(n)
        self.nb_legs = 4
        self.diurnal = True
    
    
    def roar():
        print("ROARRR!!!")
    

class Owl(Animal):
    def __init__(self, name):
        super().__init__(name, False, 2)

      
    def fly():
        pass


class Giraffe(Animal):
    def __init__(self, name, length):
        super().__init__(name, True, 4)
        self.neck_length = None 
        if (type(length) == int or type(length) == float) and length >= 0 :
            self.neck_length = length
            return           
        else :
            raise ValueError
        
        
class Zoo():
    def __init__(self, l=[]):
        self.animals = l
    
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            return
        raise ValueError("Please only add animals to the Zoo !")

def create_my_zoo():
    simba_the_lion = Lion("simba")
    twiga_the_giraffe = Giraffe("twiga", 10)
    melman_the_giraffe = Giraffe("melman", 12)
    hedwige_the_owl = Owl("hedwige")
    my_animal = [simba_the_lion, twiga_the_giraffe, hedwige_the_owl]
    my_zoo = Zoo(my_animal)
    my_zoo.add_animal(melman_the_giraffe)
    return my_zoo

    

