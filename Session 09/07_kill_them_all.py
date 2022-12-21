# Guillaume Gillard 
# 21/12/2022

#### Code to complete [START] ####

class Character():
    def __init__(self, hp, damage):
        self.life = hp
        self.attack_point = damage
    
    def attack(self, target):
        target.get_hit(self.attack_point)       
    
    def get_hit(self, damage):
        self.life -= damage
    
class Cratos(Character):
    def __init__(self):
        super().__init__(100, 10)
        self.experience = 0
    
    def gain_XP(self, amount):
        self.experience += amount
        while self.experience >= 10 :
            self.experience -= 10
            self.attack_point += 1

class Drauf(Character):
    def __init__(self, hp, damage):
        super().__init__(hp, damage)
    


