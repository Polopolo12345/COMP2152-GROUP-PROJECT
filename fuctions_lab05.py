#functions_lab05.py
import random


# Question 3
def collect_loot(loot_options, belt):
    pirnt("Random loot process: ")
    loot_Roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_Roll - 1)
    print("     |     Your belt: ", belt)
    return loot_options, belt