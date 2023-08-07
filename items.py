import random
class Item():
    def __init__(self, name, type, quantity, hp=0, atk=0, defs=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.type = type
        self.quantity = quantity
        
    def resHP(self):
        return self.hp
    
    def resATK(self):
        return self.atk
    
    def resDEF(self):
        return self.defs
    
    def getValues(self):
        match self.type:
            case 'health':
                return self.hp
            case 'attack':
                return self.atk
            case 'defense':
                return self.defs
            
    def giveItem(self):
        if random.random() < 0.3:
            self.quantity += 1
            input(f"You gained {self.name}!\n\nPress enter to continue ")