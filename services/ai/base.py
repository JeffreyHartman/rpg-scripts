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
    
    def _build_system_prompt(self) -> str:
        return (
            "You are an RPG Game Master assistant tasked with creating detailed and engaging NPC backgrounds. "
            "Interpret each provided trait and weave them into a cohesive narrative that can aid the GM in role-playing this character. "
            "Avoid addressing the player directly; focus on providing notes for the GM."
        )
    
    def _build_character_prompt(self, npc_data: Dict[str, str]) -> str:
        prompt = f"""
        Based on the following character attributes, create detailed GM notes for an NPC {self._get_theme_prompt()}.
        For each trait section in your output, reiterate the attribute and what was rolled for it.
        Interpret each trait with a sentence and then integrate them into a cohesive and interesting character background.
        The character has the following attributes:
        """

        for trait, value in npc_data.items():
            prompt += f"{trait}: {value}\n"

        prompt += "\nWrite in the style of GM notes, focusing on how these traits define the character's background, motivations, and potential interactions."
        return prompt