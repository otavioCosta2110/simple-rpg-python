def check(player):
    print(player.getAscii())
    getStatus(player)
    
def getStatus(player):
    spaces_health = " " * (10 - (len(str(player.getHealth())) + len(str(player.getHLimit()))))
    spaces_attack = " " * (20 - len(str(player.getAttack())+ "|Attack: "))
    spaces_defense = " " * (20 - len(str(player.getDefense())+ "|Defense: "))
    spaces_magic = " " * (20 - len(str(player.getMagic()) + "|Magic: "))
    print(" ___________________")
    print(f"|Health: {player.getHealth()}/{player.getHLimit()}{spaces_health}|\n|Attack: {player.getAttack()}{spaces_attack}|\n|Defense: {player.getDefense()}{spaces_defense}|\n|Magic: {player.getMagic()}{spaces_magic}|")
    print(" -------------------")