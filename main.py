import initial
import createEnemy
#! bugs:
#! enemy's level system is kind of broken

#* ToDo:
#* armour, alter character sprite as armour changes, overwolrd?
player = initial.create_player()
while True:
    enemy = createEnemy.create_enemy(player)
    initial.encounter(enemy, player)
    
    if initial.recreateEncounter():
        enemy = createEnemy.create_enemy(player)
        initial.encounter(enemy, player)    
    
    if not player.is_alive():
        break