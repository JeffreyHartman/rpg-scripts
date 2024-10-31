# engines/mythic2e/utils.py
import os
import random
from typing import List

ENGINE_NAME = "mythic2e"

def get_random_word(filename: str) -> str:
    """Get random word from a table file."""
    content = _open_file(filename)
    return random.choice(content).strip()

def get_element_tables() -> List[str]:
    """List all available element tables."""
    elements_dir = os.path.join(_get_tables_directory(), "elements")
    try:
        files = os.listdir(elements_dir)
        return [f.split('.')[0] for f in files if f.endswith('.txt')]
    except FileNotFoundError:
        raise FileNotFoundError(f'Elements directory not found: {elements_dir}')

def get_file_header(filename: str) -> str:
    """Get the header from a table file."""
    filepath = os.path.join(_get_tables_directory(), "elements", filename + '.txt')
    try:
        with open(filepath, 'r') as f:
            # Read the first line as the header
            header = f.readline().replace('\n', '')
            # Strip the # from the header
            return header[2:]
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {filepath}')

def _open_file(filename: str) -> List[str]:
    """Open and read a table file."""
    if filename.startswith('elements/'):
        # Handle element files in engine-specific subfolder
        filepath = os.path.join(_get_tables_directory(), filename)
    else:
        # Handle regular table files in engine-specific folder
        filepath = os.path.join(_get_tables_directory(), filename)
    
    try:
        with open(filepath, 'r') as f:
            # Read the first line as the header and ignore it
            header = f.readline()
            content = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {filepath}')
    
    return content

def _get_tables_directory() -> str:
    """Get the path to the engine's tables directory."""
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(project_root, "tables", ENGINE_NAME)