import enemyAi
import time
import character
import random

def create_enemy():
    enemies = []
    goblin = character.Character('Goblin', 10, 5, 2, 2, 'enemy')
    skeleton = character.Character('Skeleton', 7, 7, 2, 3, 'enemy')
    ogre = character.Character('Ogre', 15, 8, 4, 5, 'enemy')
    enemies.append(goblin)
    enemies.append(skeleton)
    enemies.append(ogre)
    
    return random.choice(enemies)

def create_player():
    name = input("What is your name? ")
    health = 0
    attack = 0
    defense = 0
    remainingPoints = 10
    
    while remainingPoints >0:
        while True:
            print(f"\nYou have {remainingPoints} remaining points to spend. What do you want to spend them in?\n")
            spendChoice = input(f"1. Health  {health}\n2. Attack  {attack}\n3. Defense {defense}\n")
            if spendChoice =='1' or spendChoice =='2' or spendChoice =='3':
                break
            else:
                print("\nInvalid!")
        while True:
            points = int(input("How many points do you want to spend on it? "))
            if points > remainingPoints:
                print("\nInvalid!\n")
            else:
                break
        
        remainingPoints -= points
        match int(spendChoice):
            case 1:
                health += points
            case 2:
                attack += points
            case 3:
                defense += points

    player = character.Character(name, health, attack, defense)
    return player

def action_menu(player, enemy):
    print("What will you do? \n")
    choice = int(input("|1. Attack |\n|2. Defend |\n|3. Run    |\n")
    )
    match choice:
        case 1:
            player.attacking(enemy)
        case 2:
            player.defend()                
        case 3:
            print("You try to run .",end="")
            for i in range(0,2):
                time.sleep(1)
                print(".",end="")
            if random.choice([True, False]):
                print(" You ran away!")
                return True
            else:
                print(" You couldnt run away!")
                return False
                
def encounter(enemy, player):
    while True:
        print(f"You encounter a {enemy.getName()}, how do you proceed?")
        print(enemy.getAscii())
        if action_menu(player, enemy):
            break
        if enemy.is_alive():
            print(f"Enemy {enemy.getName()} is still alive!")
            print(enemy.getAscii())
            enemyAi.enemy_turn(enemy,player)
        else:
            player.receive_exp(enemy)
            break
        if not player.is_alive():
            break