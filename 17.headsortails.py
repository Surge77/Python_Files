"""
Write a virtual coin toss program.It will randomly tell the user "Heads" or "Tails"

the first letter should be capitalised and spelt exactly like given aboce


"""

import random  # We need to import the random module through which we generate random numbers



random_side = random.randint(0,1)

if random_side == 1: #condition when the random number is 1
    print("Heads")

else:
    print("Tails") #this is the condition for 0

