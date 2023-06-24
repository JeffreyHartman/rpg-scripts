import os
import random

FATE_CHART = [
    [[-1, 1, 81],[-1, 1, 81],[-1, 1, 81],[1, 5, 82],[2, 10, 83],[3, 15, 84],[5, 25, 86],[7, 35, 88],[10, 50, 91]],
    [[-1, 1, 81],[-1, 1, 81],[1, 5, 82],[2, 10, 83],[3, 15, 84],[5, 25, 86],[7, 35, 88],[10, 50, 91],[13, 65, 94]],
    [[-1, 1, 81],[1, 5, 82],[2, 10, 83],[3, 15, 84],[5, 25, 86],[7, 35, 88],[10, 50, 91],[13, 65, 94],[15, 75, 96]],
    [[1, 5, 82],[2, 10, 83],[3, 15, 84],[5, 25, 86],[7, 35, 88],[10, 50, 91],[13, 65, 94],[15, 75, 96],[17, 85, 98]],
    [[2, 10, 83],[3, 15, 84],[5, 25, 86],[7, 35, 88],[10, 50, 91],[13, 65, 94],[15, 75, 96],[17, 85, 98],[19, 90, 99]],
    [[3, 15, 84],[5, 25, 86],[7, 35, 88],[10, 50, 91],[13, 65, 94],[15, 75, 96],[17, 85, 98],[19, 90, 99],[19, 95, 100]],
    [[5, 25, 86],[7, 35, 88],[10, 50, 91],[13, 65, 94],[15, 75, 96],[17, 85, 98],[18, 90, 99],[19, 95, 100],[20, 99, 999]],
    [[7, 35, 88],[10, 50, 91],[13, 65, 94],[15, 75, 96],[17, 85, 98],[18, 90, 99],[19, 95, 100],[20, 99, 999],[20, 99, 999]],
    [[10, 50, 91],[13, 65, 94],[15, 75, 96],[17, 85, 98],[18, 90, 99],[19, 95, 100],[20, 99, 999],[20, 99, 999]],[20, 99, 999]
]

#roll on the mythic fate chart
def main():
    chaos_factor = int(os.environ['ESPANSO_CHAOS'])
    odds = os.environ['ESPANSO_ODDS']
    #chaos_factor = "5"
    #odds = "I"

    chaosFactorInt = int(chaos_factor)
    #oddsInt = int(odds)

    # if odds are not an int, convert to int
    try:
        oddsInt = int(odds)
    except ValueError:
        oddsInt = convertOdds(odds)

    # minus one to iputs to account for zero indexing
    chaosFactorInt -= 1
    oddsInt -= 1

    # check bounds of inputs
    if chaosFactorInt < 0 or chaosFactorInt > 9:
        raise ValueError('Invalid chaos factor: ' + chaosFactorInt)
    
    if oddsInt < 0 or oddsInt > 9:
        raise ValueError('Invalid odds: ' + oddsInt)
     
    diceRoll = random.randint(1, 100)

    #get fate chart element to use based on inputs
    fateCell = FATE_CHART[chaosFactorInt][oddsInt]

    #convert roll to "Exceptional Yes", "Yes", "No", or "Exceptional No"
    if diceRoll <= fateCell[0]:
        result = "Exceptional Yes"
    elif diceRoll <= fateCell[1]:
        result = "Yes"
    elif diceRoll <= fateCell[2]:
        result = "No"
    else:
        result = "Exceptional No"

    print(str(diceRoll) + ' : ' + result)

def convertOdds(odds):
    if odds in ['Impossible', 'I']:
        return 1
    elif odds in ['No Way', 'NW', 'Nearly Impossible', 'NI']:
        return 2
    elif odds in ['Very Unlikely', 'VU']:
        return 3
    elif odds in ['Unlikely', 'U']:
        return 4
    elif odds in ['50/50', '50', '50-50', '5050']:
        return 5
    elif odds in ['Likely', 'L']:
        return 6
    elif odds in ['Very Likely', 'VL']:
        return 7
    elif odds in ['Near Sure Thing', 'NST', 'Near Sure', 'NS', 'Nearly Certain', 'NC']:
        return 8
    elif odds in ['A Sure Thing', 'ST', 'Sure Thing', 'S', 'Certain', 'C']:
        return 9
    else:
        raise ValueError('Cannot convert odds: ' + odds)

if __name__ == "__main__":
    main()