import random
import time

quest = str(input('Would you like to roll the dice? If yes, write "yes", or "no"!'))

def roll_the_dice():
    num = random.randint(1,6)
    print(num)
    
    for x in range(0, num):
        for y in range(0, num):
            if x == y:
                time.sleep(1)
                print('O', sep='', end=' ')
        print()
    
    print('Dice played!')    
    
if quest == 'yes':
    roll_the_dice()
    
    while True:
        quest2 = str(input('Would you like to play the dice again? If yes press "y", or "n"!'))
        if quest2 == 'y':
            roll_the_dice()
        else:
            break
else: 
    print('Ok, see you later!')