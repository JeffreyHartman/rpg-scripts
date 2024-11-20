# console/rpg-scripts.py
from config.settings import Settings
from console.mythic2e_menu import Mythic2eMenu
from console.rich_console import RichConsoleImpl
from services.logging.logger_interface import LoggerInterface
from services.logging.python_logger import PythonLogger

class RPGScripts:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.settings = Settings()
        self.io_handler = RichConsoleImpl()
        self.current_menu = None

    def run(self):
        try:
            self.current_menu = Mythic2eMenu(self.io_handler, self.logger)
            self.current_menu.display()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    logger = PythonLogger("rpg-scripts")
    app = RPGScripts(logger)
    app.run()