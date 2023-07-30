import items
import createEnemy
import enemyAi
import time
import character
import random
import points

potion = items.Item('Potion', 'health', 1,  10)
power_plus = items.Item('Power Plus', 'attack', 1, 0, 10)
steroids = items.Item('Steroids', 'defense', 1, 0, 0, 10)

item_list = []

def create_player():
    item_list.append(potion)
    item_list.append(power_plus)
    item_list.append(steroids)
    
    name = input("What is your name? ")
    player = character.Character(name)
    player = points.point_system(player, 20)
    return player

def action_menu(player, enemy):
    print("What will you do? \n")
    choice = int(input("|1. Attack       |\n|2. Defend       |\n|3. Run          |\n|4. Check status |\n|5. Use Item     |\n"))
    
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
        case 5:
            print("\n")
            valid_items = [i for i in item_list if i.quantity > 0]

            for index, i in enumerate(valid_items, 1):
                spaces_type = " " * (20 - len(i.name))
                spaces_quantity = " " * (15 - len(i.type))
                print(f"{index}. {i.name}{spaces_type}+ {i.quantity} {i.type}{spaces_quantity}Quantity: {i.quantity}")
            #* print("\nq - quit")
            item_choice = int(input("\nWhich will you choose? "))
            item_used = valid_items[item_choice - 1]
            print(f"You used {item_used.name}!")
            item_used.quantity -= 1
            player.use_item(item_used.type, item_used.getValues())
                
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
            createEnemy.create_enemy(player)
        else:
            break