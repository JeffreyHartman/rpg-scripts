import os
import random

def extract_dice_roll(diceInput):
    parts = diceInput.split('d')

    if len(parts) != 2:
        raise ValueError('Invalid dice roll: ' + diceInput)
    
    numberOfDice = int(parts[0]) if parts[0] else 1
    diceFace = int(parts[1])

    return numberOfDice, diceFace

def roll_dice(numberOfDice, diceFace):
    return [random.randint(1, diceFace) for _ in range(numberOfDice)]

diceInput = os.environ['ESPANSO_DICE']
#diceInput = "10d6"

dice = extract_dice_roll(diceInput)
rolls = roll_dice(*dice)
result = sum(rolls)
print(diceInput + " = " + str(result) + " (" + str(rolls) + ")")