# console/ascii_components.py
import os
import shutil
from typing import List, Dict, Optional
from .menu_base import MenuBase

class ASCIIComponents:
    # Box drawing characters
    HORIZONTAL = "─"
    VERTICAL = "│"
    TOP_LEFT = "╭"
    TOP_RIGHT = "╮"
    BOTTOM_LEFT = "╰"
    BOTTOM_RIGHT = "╯"
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def get_terminal_size():
        return shutil.get_terminal_size()
    
    @staticmethod
    def create_box(width: int, height: int) -> List[str]:
        """Creates an empty box with the specified dimensions."""
        box = []
        box.append(f"{ASCIIComponents.TOP_LEFT}{ASCIIComponents.HORIZONTAL * (width-2)}{ASCIIComponents.TOP_RIGHT}")
        for _ in range(height - 2):
            box.append(f"{ASCIIComponents.VERTICAL}{' ' * (width-2)}{ASCIIComponents.VERTICAL}")
        box.append(f"{ASCIIComponents.BOTTOM_LEFT}{ASCIIComponents.HORIZONTAL * (width-2)}{ASCIIComponents.BOTTOM_RIGHT}")
        return box
    
    @staticmethod
    def create_header(title: str, width: int) -> List[str]:
        """Creates a header with the title centered."""
        padding = (width - len(title) - 2) // 2
        header = [
            f"╭{'═' * (width-2)}╮",
            f"│{' ' * padding}{title}{' ' * (width - len(title) - padding - 2)}│",
            f"╰{'═' * (width-2)}╯"
        ]
        return header
    
    @staticmethod
    def create_menu(options: Dict[str, str], width: int) -> List[str]:
        """Creates a menu with the specified options."""
        menu = []
        for key, value in options.items():
            menu.append(f"  [{key}] {value}")
        return menu
    
    @staticmethod
    def create_status_bar(engine: str, chaos: int, width: int) -> List[str]:
        """Creates a status bar with engine and chaos factor."""
        status = f" Engine: {engine} | Chaos Factor: {chaos} "
        padding = width - len(status) - 2
        return [f"╠{'═' * (width-2)}╣",
                f"║{status}{' ' * padding}║",
                f"╚{'═' * (width-2)}╝"]

class ASCIIMenuBase(MenuBase):
    def __init__(self):
        super().__init__()
        self.ascii = ASCIIComponents()
        self.width = min(80, self.ascii.get_terminal_size().columns)
        self.chaos_factor = 5  # Default chaos factor
        
    def display_frame(self, content: List[str], title: str):
        """Displays content within an ASCII frame."""
        self.ascii.clear_screen()
        
        # Create and display header
        header = self.ascii.create_header(title, self.width)
        for line in header:
            print(line)
            
        # Display content
        for line in content:
            print(line)
            
        # Create and display status bar
        status = self.ascii.create_status_bar(
            self.settings.engines[self.settings.current_engine],
            self.chaos_factor,
            self.width
        )
        for line in status:
            print(line)
    
    def display_result(self, result: str):
        """Displays a result in an attractive box."""
        box_width = min(60, self.width - 4)
        #result_box = self.ascii.create_box(box_width, 5)

        initial_lines = result.split('\n')
        result_lines = []
        for line in initial_lines:
            while line:
                result_lines.append(line[:box_width-4])
                line = line[box_width-4:]
        
        result_box = self.ascii.create_box(box_width, len(result_lines) + 2)

        for i, line in enumerate(result_lines, 1):
            padding = (box_width - len(line) - 2) // 2
            result_box[i] = f"│{' ' * padding}{line}{' ' * (box_width - len(line) - padding - 2)}│"
        
        print("\n".join(result_box))
        input("\nPress Enter to continue...")