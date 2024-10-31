import random
from .utils import get_random_word, get_element_tables

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

def generate_random_event() -> str:
    eventFocus = _generate_event_focus()
    event = _generate_action()
    return "Event Focus: " + eventFocus + "\nEvent: " + event

def _generate_event_focus() -> str:
    dieRoll = random.randint(1, 100)
    # check each range in the focus table and return the focus if the roll is in the range
    for range, result in EVENT_FOCUS_TABLE:
        if dieRoll in range:
            return result
    return "Invalid Event Focus"

def _generate_action() -> str:
    return f"{get_random_word('action1.txt')} {get_random_word('action2.txt')}"

def generate_descriptor() -> str:
    return f"{get_random_word('descriptor1.txt')} {get_random_word('descriptor2.txt')}"

def list_elements() -> list[str]:
    return get_element_tables()

def generate_element(element: str) -> str:
    return f"{get_random_word('elements/' + element + '.txt')} {get_random_word('elements/' + element + '.txt')}"

def generate_npc() -> dict[str, str]:
    npc_attributes = [
        'Identity', 'Description', 'Appearance', 'Background',
        'Personality', 'Motivation', 'Skills', 'Trait'
    ]
    return {attr: generate_element(f'character{attr.lower()}.txt') for attr in npc_attributes}