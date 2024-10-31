# console/mythic2e_menu.py
import sys
from .menu_base import MenuBase
from engines.mythic2e import fate_chart, random_event

class Mythic2eMenu(MenuBase):
    def display(self):
        options = {
            "1": "Fate Check",
            "2": "Random Event",
            "3": "Scene Check",
            "4": "Descriptors",
            "5": "Elements",
        }
        
        while True:
            choice = self.print_menu(options, "Mythic 2e")

            if self.handle_input(choice, options):
                continue
            
            if choice == "1":
                self.fate_check_menu()
            elif choice == "2":
                self.random_event_menu()
            elif choice == "3":
                self.scene_check_menu()
            elif choice == "4":
                self.descriptor_menu()
            elif choice == "5":
                self.element_menu()

    def fate_check_menu(self):
        try:
            chaos_factor = int(input("Chaos Factor: "))
            odds = int(input("Odds (1-10, default 5): ").strip() or "5")
            print(fate_chart.fate_check(chaos_factor, odds))
        except ValueError:
            print("Invalid input. Please try again.")

    def random_event_menu(self):
      while True:
          print("\nPlease choose an option:")
          print("1. Generate Random Event")
          print("2. Generate Descriptor")
          print("3. Generate Element")
          print("4. Generate NPC")
          print("5. Back")
          print("6. Exit")
          print("")

          # get user input
          userInput = input("Enter your choice: ")
          print("")

          # check user input
          if userInput == "1":
              print(random_event.generate_random_event())
          elif userInput == "2":
              print(random_event.generate_descriptor())
          elif userInput == "3":
              self.element_menu()
          elif userInput == "4":
              print(random_event.generate_npc())
          elif userInput == "5":
              return
          elif userInput == "6":
              sys.exit()

    def element_menu(self):
        while True:
            elements = random_event.list_elements()
            print("\nPlease choose an element:")
            for i, element in enumerate(elements, start=1):
                print(f"{i}. {element}")
            print("0. Back")
            print("")

            # get user input
            userInput = input("Enter your choice: ")
            print("")

            # check user input
            if userInput == "0":
                return