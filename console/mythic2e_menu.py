# console/mythic2e_menu.py
from .menu_base import MenuBase
from engines.mythic2e import fate_chart, random_event, scene_check
from .io_handler import IOHandler

class Mythic2eMenu(MenuBase):
    def __init__(self, io_handler: IOHandler):
        super().__init__(io_handler)
        self.chaos_factor = 5  # Default chaos factor

    def display(self):
        options = {
            "1": "Fate Check",
            "2": "Random Event",
            "3": "Scene Check",
            "4": "Descriptors",
            "5": "Elements",
            "6": "Generate NPC",
        }
        system_options = {
            "C": "Change Game Engine",
            "S": "Settings",
            "Q": "Quit"
        }
        
        while True:
            options_table = self.io_handler.display_menu(options, "Game Options")
            system_table = self.io_handler.display_menu(system_options, "System Options")
            content = [options_table, system_table]
            self.io_handler.display_frame(content, "Mythic 2e Game Master Emulator")
            
            choice = self.io_handler.display_input_prompt("\nEnter your choice: ").strip().upper()
            if self.handle_input(choice, {**options, **system_options}):
                continue
            
            if choice == "1":
                self.fate_check_menu()
            elif choice == "2":
                result =random_event.generate_random_event()
                self.io_handler.display_result(result)
            elif choice == "3":
                self.scene_check_menu()
            elif choice == "4":
                result = random_event.generate_descriptor()
                self.io_handler.display_result(result)
            elif choice == "5":
                self.element_menu()
            elif choice == "6":
                self.npc_menu()
                # result = random_event.generate_npc()
                # self.display_result(result)
    
    def fate_check_menu(self):
        try:
            content = [
                f"Enter Chaos Factor (current: {self.chaos_factor})",
                "Enter odds (1-10, default 5)"
            ]
            self.io_handler.display_frame(content, "Fate Check")
            
            chaos_input = self.io_handler.display_input_prompt("\nChaos Factor: ").strip()
            self.chaos_factor = int(chaos_input) if chaos_input else self.chaos_factor
            
            odds_input = self.io_handler.display_input_prompt("Odds: ").strip()
            odds = int(odds_input) if odds_input else 5            
            result = fate_chart.fate_check(self.chaos_factor, odds)
            self.io_handler.display_result(result)
            
        except ValueError:
            self.io_handler.display_error("Invalid input. Please try again.")

    def scene_check_menu(self):
        try:
            content = [f"Enter Chaos Factor (current: {self.chaos_factor})"]
            self.io_handler.display_frame(content, "Scene Check")

            
            chaos_input = self.io_handler.display_input_prompt("\nChaos Factor: ").strip()
            self.chaos_factor = int(chaos_input) if chaos_input else self.chaos_factor

            result = scene_check.generate_scene_check(self.chaos_factor)
            self.io_handler.display_result(result)
            
        except ValueError:
            self.io_handler.display_error("Invalid input. Please try again.")
                
    def element_menu(self):
        while True:
            elements = random_event.list_elements()
            
            # Create numbered options dictionary
            options = {str(i): element for i, element in enumerate(elements, start=1)}
            options["0"] = "Back"
            
            content = self.io_handler.display_menu(options, "Element Generator")
            self.io_handler.display_frame(content, "Element Generator")
        
            choice = self.io_handler.display_input_prompt("\nEnter your choice: ").strip()
            
            if choice == "0":
                break
            elif choice in options:
                try:
                    # Generate the selected element type
                    element_type = options[choice]
                    result = random_event.generate_element(element_type)
                    self.io_handler.display_result(result)
                except Exception as e:
                    self.io_handler.display_error(f"Error generating element: {str(e)}")
            else:
                self.io_handler.display_error("Invalid choice. Please try again.")
                
    def npc_menu(self):
        npc_data = random_event.generate_npc()
        self.io_handler.display_result(npc_data)

        choice = self.io_handler.display_input_prompt("\nWould you like an AI-generated description? (y/n): ").strip().lower()
        if choice == "y":
            ai_description = self.ai_service.generate_npc_description(npc_data)
            self.io_handler.display_result(ai_description)
        