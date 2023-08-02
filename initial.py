import items
import createEnemy
import enemyAi
import time
import character
import random
import points
import magic
import inventory
        
def recreateEncounter():
    return True
#* armour_list = [
    
# ]

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

def action_menu(player, enemy, og_defense):
    print("What will you do? \n")
    print(" ___________________")
    choice = int(input("|1. Attack          |\n|2. Defend          |\n|3. Run             |\n|4. Check inventory |\n|5. Use Item        |\n|6. Use Magic       |\n -------------------\n"))
    
    while True:
        player.reverse_defense(og_defense)
        match choice:
            case 1:
                player.attacking(enemy)
                break
            case 2:
                player.defend()
                break
            case 3:
                print("You try to run .",end="")
                for i in range(0,2):
                    time.sleep(1)
                    print(".",end="")
                if random.choice([True, False]):
                    print(" You ran away!")
                    newenemy = createEnemy.create_enemy(player)
                    encounter(newenemy, player)
                    break
                else:
                    print(" You couldnt run away!")
                    break
            case 4:
                inventory.check(player)
                action_menu(player, enemy, og_defense)
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
                    print("Saiu")
                    action_menu(player, enemy, og_defense)
                    break
                else:    
                    item_used = valid_items[int(item_choice) - 1]
                    print(f"You used {item_used.name}!")
                    item_used.quantity -= 1
                    player.use_item(item_used.type, item_used.getValues())
                    return True
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
    print(f"You encountered a {enemy.getName()} level {enemy.getLevel()}, how do you proceed?")
    print(enemy.getAscii())
    og_defense = player.getDefense()
    while True:
        
        if action_menu(player, enemy, og_defense):
            continue
        if enemy.is_alive():
            print(f"Enemy {enemy.getName()} is still alive!")
            enemyAi.enemy_turn(enemy,player)
        else:
            player.receive_exp(enemy)
            if random.random() < 0.5:
                item_dropped = random.choice(item_list)
                item_dropped.quantity += 1
                print(f"You gained {item_dropped.name}")
            break
        if player.is_alive():
            createEnemy.create_enemy(player)
        else:
            break