import initial
import createEnemy

#* Criar sistema de itens
#* Criado: Classe de itens
#* Falta: monstros droparem itens, mais itens, mais um monte de coisa
player = initial.create_player()
while True:
    enemy = createEnemy.create_enemy(player)
    initial.encounter(enemy, player)
    if not player.is_alive():
        break