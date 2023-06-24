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
    chaos_factor = int(os.environ['ESPANSO_DICE'])
    odds = os.environ['ESPANSO_ODDS']

    # if odds are passed in as a string, attempt to parse it into an int
    if isinstance(odds, str):
        odds = convertOdds(odds)

    # minus one to iputs to account for zero indexing
    chaos_factor -= 1
    odds -= 1

    # check bounds of inputs
    if chaos_factor < 0 or chaos_factor > 9:
        raise ValueError('Invalid chaos factor: ' + chaos_factor)
    
    if odds < 0 or odds > 9:
        raise ValueError('Invalid odds: ' + odds)
     
    diceRoll = random.randint(1, 100)

    #get fate chart element to use based on inputs
    fateCell = FATE_CHART[chaos_factor][odds]

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
        raise ValueError('Invalid odds: ' + odds)

if __name__ == "__main__":
    main()