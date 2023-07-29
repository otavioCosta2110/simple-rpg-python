import createEnemy
import enemyAi
import time
import character
import random
import points

def create_player():
    name = input("What is your name? ")
    
    player = character.Character(name)
    player = points.point_system(player, 20)
    return player

def action_menu(player, enemy):
    print("What will you do? \n")
    choice = int(input("|1. Attack       |\n|2. Defend       |\n|3. Run          |\n|4. Check status |\n"))
    
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
        case 4:
            print(f"Health: {player.getHealth()}\nAttack: {player.getAttack()}\nDefense: {player.getDefense()}\n")
                
def encounter(enemy, player):
    print(f"You encounter a {enemy.getName()} level {enemy.getLevel()}, how do you proceed?")
    print(enemy.getAscii())
    while True:
        if action_menu(player, enemy):
            break
        if enemy.is_alive():
            print(f"Enemy {enemy.getName()} is still alive!")
            enemyAi.enemy_turn(enemy,player)
        else:
            player.receive_exp(enemy)
            break
        if player.is_alive():
            createEnemy.create_enemy
        else:
            break