import initial
import createEnemy

#! bugs:
#! enemy's level system is kind of broken

#* ToDo:
#* overwolrd?
#* make cool interface
#* Bosses
player = initial.create_player()
while True:
    enemy = createEnemy.create_enemy(player)
    initial.init_world(player, enemy)
    
    if initial.recreateEncounter():
        enemy = createEnemy.create_enemy(player)
        initial.encounter(enemy, player)    
    
    if not player.is_alive():
        break