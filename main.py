#Dice Roll stimulator my very first project on github i hope you like it and have a good day :)
import random

Dice_1 = 1
Dice_2 = 6

roll_again = 'y'

while roll_again is 'y':
    print("The Numbers are: ")
    print(random.randint(Dice_1, Dice_2))
    print(random.randint(Dice_1, Dice_2))
    roll_again = input("Roll the dices again?")