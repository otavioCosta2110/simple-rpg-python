class armour():
    def __init__(self, name, attack, defense, magicRes='None', magicWeak='None'):
      self.name = name
      self.attack = attack
      self.defense = defense
      self.magicRes = magicRes
      self.magicWeak = magicWeak
      
    def equip(self, player):
      player.defense += self.defense
      player.attack += self.attack
      player.magicRes = self.magicRes
      player.magicWeak = self.magicWeak
      player.armour = self
      
    def unequip(self, player):
      player.defense -= self.defense
      player.defense -= self.attack
      player.magicRes = 'none'
      player.magicWeak = 'none'
      player.armour = 'none'