import points
import ascii
class Character():
    def __init__(self, name, health=1, attack=1, defense=1, magic=1, magicRes='none', magicWeak='none', level=1, type='player', healthlimit=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.level = level
        self.magicRes = magicRes
        self.magicWeak = magicWeak
        self.type = type
        self.healthlimit = health
        self.exp = 0
        
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    
    def getDefense(self):
        return self.defense
    
    def getMagic(self):
        return self.magic
    
    def getLevel(self):
        return self.level
    
    def getMagicRes(self):
        return self.magicRes
    
    def getMagicWeak(self):
        return self.magicWeak

    def getExp(self):
        return self.exp
    
    def getHLimit(self):
        return self.healthlimit
    
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
        
    
    def reverse_defense(self, defense):
        print(self.defense)
        self.defense = defense
        
    def receive_exp(self, enemy):
        self.exp += enemy.getLevel()
        self.level_up()
        
    def level_up(self):
        if self.getExp() >= int(self.getLevel()) * 3.5:
            self.level += 1
            print(f"You Leveld up! Your current level is {self.getLevel()}")
            points.point_system(self, 1)
    
    def heal(self, value):
        self.health += value
        
    def use_item(self, type, value):
        match type:
            case 'health':
                if self.health + value < self.healthlimit:
                    self.heal(value)
                else:
                    self.heal(self.healthlimit)
                    
                print(self.health, self.healthlimit, value)
            case 'attack':
                self.attack += value
            case 'health':
                self.defense += value
                