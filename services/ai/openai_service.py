from services.ai.base import AIService
from typing import Dict
from openai import OpenAI

class OpenAIService(AIService):
    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=self.settings.get_api_key("openai"))
        active_model = self.settings.get_active_model()
        self.model = self.settings.get_model_name_from_full(active_model)

    def generate_npc_description(self, npc_data: Dict[str, str]) -> str:
        theme_context = self._get_theme_prompt()

        prompt = f"""
        Based on the following character attributes, create detailed GM notes for an NPC {theme_context}.
        Interpret each trait with a sentence and then integrate them into a cohesive and interesting character background.
        The character has the following attributes:
        """

        for trait, value in npc_data.items():
            prompt += f"{trait}: {value}\n"

        prompt += "\nWrite in the style of GM notes, focusing on how these traits define the character's background, motivations, and potential interactions."

        try:
            repsonse = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an RPG Game Master assistant tasked with creating detailed and engaging NPC backgrounds. "
                            "Interpret each provided trait and weave them into a cohesive narrative that can aid the GM in role-playing this character. "
                            "Avoid addressing the player directly; focus on providing notes for the GM."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            return repsonse.choices[0].message.content
        except Exception as e:
            return f"Error generating description: {str(e)}"