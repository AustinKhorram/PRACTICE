# 2018-10-08
# Austin Khorram
# Dice Roll Simulator
#
# This program should output a number between 1 & 6 for as long as the user wants to generate them.

# Return a random integer between 1 & 6 (inclusive)
def get_random():
    import random
    dice_roll = random.randint(1,6)
    return dice_roll

print("Hello user! Please enter \"1\" if you wish to roll dice. To exit, enter \"0\". ")

roll = input()

while roll == "1":
    print("Random number is: " + str(get_random()) )
    print("Please enter \"1\" if you wish to roll again. To exit, enter \"0\"." )
    roll = input()
