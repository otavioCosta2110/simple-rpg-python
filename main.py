import initial
import createEnemy

#* ToDo: monsters drop items, quit without endind turn in action_menu
player = initial.create_player()
while True:
    enemy = createEnemy.create_enemy(player)
    initial.encounter(enemy, player)
    if not player.is_alive():
        break