# menu_base.py
from console.io_handler import IOHandler
from abc import ABC, abstractmethod
from config.settings import Settings
from services.ai.base import AIConfig
import sys

class MenuBase(ABC):
    def __init__(self, io_handler: IOHandler):
        self.settings = Settings()
        self.ai_config = AIConfig()
        self.io_handler = io_handler

    @abstractmethod
    def display(self):
        pass

    def handle_input(self, choice: str, options: dict) -> bool:
        choice = choice.upper()
        if choice == "C":
            self.change_engine()
            return True
        elif choice == "S":
            self.settings_menu()
            return True
        elif choice == "Q":
            self.io_handler.display_message("Goodbye!")
            sys.exit()
        elif choice in options:
            return False
        else:
            self.io_handler.display_error("Invalid choice. Please try again.")
            return True

    def print_menu(self, options: dict, title: str = None):
        # Use the io_handler to display the menu
        menu_content = self.io_handler.display_menu(options, title)
        return menu_content

    def settings_menu(self):
        while True:
            options = {
                "1": "AI Settings",
                "B": "Back",
            }

            # Use the io_handler to display the menu
            content = self.io_handler.display_menu(options, "Settings Menu")
            self.io_handler.display_frame(content, "Settings")

            choice = self.io_handler.display_input_prompt("\nEnter your choice: ").strip().upper()

            if choice == "1":
                self.ai_settings_menu()
            elif choice == "B":
                break
            else:
                self.io_handler.display_error("Invalid choice. Please try again.")

    def ai_settings_menu(self):
        while True:
            options = {
                "1": "Set OpenAI API Key",
                "2": "Set Theme",
                "3": "View Current Settings",
                "B": "Back",
            }

            content = self.io_handler.display_menu(options, "AI Settings Menu")
            self.io_handler.display_frame(content, "AI Settings")

            choice = self.io_handler.display_input_prompt("\nEnter your choice: ").strip().upper()

            if choice == "1":
                self._set_api_key_menu()
            elif choice == "2":
                self._set_theme_menu()
            elif choice == "3":
                self._display_current_settings()
            elif choice == "B":
                break
            else:
                self.io_handler.display_error("Invalid choice. Please try again.")

    def change_engine(self):
        engines = self.settings.engines
        options = {str(i): name for i, (key, name) in enumerate(engines.items(), 1)}
        options["0"] = "Cancel"

        content = self.io_handler.display_menu(options, "Available Engines")
        self.io_handler.display_frame(content, "Change Engine")

        choice = self.io_handler.display_input_prompt("\nSelect engine: ").strip()
        if choice == "0":
            return
        elif choice in options:
            index = int(choice) - 1
            engine_key = list(engines.keys())[index]
            self.settings.current_engine = engine_key
            self.io_handler.display_message(f"\nSwitched to {engines[engine_key]}")
        else:
            self.io_handler.display_error("Invalid choice")

    def _set_api_key_menu(self):
        self.io_handler.display_frame("", "Set OpenAI API Key")
        self.io_handler.display_message("\nEnter your OpenAI API key (leave blank to keep current):")
        self.io_handler.display_message("You can get this from https://platform.openai.com/account/api-keys")
        current_key = self.ai_config.get_api_key("openai")
        if current_key:
            self.io_handler.display_message(f"Current API key: {current_key}")

        new_key = self.io_handler.display_input_prompt().strip()
        if new_key:
            self.ai_config.set_api_key("openai", new_key)
            self.io_handler.display_message("API key set successfully")
        self.io_handler.display_message("\nPress Enter to continue...")
        self.io_handler.display_input_prompt()

    def _set_theme_menu(self):
        themes = ["fantasy", "scifi", "modern", "horror", "cyberpunk", "grimdark"]
        options = {str(i): theme for i, theme in enumerate(themes, 1)}
        options["0"] = "Back"

        content = self.io_handler.display_menu(options, "Available Themes")
        self.io_handler.display_frame(content, "Set Theme")

        choice = self.io_handler.display_input_prompt("\nSelect theme: ").strip()
        if choice == "0":
            return
        elif choice in options:
            selected_theme = options[choice]
            self.ai_config.set_theme(selected_theme)
            self.io_handler.display_message(f"Theme set to {selected_theme}")
            self.io_handler.display_message("\nPress Enter to continue...")
            self.io_handler.display_input_prompt()
        else:
            self.io_handler.display_error("Invalid choice")

    def _display_current_settings(self):
        theme = self.ai_config.get_theme()
        key = self.ai_config.get_api_key("openai")
        key_display = key if key else "Not Set"

        content = f"[bold]Current Settings:[/bold]\n\n- Theme: {theme}\n- OpenAI API Key: {key_display}"
        self.io_handler.display_frame(content, "Current Settings")
        self.io_handler.display_message("\nPress Enter to continue...")
        self.io_handler.display_input_prompt()
