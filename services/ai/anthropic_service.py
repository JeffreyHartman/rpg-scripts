from services.ai.base import AIService
from typing import Dict
from anthropic import Anthropic

class AnthropicService(AIService):
    def __init__(self):
        super().__init__()
        self.provider = "anthropic"
        self.client = Anthropic(api_key=self.settings.get_api_key("anthropic"))
        active_model = self.settings.get_active_model()
        self.model = self.settings.get_model_name_from_full(active_model)

    def generate_npc_description(self, npc_data: Dict[str, str]) -> str:
        try:
            response = self.client.messages.create(
                model = self.model,
                max_tokens = 1000,
                system = self._build_system_prompt(),
                messages = [
                    {
                        "role": "user", "content": self._build_character_prompt(npc_data)
                    }
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating description: {str(e)}"