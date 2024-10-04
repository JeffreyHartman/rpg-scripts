import random
import argparse

SCENE_ADJUSTMENT_TABLE = [
    (1, "Remove a Character"),
    (2, "Add a Character"),
    (3, "Reduce/Remove an Activity"),
    (4, "Increase an Activity"),
    (5, "Remove an Object"),
    (6, "Add an Object"),
    (7, "Make 2 Adjustments"),
    (8, "Make 2 Adjustments"),
    (9, "Make 2 Adjustments"),
    (10, "Make 2 Adjustments")
]

def main():
    parser = argparse.ArgumentParser(description='Generate a random event.')
    parser.add_argument('action', nargs='?', default='scene_check', help='scene_check|scene_adjustment')
    parser.add_argument('--chaos', type=int, nargs='?', default='5', help='chaos factor')
    args = parser.parse_args()

    if args.action == 'scene_check':
        dieRoll = random.randint(1, 10)
        print("Scene Check: " + sceneCheck(args.chaos, dieRoll) + " (" + str(dieRoll) + ")")
    elif args.action == 'scene_adjustment':
        print("Scene Adjustment: " + sceneAdjustment(args.chaos))

def sceneAdjustment(chaosFactorInt):
    dieRoll = random.randint(1, 10)
    for pos, result in SCENE_ADJUSTMENT_TABLE:
        if dieRoll == pos:
            return result
    
def sceneCheck(chaosFactorInt, dieRoll):
    if dieRoll <= chaosFactorInt:
        if dieRoll % 2 == 0:
            return "Interrupt Scene!"
        else:
            return "Altered Scene!"
    else:
        return "Normal Scene"

if __name__ == "__main__":
    main()