from services.ai.base import AIService
from typing import Dict
from openai import OpenAI

class OpenAIService(AIService):
    def __init__(self):
        super().__init__()
        self.provider = "openai"
        self.client = OpenAI(api_key=self.settings.get_api_key("openai"))
        active_model = self.settings.get_active_model()
        self.model = self.settings.get_model_name_from_full(active_model)

    def generate_npc_description(self, npc_data: Dict[str, str]) -> str:
        try:
            repsonse = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._build_system_prompt()},
                    {"role": "user", "content": self._build_character_prompt(npc_data)},
                ],
            )
            return repsonse.choices[0].message.content
        except Exception as e:
            return f"Error generating description: {str(e)}"