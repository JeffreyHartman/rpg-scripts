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
    parser.add_argument('action', nargs='?', default='npc', help='random_event, focus, action, description, list_element_tables, random_element')
    parser.add_argument('--element', default='noblehouse', help='roll on the specified element table')
    args = parser.parse_args()

    if args.action == 'random_event':
        print(generate_random_event())
    elif args.action == 'focus':
        print('Event Focus: ' + generate_event_focus())
    elif args.action == 'action':
        print('Action: ' + generate_action())
    elif args.action == 'description':
        print('Description: ' + generate_descriptor())
    elif args.action == 'list_element_tables':
        fileList = list_element_tables()
        print('Element Tables: ' + ', '.join(fileList))
    elif args.action == 'random_element':
        print(get_file_header(args.element) + ': ' + generate_elements(args.element))
    elif args.action == 'npc':
        npc = generate_NPC()
        for label, value in npc.items():
            print(f"{label}: {value}")

def generate_random_event():
    eventFocus = generate_event_focus()
    event = generate_action()
    return "Event Focus: " + eventFocus + "\nEvent: " + event

def generate_event_focus():
    dieRoll = random.randint(1, 100)
    eventFocus = None

    # check each range in the focus table and  return the focus if the roll is in the range
    for range, result in EVENT_FOCUS_TABLE:
        if dieRoll in range:
            eventFocus = result

    return eventFocus

def generate_action():
    return get_random_word_from_file('action1.txt') + ' ' + get_random_word_from_file('action2.txt')    

def generate_descriptor():
    return get_random_word_from_file('descriptor1.txt') + ' ' + get_random_word_from_file('descriptor2.txt')

def generate_elements(element):
    return generateWordPair('elements/' + element + '.txt')

def generate_NPC():
    npc = {
        'Identity': generateWordPair('elements/characteridentity.txt'),
        'Description': generateWordPair('elements/characterdescription.txt'),
        'Appearance': generateWordPair('elements/characterapp.txt'),
        'Background': generateWordPair('elements/characterbackground.txt'),
        'Personality': generateWordPair('elements/characterpersonality.txt'),
        'Motivation': generateWordPair('elements/charactermotivation.txt'),
        'Skills': generateWordPair('elements/characterskill.txt'),
        'Trait': generateWordPair('elements/charactertrait.txt')
    }
    return npc

def list_element_tables():
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

def get_file_header(filename):
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

def open_file(filename):
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

def get_random_word_from_file(filename):
    content = open_file(filename)
    dieRoll = random.randint(1, len(content))  # Adjust the die roll to the size of the content
    word = content[dieRoll - 1].replace('\n', '')
    return word

def generateWordPair(file):
    return get_random_word_from_file(file) + ' ' + get_random_word_from_file(file)

if __name__ == "__main__":
    main()