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

enemy = create_enemy()

def create_player():
    name = input("What is your name? ")
    health = input("How much health do you have? ")
    attack = input("How strong are you? ")
    defense = input("How resilient are you? ")
    player = character.Character(name, health, attack, defense)
    return player

# player = create_player()

# print(player.getName())
# print(player.getHealth())
# print(player.getAttack())
# print(player.getDefense())
# print(player.getLevel())
print(enemy.getName())
enemy.take_damage(5)
print(enemy.getAscii())