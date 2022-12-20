# Guillaume Gillard
# 20/12/2022


### Code to complete [START] ###

class Weapon():
    def __init__(self, attack):
        self.attack = attack
    
class Cratos():
    def __init__(self, weapon):
        self.weapon = weapon 
    
    def set_weapon(self, new_weapon):
        """
        change the weapon
        """
        self.weapon = new_weapon
    
    def hit(self, enemy):
        """ 
        hit the ennemy with the weapon attack and reduce its hp
        """
        damage = self.weapon.attack 
        enemy.get_hit(damage)

class Drauf():
    def __init__(self, hp):
        self.life = hp

    def get_hit(self, damage):
        """
        reduce the life by the damage taken
        """
        self.life -= damage 
    