# Author :  s1317004

import random

def roll_dice():
    print("Rolling dice...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Total value:", die1 + die2)
    total_value = die1 + die2
    print("Total value:", total_value)
    if total_value > 7:
        print(name + " won!")
    else:
        print(name + " lost.")

name = input("What is your name? ")
print("Hello,", name + "!")

roll_dice()


input("press enter to exit.")