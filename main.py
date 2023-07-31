import initial
import createEnemy
#! bugs:
#! enemy's level system is kind of broken

#* ToDo:
#* magic, health limit, enemy weakness and resistence to magic, cool boxes for selecting
#* armour, overwolrd?
player = initial.create_player()
while True:
    enemy = createEnemy.create_enemy(player)
    initial.encounter(enemy, player)
    if not player.is_alive():
        break