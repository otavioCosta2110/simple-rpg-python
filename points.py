def point_system(player, remainingPoints):
    while remainingPoints >0:
        while True:
            print(f"\nYou have {remainingPoints} remaining points to spend. What do you want to spend them in?\n")
            spendChoice = input(f"1. Health  {player.health}\n2. Attack  {player.attack}\n3. Defense {player.defense}\n4. Magic   {player.magic}\n")
            if spendChoice =='1' or spendChoice =='2' or spendChoice =='3' or spendChoice =='4':
                break
            else:
                print("\nInvalid!")
        while True:
            points = int(input("How many points do you want to spend on it? "))
            if points > remainingPoints:
                print("\nInvalid!\n")
            else:
                break
        
        remainingPoints -= points
        match int(spendChoice):
            case 1:
                player.health += points
            case 2:
                player.attack += points
            case 3:
                player.defense += points
            case 4:
                player.magic += points
    return player