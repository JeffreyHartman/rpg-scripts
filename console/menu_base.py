from abc import ABC, abstractmethod
from config.settings import Settings
import sys

class MenuBase(ABC):
    def __init__(self):
        self.settings = Settings()

    @abstractmethod
    def display(self):
        pass
    
    def print_menu(self, options: dict, title: str = None):
        if title:
            print(f"\n{title}")

            print("\nSystem Options:")
            print("C. Change Game Engine")
            print("S. Settings")
            print("Q. Quit")
            
            if options:
                print("\nGame Options:")
                for key, value in options.items():
                    print(f"{key}. {value}")
            
            print("")
            return input("Enter your choice: ").upper()
        
    def handle_input(self, choice: str, options: dict) -> bool:
        choice = choice.upper()
        if choice == "C":
            self.change_engine()
            return True
        elif choice == "S":
            self.settings_menu()
            return True
        elif choice == "Q":
            print("Goodbye!")
            sys.exit()
        return False
    
    def change_engine(self):        
        print("\nAvailable Engines:")
        for i, (key, name) in enumerate(self.settings.engines.items(), 1):
            print(f"{i}. {name}")
        print("0. Cancel")
        
        choice = input("\nSelect engine: ")
        if choice == "0":
            return
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.settings.engines):
                engine_key = list(self.settings.engines.keys())[index]
                self.settings.current_engine = engine_key
                print(f"\nSwitched to {self.settings.engines[engine_key]}")
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")