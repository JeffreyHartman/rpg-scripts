# menu_base.py
from console.io_handler import IOHandler
from abc import ABC, abstractmethod
from config.settings import Settings
import sys
from services.ai.manager import AIServiceManager

class MenuBase(ABC):
    def __init__(self, io_handler: IOHandler):
        self.settings = Settings()
        self.io_handler = io_handler
        self.ai_manager = AIServiceManager()
        self.ai_service = self.ai_manager.get_service()

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
                "1": "Set AI Model",
                "2": "Manage API Keys",
                "3": "Set Theme",
                "4": "View Current Settings",
                "B": "Back",
            }

            content = self.io_handler.display_menu(options, " Settings Menu")
            self.io_handler.display_frame(content, "Settings")
            choice = self.io_handler.display_input_prompt("\nEnter your choice: ").strip().upper()

            if choice == "1":
                self._set_model_menu()
            elif choice == "2":
                self._manage_api_keys_menu() 
            elif choice == "3":
                self._set_theme_menu()
            elif choice == "4":
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

    def _manage_api_keys_menu(self):
        while True:
            options = {
                "1": "Set OpenAI API Key",
                "2": "Set Anthropic API Key",
                "0": "Back"
            }

            content = self.io_handler.display_menu(options, "API Keys Management")
            self.io_handler.display_frame(content, "Manage API Keys")
            choice = self.io_handler.display_input_prompt("\nEnter your choice: ").strip()

            if choice == "1":
                self._set_openai_key()
            elif choice == "2":
                self._set_anthropic_key()
            elif choice == "0":
                break
            else:
                self.io_handler.display_error("Invalid choice. Please try again.")

    def _set_openai_key(self):
        self.io_handler.display_frame("", "Set OpenAI API Key")
        self.io_handler.display_message("\nEnter your OpenAI API key (leave blank to keep current):")
        self.io_handler.display_message("You can get this from https://platform.openai.com/account/api-keys")
        
        current_key = self.settings.get_api_key("openai")
        if current_key:
            self.io_handler.display_message(f"Current API key: {current_key}")

        new_key = self.io_handler.display_input_prompt("New API key (leave blank to keep current): ").strip()
        if new_key:
            self.settings.set_api_key("openai", new_key)
            self.io_handler.display_message("OpenAI API key set successfully")
        self.io_handler.wait_for_input()

    def _set_anthropic_key(self):
        self.io_handler.display_frame("", "Set Anthropic API Key")
        self.io_handler.display_message("\nEnter your Anthropic API key (leave blank to keep current):")
        self.io_handler.display_message("You can get this from https://console.anthropic.com/settings/keys")
        
        current_key = self.settings.get_api_key("anthropic")
        if current_key:
            self.io_handler.display_message(f"Current API key: {current_key}")

        new_key = self.io_handler.display_input_prompt("New API key (leave blank to keep current): ").strip()
        if new_key:
            self.settings.set_api_key("anthropic", new_key)
            self.io_handler.display_message("Anthropic API key set successfully")
        self.io_handler.wait_for_input()

    def _set_theme_menu(self):
        themes = self.settings.get_available_themes()
        options = {str(i): theme for i, theme in enumerate(themes, 1)}
        options["0"] = "Back"
        
        content = self.io_handler.display_menu(options, "Theme Selection")
        self.io_handler.display_frame(content, "Set Theme")
        choice = self.io_handler.display_input_prompt("\nSelect theme: ").strip()
        
        if choice == "0":
            return
        elif choice in options:
            self.settings.set_theme(options[choice])
            self.io_handler.display_message(f"Theme set to: {options[choice]}")
        else:
            self.io_handler.display_error("Invalid choice")
            
    def _set_model_menu(self):
        available_models = self.settings.get_available_models()
        
        # Create numbered options for available models
        options = {str(i): f"{model}: {desc}" for i, (model, desc) in enumerate(available_models.items(), 1)}
        options["B"] = "Back"
        
        # Display current model
        current_model = self.settings.get_active_model()
        self.io_handler.display_message(f"\nCurrent model: {current_model or 'Not Set'}")
        
        # Display menu
        content = self.io_handler.display_menu(options, "Select AI Model")
        self.io_handler.display_frame(content, "Set AI Model")
        choice = self.io_handler.display_input_prompt("\nSelect model: ").strip()
        
        if choice == "0":
            return
        elif choice in options:
            model_key = list(available_models.keys())[int(choice) - 1]
            self.settings.set_active_model(model_key)
            self.ai_service = self.ai_manager.get_service()
            self.io_handler.display_message(f"Model set to: {model_key}")
        else:
            self.io_handler.display_error("Invalid choice")
        
    def _display_current_settings(self):
        available_models = self.settings.get_available_models()
        theme = self.settings.get_theme()
        current_model = self.settings.get_active_model()
        model_description = available_models[current_model] if current_model else "Not Set"

        content = f"""[bold]Current Settings:[/bold]

    - Theme: {theme}
    - AI Model: {current_model}
      Description: {model_description}

    [bold]API Keys:[/bold]
    - OpenAI: {'Set' if self.settings.get_api_key('openai') else 'Not Set'}
    - Anthropic: {'Set' if self.settings.get_api_key('anthropic') else 'Not Set'}"""

        self.io_handler.display_frame(content, "Current Settings")
        self.io_handler.wait_for_input()
