from typing import Dict
from openai import OpenAI

from .base import AIService

class OpenAIService(AIService):
    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=self.config.get_api_key("openai"))
        self.model = self.config.config["providers"]["openai"].get("model", "gpt-3.5-turbo")

    def generate_npc_description(self, npc_data: Dict[str, str]) -> str:
        theme_context = self._get_theme_prompt()

        prompt = f"""
        Create a brief, one-paragraph description (maximum 3 sentences) for a quick NPC encounter {theme_context}.
        The character has the following attributes:
        """

        for trait, value in npc_data.items():
            prompt += f"{trait}: {value}\n"

        prompt += "\nWrite a narrative paragraph describing this character, their appearance, personality, and notable features. Focus on making them memorable and interesting."

        try:
            repsonse = self.client.chat.completions.create(model=self.model,
            messages=[
                {"role": "system", "content": "You are a concise RPG GM assistant. Keep all NPC descriptions brief and focused on essential details only. Avoid flowery language and extensive backstory."},
                {"role": "user", "content": prompt}
            ])

            return repsonse.choices[0].message.content
        except Exception as e:
            return f"Error generating description: {str(e)}"