import ascii
class Character():
    def __init__(self, name, health, attack, defense, level=1, type='player'):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.type = type
        
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    
    def getDefense(self):
        return self.defense
    
    def getLevel(self):
        return self.level
    
    def getAscii(self):
        ascii_art = ascii.ascii()
        return ascii_art.get_ascii(self.name)
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            self.health = 0
            return False

    def take_damage(self, damage):
        damage = int(damage)
        if damage >= self.getDefense():
            self.health -= damage - self.getDefense()
            if self.is_alive():
                print(f"Character {self.name} has {self.health} remaining health!")
            else:
                print(f"{self.getName()} died!")
        else:
            print(f"Damage was annullated by {self.getName()}'s defense!")
    
    def attacking(self, attacked):
        attacked.take_damage(self.getAttack())
        
    def defend(self):
        self.defense *= 2 
        print(self.defense)