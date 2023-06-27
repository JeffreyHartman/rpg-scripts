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
    parser.add_argument('action', nargs='?', default='random_element', help='random_event, focus, action, description, list_element_tables, random_element')
    parser.add_argument('--element', default='noblehouse', help='roll on the specified element table')
    args = parser.parse_args()

    if args.action == 'random_event':
        print(generateRandomEvent())
    elif args.action == 'focus':
        print('Event Focus: ' + generateEventFocus())
    elif args.action == 'action':
        print('Action: ' + generateAction())
    elif args.action == 'description':
        print('Description: ' + generateDescriptor())
    elif args.action == 'list_element_tables':
        fileList = listElementTables()
        print('Element Tables: ' + ', '.join(fileList))
        #for file in fileList:
         #   print(file)
    elif args.action == 'random_element':
        print(getFileHeader(args.element) + ': ' + generateElements(args.element))

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
    return getRandomWordFromFile('action1.txt') + ' ' + getRandomWordFromFile('action2.txt')    

def generateDescriptor():
    return getRandomWordFromFile('descriptor1.txt') + ' ' + getRandomWordFromFile('descriptor2.txt')

def generateElements(element):
    return getRandomWordFromFile('elements/' + element + '.txt') + ' ' + getRandomWordFromFile('elements/' + element + '.txt')

def listElementTables():
    # list all the tables in the tables/mythic2e/elements directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    filepath = os.path.join(parent_dir, "tables/mythic2e/elements")

    fileList = []

    for filename in os.listdir(filepath):
        fileParts = filename.split('.')
        fileList.append(fileParts[0])
    fileList.sort()

    return fileList

def getFileHeader(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    filepath = os.path.join(parent_dir, "tables/mythic2e/elements", filename + '.txt')

    try:
        with open(filepath, 'r') as f:
            # Read the first line as the header
            header = f.readline().replace('\n', '')
            # Strip the # from the header
            header = header[2:]
    except FileNotFoundError:
        raise FileNotFoundError('File not found: ' + filepath)
    
    return header

def openFile(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    filepath = os.path.join(parent_dir, "tables/mythic2e", filename)

    try:
        with open(filepath, 'r') as f:
            # Read the first line as the header and ignore it
            header = f.readline()
            content = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError('File not found: ' + filepath)
    
    return content

def getRandomWordFromFile(filename):
    content = openFile(filename)
    dieRoll = random.randint(1, len(content))  # Adjust the die roll to the size of the content
    word = content[dieRoll - 1].replace('\n', '')
    return word

if __name__ == "__main__":
    main()