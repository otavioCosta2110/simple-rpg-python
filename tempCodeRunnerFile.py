import initial

enemy = initial.create_enemy()
player = initial.create_player()

print(f"You encounter a {enemy.getName()}, how do you proceed?")
print(enemy.getAscii())
initial.action_menu(player, enemy)