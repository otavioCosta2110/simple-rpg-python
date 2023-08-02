import math
import random
import character
def create_enemy(player):
    enemy_name_list = ['Goblin', 'Skeleton', 'Ogre']
    enemy_name = random.choice(enemy_name_list)
    
    enemy = character.Character(enemy_name)
    
    enemy.level = random.randint(1, 5)
    
    enemy.type = 'enemy'
    
    if enemy_name == 'Goblin':
        enemy.health = int((enemy.level * player.level) + 4)
        enemy.attack = int((enemy.level * player.level) + 2)
        enemy.defense = int((enemy.level * (player.level/2)) + 3)
        enemy.magicRes = 'fire'
        enemy.magicWeak = 'ice'
        
    elif enemy_name == 'Skeleton':
        enemy.health = (enemy.level * (player.level + 3)) + 1
        enemy.attack = math.ceil((enemy.level * 5/4) + 4)
        enemy.defense = (enemy.level * (player.level)) + 1
        enemy.magicRes = 'ice'
        enemy.magicWeak = 'fire'

    elif enemy_name == 'Ogre':
        enemy.health = (enemy.level * 2) + 3
        enemy.attack = math.ceil((enemy.level * 16/3) + 5)
        enemy.defense = (enemy.level * 4) + 1
        enemy.magicRes = 'light'
    
    return enemy