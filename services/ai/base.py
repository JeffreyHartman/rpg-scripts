# services/ai/base.py
from abc import ABC, abstractmethod
from typing import Dict
from config.settings import Settings

class AIService(ABC):
    def __init__(self):
        self.settings = Settings()
    
    @abstractmethod
    def generate_npc_description(self, npc_data: Dict[str, str]) -> str:
        pass

    def _get_theme_prompt(self) -> str:
        return self.settings.get_theme_prompt()

    def get_api_key(self, provider: str = "openai") -> str:
        return self.settings.get_api_key(provider)