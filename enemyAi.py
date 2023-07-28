import time
import random
def enemy_turn(enemy, player):
    choices = [1, 2, 3]
    weights = [60, 30, 10]

    choice = random.choices(choices, weights=weights)[0]
    match choice:
        case 1:
            attack(enemy, player)
        case 2:
            defend(enemy)
        case 3:
            print(f"Enemy {enemy.getName()} tries to run .",end="")
            for i in range(0,2):
                time.sleep(1)
                print(".",end="")
            if random.choice([True, False]):
                print(" He ran away!")
                return True
            else:
                print(" He couldnt run away!")
                return False
            
def attack(enemy, player):
    enemy.attacking(player)
    
def defend(enemy):
    enemy.defend