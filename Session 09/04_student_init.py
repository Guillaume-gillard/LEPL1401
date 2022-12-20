# Guillaume Gillard
# 20/12/2022


#### Code to complete [START] ####

class Student():
    
    __noma_generator = 0
    
    def __init__(self, firstname, surname, birthday, email):
        self.__noma = Student.__noma_generator
        self.__firstname = firstname
        self.__lastname = surname
        self.__birthday = birthday
        self.__email = email        
        Student.__noma_generator += 1
    
    def __str__(self):
        info = "L'étudiant numéro {} : {} {} né le {}, peut être contacté par {}".format(self.__noma, self.__firstname, self.__lastname, self.__birthday, self.__email)
        return info