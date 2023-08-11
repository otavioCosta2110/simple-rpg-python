from other import initial

#! bugs:
#! enemy's level system is kind of broken

#* ToDo:
#* overwolrd?
#* Bosses
#* correct directories
player = initial.create_player()
while True:
    enemy = initial.create_enemy(player)
    initial.init_world(player, enemy)
    
    if initial.recreateEncounter():
        enemy = initial.create_enemy(player)
        initial.encounter(enemy, player)    
    
    if not player.is_alive():
        break