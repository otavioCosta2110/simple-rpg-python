import initial
import createEnemy

#* Criar sistema de itens
player = initial.create_player()
while True:
    enemy = createEnemy.create_enemy()
    initial.encounter(enemy, player)
    if not player.is_alive():
        break