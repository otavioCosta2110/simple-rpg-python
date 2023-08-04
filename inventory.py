import armour

armour_gotten = []

def check(player):
    print(player.getAscii())
    getStatus(player)
    
def getStatus(player):
    spaces_health = " " * (30 - (len(str(player.getHealth())) + len(str(player.getHLimit()))))
    spaces_attack = " " * (40 - len(str(player.getAttack())+ "|Attack: "))
    spaces_defense = " " * (40 - len(str(player.getDefense())+ "|Defense: "))
    spaces_magic = " " * (40 - len(str(player.getMagic()) + "|Magic: "))
    spaces_armour = " " * (40 - len(player.getArmour() + "|Armour: "))
    print(" _______________________________________")
    print(f"|Health: {player.getHealth()}/{player.getHLimit()}{spaces_health}|\n|Attack: {player.getAttack()}{spaces_attack}|\n|Defense: {player.getDefense()}{spaces_defense}|\n|Magic: {player.getMagic()}{spaces_magic}|\n|Armour: {player.getArmour()}{spaces_armour}|")
    print(" ---------------------------------------")
    if len(armour_gotten) > 0:
        print("Available Armour:")
    if(len(armour_gotten)> 0 ):
        for index, armour in enumerate(armour_gotten, 1):
            print(f"{index}. {armour.name}")
        print("\n0. no")
        choice_armour = int(input("Want to equip any of them? "))
        
        if choice_armour != 0:
            if armour_gotten[choice_armour - 1] != player.armour:
                if player.armour != None:
                    player.armour.unequip
                armour_gotten[choice_armour - 1].equip(player)
            else:
                print("Already Equipped!")