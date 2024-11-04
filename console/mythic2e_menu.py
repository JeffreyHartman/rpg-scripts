# console/mythic2e_menu.py
from .ascii_components import ASCIIMenuBase
from engines.mythic2e import fate_chart, random_event, scene_check
from .ascii_components import ASCIIMenuBase
from services.ai.openai_service import OpenAIService

class Mythic2eMenu(ASCIIMenuBase):
    def __init__(self):
        super().__init__()
        self.ai_service = OpenAIService()

    def display(self):
        options = {
            "1": "Fate Check",
            "2": "Random Event",
            "3": "Scene Check",
            "4": "Descriptors",
            "5": "Elements",
            "6": "Generate NPC",
            "C": "Change Game Engine",
            "S": "Settings",
            "Q": "Quit"
        }
        
        while True:
            content = self.ascii.create_menu(options, self.width)
            self.display_frame(content, "Mythic 2e Game Master Emulator")
            
            choice = input("\nEnter your choice: ").upper()
            if self.handle_input(choice, options):
                continue
            
            if choice == "1":
                self.fate_check_menu()
            elif choice == "2":
                result =random_event.generate_random_event()
                self.display_result(result)
            elif choice == "3":
                self.scene_check_menu()
            elif choice == "4":
                result = random_event.generate_descriptor()
                self.display_result(result)
            elif choice == "5":
                self.element_menu()
            elif choice == "6":
                self.npc_menu()
                # result = random_event.generate_npc()
                # self.display_result(result)
    
    def fate_check_menu(self):
        try:
            self.display_frame(
                ["Enter Chaos Factor (current: {})".format(self.chaos_factor),
                 "Enter odds (1-10, default 5)"],
                "Fate Check"
            )
            
            chaos_input = input("\nChaos Factor: ").strip()
            self.chaos_factor = int(chaos_input) if chaos_input else self.chaos_factor
            
            odds = int(input("Odds: ").strip() or "5")
            result = fate_chart.fate_check(self.chaos_factor, odds)
            
            self.display_result(result)
            
        except ValueError:
            self.display_result("Invalid input. Please try again.")

    def scene_check_menu(self):
        try:
            self.display_frame(
                ["Enter Chaos Factor (current: {})".format(self.chaos_factor)],
                "Scene Check"
            )
            
            chaos_input = input("\nChaos Factor: ").strip()
            self.chaos_factor = int(chaos_input) if chaos_input else self.chaos_factor
            
            result = scene_check.generate_scene_check(self.chaos_factor)
            
            self.display_result(result)
            
        except ValueError:
            self.display_result("Invalid input. Please try again.")
                
    def element_menu(self):
        while True:
            elements = random_event.list_elements()
            
            # Create numbered options dictionary
            options = {str(i): element for i, element in enumerate(elements, start=1)}
            options["0"] = "Back"
            
            # Display the menu
            content = self.ascii.create_menu(options, self.width)
            self.display_frame(content, "Element Generator")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "0":
                break
            elif choice in options:
                try:
                    # Generate the selected element type
                    element_type = options[choice]
                    result = random_event.generate_element(element_type)
                    self.display_result(result)
                except Exception as e:
                    self.display_result(f"Error generating element: {str(e)}")
            else:
                self.display_result("Invalid choice. Please try again.")

    def npc_menu(self):
        npc_data = random_event.generate_npc()
        self.display_result(npc_data)

        print("\nWould you like an AI-generated description? (y/n)")
        choice = input().strip().lower()
        if choice == "y":
            ai_description = self.ai_service.generate_npc_description(npc_data)
            self.display_result(ai_description)