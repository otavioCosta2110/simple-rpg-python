import os

import usable.items as items
import other.overworld as overworld
import enemies.createEnemy as createEnemy
import enemies.createBoss as createBoss
import enemies.enemyAi as enemyAi
import time
import player.character as character
import random
import player.points as points
import usable.magic as magic
import usable.inventory as inventory
import usable.armour as armour
    
turn = 1
totalTurn = 0
is_defending = False
def recreateEncounter():
    return True

armour_list = [
    armour.armour('Fire Armour', 3, 3, 'fire', 'ice'),
    armour.armour('Ice Armour', 3, 3, 'ice', 'fire'),
    armour.armour('Lightining Armour', 3, 3, 'light'),
    armour.armour('Obsidian Armour', 3, 3, 'fire', 'light')
]

item_list = [
    items.Item('Potion', 'health', 1,  10),
    items.Item('Power Plus', 'attack', 1, 0, 10),
    items.Item('Steroids', 'defense', 1, 0, 0, 10)
]

magic_list = [
    magic.Magic('Fireball', 'black', 'fire', 10, 2),
    magic.Magic('Ice Spear', 'black', 'fire', 10, 2),
    magic.Magic('Bolt', 'black', 'light', 10, 2),
    magic.Magic('Cure', 'white', 'light', 5, 2)
]

def create_player():
    
    name = input("What is your name? ")
    player = character.Character(name)
    player = points.point_system(player, 100)
    return player

def action_menu(player, enemy):
    global is_defending
    print(f"Enemy {enemy.getName()} is still alive!")
    print(enemy.getAscii())
    print(f"Turn {turn}")
    print(f"Turn {totalTurn}")
    
    print("What will you do? \n")
    print(" ___________________")
    choice = int(input("|1. Attack          |\n|2. Defend          |\n|3. Run             |\n|4. Check inventory |\n|5. Use Item        |\n|6. Use Magic       |\n -------------------\n"))
    
    while True:
        os.system('clear')
        if is_defending:
            is_defending = player.reverse_defense()
        match choice:
            case 1:
                player.attacking(enemy)
                break
            case 2:
                is_defending = player.defend()
                print(f"Sua defesa agora é {player.getDefense()}")
                break
            case 3:
                print("You try to run .",end="")
                for i in range(0,2):
                    time.sleep(1)
                    print(".",end="")
                if random.choice([True, False]):
                    os.system('clear')
                    input(" You ran away!\n\nPress Enter to continue")
                    newenemy = create_enemy(player)
                    encounter(newenemy, player)
                    break
                else:
                    input(" You couldnt run away!\n\nPress Enter to continue")
                    break
            case 4:
                inventory.check(player)
                os.system('clear')
                action_menu(player, enemy)
                break
            case 5:
                print("\n")
                valid_items = [i for i in item_list if i.quantity > 0]

                for index, i in enumerate(valid_items, 1):
                    spaces_type = " " * (20 - len(i.name))
                    spaces_quantity = " " * (15 - len(i.type))
                    print(f"{index}. {i.name}{spaces_type}+{i.getValues()} {i.type}{spaces_quantity}Quantity: {i.quantity}")
                print("\nq - quit")
                item_choice = input("\nWhich will you choose? ")
                if item_choice == 'q':
                    os.system('clear')
                    action_menu(player, enemy)
                    break
                else:    
                    item_used = valid_items[int(item_choice) - 1]
                    print(f"You used {item_used.name}!")
                    item_used.quantity -= 1
                    player.use_item(item_used.type, item_used.getValues())
                    # return True
                    break
            case 6:
                print("\n")
                print(" ______________________________________________")
                print(f'|Name   {" " * (10 - len("Name"))}|Power{" " * (10 - len("Power"))}|Kind{" " * (10 - len("Kind"))}|Cost{" " * (10 - len("Cost"))}|')
                for index, i in enumerate(magic_list, 1):
                    spaces = " " * (10 - len(i.name))
                    spaces_power = " " * (10 - len(str(i.power)))
                    spaces_kind = " " * (10 - len(i.kind))
                    print(f"|{index}. {i.name}{spaces}|{i.power}{spaces_power}|{i.kind}{spaces_kind}| Cost: {i.cost}  |")
                print(" ----------------------------------------------")
                magic_choice = int(input("\nWhich will you choose? "))
                if magic_list[magic_choice - 1].act(enemy, player):
                    break
                else:
                    action_menu(player, enemy)
                    break        
                          
def encounter(enemy, player):
    global turn
    global totalTurn
    global is_defending
    os.system('clear')
    print(f"You encountered a {enemy.getName()} level {enemy.getLevel()}, how do you proceed?")
    while True:
        totalTurn += 1
        if action_menu(player, enemy):
            continue
        if enemy.is_alive():
            enemyAi.enemy_turn(enemy,player)
            turn += 1
        else:
            turn = 1
            player.receive_exp(enemy)
            os.system('clear')
            item_dropped = random.choice(item_list)
            item_dropped.giveItem()
            os.system('clear')
            armour_dropped = random.choice(armour_list)
            armour_dropped.giveArmour()
            os.system('clear')
            break
        if player.is_alive():
            create_enemy(player)
        else:
            break
        
def init_world(player, enemy):
    if not overworld.showPath(item_list):
        encounter(enemy, player)
        
def create_enemy(player):
    if totalTurn > 20:
        rng = random.random()
        print(rng)
        if rng > 0.7:
            return createBoss.create_boss(player)
    else:
        return createEnemy.create_enemy(player)