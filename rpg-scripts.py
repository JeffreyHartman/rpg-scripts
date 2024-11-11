# console/rpg-scripts.py
from config.settings import Settings
from console.mythic2e_menu import Mythic2eMenu
from console.rich_console import RichConsoleImpl

class RPGScripts:
    def __init__(self):
        self.settings = Settings()
        self.io_handler = RichConsoleImpl()
        self.current_menu = None

    def run(self):
        # Start with default engine (Mythic 2e)
        self.current_menu = Mythic2eMenu(self.io_handler)
        self.current_menu.display()

if __name__ == "__main__":
    app = RPGScripts()
    app.run()