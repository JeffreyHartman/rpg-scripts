from abc import ABC, abstractmethod
from config.settings import Settings
from services.ai.base import AIConfig
import sys

class MenuBase(ABC):
    def __init__(self):
        self.settings = Settings()
        self.ai_config = AIConfig()

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

    def settings_menu(self):
        while True:
            options = {
                "1": "AI Settings",
                "B": "Back"
            }
            
            print("\nSettings Menu:")
            for key, value in options.items():
                print(f"{key}. {value}")
            
            choice = input("\nEnter your choice: ").upper()
            
            if choice == "1":
                self.ai_settings_menu()
            elif choice == "B":
                break

    def ai_settings_menu(self):
        while True:
            options = {
                "1": "Set OpenAI API Key",
                "2": "Set Theme",
                "3": "View Current Settings",
                "B": "Back"
            }

            content = self.ascii.create_menu(options, self.width)
            self.display_frame(content, "AI Settings")
            
            choice = input("\nEnter your choice: ").upper()
            if choice == "1":
                self._set_api_key_menu()
            elif choice == "2":
                self._set_theme_menu()
            elif choice == "3":
                self._display_current_settings()
            elif choice == "B":
                break
    
    def _set_api_key_menu(self):
        print ("\nEnter your OpenAI API key (leave blank to keep current):")
        print("You can get this from https://platform.openai.com/account/api-keys")
        current_key = self.ai_config.get_api_key("openai")
        if current_key:
            print(f"Current API key: {current_key}")

        new_key = input().strip()
        if new_key:
            self.ai_config.set_api_key("openai", new_key)
            print("API key set successfully")
        input("\nPress Enter to continue...")

    def _set_theme_menu(self):
        print("\nAvailable Themes:")
        themes = ["fantasy", "scifi", "modern", "horror", "cyberpunk", "grimdark"]
        for i, theme in enumerate(themes, 1):
            print(f"{i}. {theme}")
        print("0. Back")
        
        try:
            choice = input("\nSelect theme: ")
            if choice == "0":
                return
            else:
                self.ai_config.set_theme(choice)
                print(f"Theme set to {choice}")
                input("\nPress Enter to continue...")
        except ValueError:
            print("Invalid input")

    def _display_current_settings(self):
        print("\nCurrent Settings:")
        print(f"Theme: {self.ai_config.get_theme()}")
        key = self.ai_config.get_api_key("openai")
        if key:
            print(f"OpenAI API Key: {key}")
        else:
            print("OpenAI API Key: Not Set")
        input("\nPress Enter to continue...")
    