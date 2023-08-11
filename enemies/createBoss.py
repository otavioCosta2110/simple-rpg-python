import player.character as character
import random
import math

def create_boss(player):
    boss_name_list = ['Dragon', 'Kraken', 'King of Rats']
    boss_name = random.choice(boss_name_list)
    
    boss = character.Character(boss_name)
    
    boss.level = random.randint(5, 10) + player.level 
    
    boss.type = 'boss'
    
    if boss_name == 'Dragon':
        boss.health = (boss.level * 2) + 3
        boss.attack = math.ceil((boss.level * 16/3) + 5)
        boss.defense = (boss.level * 4) + 1
        boss.magicRes = 'fire'
        boss.magicWeak = 'ice'
        
    elif boss_name == 'Kraken':
        boss.health = (boss.level * 2) + 3
        boss.attack = math.ceil((boss.level * 16/3) + 5)
        boss.defense = (boss.level * 4) + 1
        boss.magicRes = 'ice'
        boss.magicWeak = 'fire'

    elif boss_name == 'King of Rats':
        boss.health = (boss.level * 2) + 3
        boss.attack = math.ceil((boss.level * 16/3) + 5)
        boss.defense = (boss.level * 4) + 1
        boss.magicRes = 'light'
    
    return boss