import time
import random
import character
def enemy_turn(enemy, player):
    choices = [1, 2]
    weights = [60, 40]
    choice = random.choices(choices, weights=weights)[0]
    match choice:
        case 1:
            print(f"Enemy {enemy.getName()} attacks!")
            attack(enemy, player)
        case 2:
            print(f"Enemy {enemy.getName()} defends")
            defend(enemy)
            
def attack(enemy, player):
    enemy.attacking(player)
    
def defend(enemy):
    enemy.defend