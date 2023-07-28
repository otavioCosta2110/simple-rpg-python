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
    print("You have 10 points to spend. What do you want to spend them in?")
    spendChoice = input("1. Health  {health}\n2. Attack  {attack}\n3. Defense {defense}\n")
    points = input("How many points do you want to spend on it?")
    match spendChoice:
        case 1:
            health += int(points)
            
    player = character.Character(name, health, attack, defense)
    return player

def action_menu(player, enemy):
    print("What will you do? \n")
    choice = int(input("|1. Attack |\n|2. Defend |\n|3. Run    |\n")
    )
    match choice:
        case 1:
            enemy.take_damage(player.getAttack())