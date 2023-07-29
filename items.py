class Item():
    def __init__(self, name, hp=0, atk=0, defs=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
        
    def resHP(self):
        return self.hp