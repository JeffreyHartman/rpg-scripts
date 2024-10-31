import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mythic2e import fatechart, randomevent

ENGINES = {
    "mythic2e": "Mythic 2e",
    "mythic1e": "Mythic 1e",
    "une": "UNE",
    "pum": "Plot Unfolding Machine"
}

current_engine = "mythic2e"

def main_menu():
    while True:
        print("Welcome to the RPG Scripts!")
        print("Please choose an option:")
        print("1. Mythic 2e")
        print("2. Dice Roll")
        print("3. Exit")
        print("")

        # get user input
        userInput = input("Enter your choice: ")
        print("")

        # check user input
        if userInput == "1":
            mythic2e_menu()
        elif userInput == "2":
            print("Dice Roll")
        elif userInput == "3":
            sys.exit()
        else:
            print("Invalid input. Please try again.")#
        print("")

def mythic2e_menu():
    while True:
        print("\nPlease choose an option:")
        print("1. Fate Check")
        print("2. Scene Check")
        print("3. Back")
        print("4. Exit")
        print("")

        # get user input
        userInput = input("Enter your choice: ")
        print("")

        # check user input
        if userInput == "1":
            try:
                chaos_factor = int(input("Chaos Factor: "))
                # odds 1 - 10, default 5 if blank
                odds = int(input("Odds (1-10, default 5): ").strip() or "5")
                print(fatechart.fate_check(chaos_factor, odds))
            except ValueError:
                print("Invalid input. Please try again.")
        elif userInput == "2":
            random_event_menu()
        elif userInput == "3":
            return
        elif userInput == "4":
            sys.exit()

def random_event_menu():
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
            print(randomevent.generate_random_event())
        elif userInput == "2":
            print(randomevent.generate_descriptor())
        elif userInput == "3":
            element_menu()
        elif userInput == "4":
            print(randomevent.generate_npc())
        elif userInput == "5":
            return
        elif userInput == "6":
            sys.exit()

def element_menu():
    while True:
        elements = randomevent.list_element_tables()
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

if __name__ == "__main__":
    main_menu()