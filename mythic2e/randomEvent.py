import os
import random
import argparse

EVENT_FOCUS_TABLE = [
    (range(1, 6), "Remote Event"),
    (range(6, 11), "Ambiguous Event"),
    (range (11, 21), "New NPC"),
    (range (21, 41), "NPC Action"),
    (range (41, 46), "NPC Negative"),
    (range (46, 51), "NPC Positive"),
    (range (51, 56), "Move Toward A Thread"),
    (range (56, 66), "Move Away from A Thread"),
    (range (66, 71), "Close a Thread"),
    (range (71, 81), "PC Negative"),
    (range (81, 86), "PC Positive"),
    (range (86, 101), "Current Context")
]

def main():
    parser = argparse.ArgumentParser(description='Generate a random event.')
    parser.add_argument('action', nargs='?', default='descriptor', help='generate a random event')
    args = parser.parse_args()

    
    if args.action == 'random_event':
        print(generateRandomEvent())
    elif args.action == 'focus':
        print('Event Focus: ' + generateEventFocus())
    elif args.action == 'action':
        print('Action: ' + generateAction())
    elif args.action == 'descriptor':
        print('Descriptor: ' + generateDescriptor())


def generateRandomEvent():
    eventFocus = generateEventFocus()
    event = generateAction()
    return "Event Focus: " + eventFocus + "\nEvent: " + event

def generateEventFocus():
    dieRoll = random.randint(1, 100)
    eventFocus = None

    # check each range in the focus table and  return the focus if the roll is in the range
    for range, result in EVENT_FOCUS_TABLE:
        if dieRoll in range:
            eventFocus = result

    return eventFocus

def generateAction():
    # roll randomly and read that line number from action1.txt in tables folder
    dieRoll = random.randint(1, 100)

    content = openFile("action1.txt")
    word1 = content[dieRoll - 1]
    word1 = word1.replace('\n', '')

    content = None
    dieRoll = random.randint(1, 100)

    content = openFile('action2.txt')
    word2 = content[dieRoll - 1]
    word2 = word2.replace('\n', '')

    return word1 + ' ' + word2

def generateDescriptor():
    dieRoll = random.randint(1, 100)

    content = openFile("descriptor1.txt")
    word1 = content[dieRoll - 1]
    word1 = word1.replace('\n', '')

    content = None
    dieRoll = random.randint(1, 100)

    content = openFile('descriptor2.txt')
    word2 = content[dieRoll - 1]
    word2 = word2.replace('\n', '')

    return word1 + ' ' + word2

def openFile(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    filepath = os.path.join(parent_dir, "tables", filename)
    
    try:
        with open(filepath, 'r') as f:
            content = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError('File not found: ' + filepath)
    
    return content

if __name__ == "__main__":
    main()