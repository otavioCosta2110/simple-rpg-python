import other.ascii as ascii
import time
import os
import random
#* to have: enemies, npcs? 
def showPath(item_list):
    while True:
        print(ascii.ascii().get_ascii("singular path"))
        time.sleep(0.7);
        os.system('clear')
        if random.random() > 0.7:
            item_dropped = random.choice(item_list)
            item_dropped.giveItem()
            os.system('clear')
        print(ascii.ascii().get_ascii("singular path 2"))
        time.sleep(0.7);
        os.system('clear')
        if random.random() > 0.5:
            return False