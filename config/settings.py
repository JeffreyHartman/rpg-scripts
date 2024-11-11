# config/settings.py
from typing import Dict, List
from pathlib import Path
import json

class Settings:
    def __init__(self):
        self.config_file = Path.home() / ".rpg-scripts" / "settings.json"
        
        # Define all available themes and their prompts
        self.themes = {
            "fantasy": "in a high fantasy setting with magic and medieval technology",
            "scifi": "in a sci-fi setting with advanced technology and space travel",
            "modern": "in a contemporary setting with current technology",
            "horror": "in a dark and frightening setting with supernatural elements",
            "cyberpunk": "in a high-tech dystopian future with advanced cyber technology",
            "grimdark": "in a grim and dark setting where morality is ambiguous"
        }

        # Define available engines
        self.engines = {
            "mythic2e": "Mythic 2e",
            "mythic1e": "Mythic 1e",
            "une": "UNE",
            "pum": "Plot Unfolding Machine"
        }
        
        self.available_models = {
            "openai": {
                "gpt-4o-mini": "gpt-4o-mini - Best for most users, $0.60/1M output tokens",
                "gpt-4o": "gpt-4o - More capable than GPT-4o-mini, at $10.00/1M output tokens",
                "gpt-3.5-turbo": "gpt-3.5-turbo - Legacy model. 4o is cheaper and more capable. $3.00/1M output tokens",                
            }
        }

        # Load or create config
        self.config = self.load_config()

    def load_config(self) -> Dict:
        if not self.config_file.exists():
            default_config = {
                "current_engine": "mythic2e",
                "theme": "fantasy",
                "ai_provider": {
                    "active": "openai",
                    "providers": {
                        "openai": {
                            "api_key": "",
                            "model": "gpt-3.5-turbo"
                        }
                    }
                }
            }
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            self.config_file.write_text(json.dumps(default_config, indent=2))
            return default_config
        return json.loads(self.config_file.read_text())

    def get_available_models(self, provider: str) -> List[str]:
        """Get list of available models for a provider."""
        return self.available_models.get(provider, [])

    def get_ai_model(self, provider: str) -> str:
        """Get the currently selected model for a provider."""
        return self.config["ai_provider"]["providers"].get(
            provider, {}).get("model", "gpt-3.5-turbo")

    def set_ai_model(self, provider: str, model: str):
        """Set the model for a provider."""
        if model in self.available_models.get(provider, []):
            if provider not in self.config["ai_provider"]["providers"]:
                self.config["ai_provider"]["providers"][provider] = {}
            self.config["ai_provider"]["providers"][provider]["model"] = model
            self.save_config()
            
    def save_config(self):
        self.config_file.write_text(json.dumps(self.config, indent=2))

    # Theme methods
    def get_available_themes(self) -> List[str]:
        return list(self.themes.keys())

    def get_theme(self) -> str:
        return self.config.get("theme", "fantasy")

    def get_theme_prompt(self) -> str:
        current_theme = self.get_theme()
        return self.themes.get(current_theme, self.themes["fantasy"])

    def set_theme(self, theme: str):
        if theme in self.themes:
            self.config["theme"] = theme
            self.save_config()

    # Engine methods
    def get_available_engines(self) -> Dict[str, str]:
        return self.engines

    def get_current_engine(self) -> str:
        return self.config.get("current_engine", "mythic2e")

    def set_current_engine(self, engine: str):
        if engine in self.engines:
            self.config["current_engine"] = engine
            self.save_config()

    # AI provider methods
    def get_api_key(self, provider: str) -> str:
        return self.config["ai_provider"]["providers"].get(provider, {}).get("api_key", "")

    def set_api_key(self, provider: str, api_key: str):
        if "ai_provider" not in self.config:
            self.config["ai_provider"] = {"providers": {}}
        if provider not in self.config["ai_provider"]["providers"]:
            self.config["ai_provider"]["providers"][provider] = {}
        self.config["ai_provider"]["providers"][provider]["api_key"] = api_key
        self.save_config()