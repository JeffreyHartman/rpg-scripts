import os
import random
from typing import List

def get_random_word(filename: str) -> str:
    content = _open_file(filename)
    return random.choice(content).strip()

def list_element_tables() -> List[str]:
    elements_dir = _get_elements_directory()
    return [f.split('.')[0] for f in os.listdir(elements_dir) if f.endswith('.txt')]

def get_file_header(filename: str) -> str:
    filepath = os.path.join(_get_elements_directory(), f"{filename}.txt")
    with open(filepath, 'r') as f:
        return f.readline().strip()[2:]  # Remove '# ' from the start

def _open_file(filename: str) -> List[str]:
    filepath = os.path.join(_get_mythic2e_directory(), filename)
    with open(filepath, 'r') as f:
        return f.readlines()[1:]  # Skip header

def _get_mythic2e_directory() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _get_elements_directory() -> str:
    return os.path.join(_get_mythic2e_directory(), "tables", "mythic2e", "elements")