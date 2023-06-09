# Author :  s1317004

import random

def roll_dice():
    print("Rolling dice...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Total value:", die1 + die2)

roll_dice()


input("press enter to exit.")