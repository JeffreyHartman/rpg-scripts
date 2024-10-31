# rpg-scripts.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from console import Mythic2eMenu
from config.settings import Settings

class RPGScripts:
    def __init__(self):
        self.settings = Settings()
        self.current_menu = None

    def run(self):
        # Start with default engine (Mythic 2e)
        self.current_menu = Mythic2eMenu()
        self.current_menu.display()

if __name__ == "__main__":
    app = RPGScripts()
    app.run()