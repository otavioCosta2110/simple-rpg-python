import math
import random
import character
def create_enemy():
    enemy_name_list = ['Goblin', 'Skeleton', 'Ogre']
    enemy_name = random.choice(enemy_name_list)
    
    enemy = character.Character(enemy_name)
    
    enemy.level = random.randint(1, 5)
    
    enemy.type = 'enemy'
    
    if enemy_name == 'Goblin':
        enemy.health = int((enemy.level * 2) + 4)
        enemy.attack = int((enemy.level * 2) + 2)
        enemy.defense = int((enemy.level * 4) + 1)
        
    elif enemy_name == 'Skeleton':
        enemy.health = (enemy.level * 3) + 1
        enemy.attack = math.ceil((enemy.level * 10/4) + 4)
        enemy.defense = (enemy.level * 2) + 1

    elif enemy_name == 'Ogre':
        enemy.health = (enemy.level * 5) + 3
        enemy.attack = math.ceil((enemy.level * 16/3) + 5)
        enemy.defense = (enemy.level * 4) + 1
    
    return enemy