class Magic():
    def __init__(self, name, kind, type, power, cost):
        self.name = name
        self.type = type
        self.power = power
        self.kind = kind
        self.cost = cost
                
    def can_use(self, player):
        if player.magic >= self.cost:
            player.magic -= self.cost
            return True
        else:
            return False
    
    def act(self, enemy, player):
        if self.can_use(player):
            if self.kind =='black':
                if self.type == enemy.getMagicRes():
                    enemy.take_damage(int(self.power * 0.5))
                elif self.type == enemy.getMagicWeak():
                    enemy.take_damage(int(self.power * 2))
                else:
                    enemy.take_damage(self.power)
                    
            else:
                player.health += self.power
            print(f"You used {self.name}!")
            return True
        else:
            print("Not Enough Magic!")
            return False