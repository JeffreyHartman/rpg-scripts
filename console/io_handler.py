from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IOHandler(ABC):
    @abstractmethod
    def clear_screen(self):
        pass

    @abstractmethod
    def display_result(self, result: str):
        pass

    @abstractmethod
    def display_frame(self, content: List[str], title: str):
        pass

    @abstractmethod
    def display_menu(self, options: Dict[str, str], title: str = None):
        pass

    @abstractmethod
    def display_input_prompt(self, prompt: str) -> str:
        pass

    @abstractmethod
    def display_error(self, message: str):
        pass

    @abstractmethod
    def display_message(self, message: str):
        pass
    
    @abstractmethod
    def wait_for_input(self):
        pass