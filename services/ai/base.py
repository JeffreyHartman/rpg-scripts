from abc import ABC, abstractmethod
from typing import Optional, Dict
import json
import os
from pathlib import Path

class AIConfig:
    def __init__(self):
        self.config_file = Path.home() / ".rpg-scripts" / "ai_config.json"
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, str]:
        if not self.config_file.exists():
            default_config = {
                "active_provider": "openai",
                "theme": "fantasy",
                "providers": {
                    "openai": {
                        "api_key": "",
                        "model": "gpt-3.5-turbo",
                    }
                }
            }
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            self.config_file.write_text(json.dumps(default_config, indent=2))
            return default_config
        return json.loads(self.config_file.read_text())
    
    def save_config(self):
        self.config_file.write_text(json.dumps(self.config, indent=2))

    def get_api_key(self, provider: str) -> str:
        return self.config["providers"].get(provider, {}).get("api_key", "")
    
    def set_api_key(self, provider: str, api_key: str):
        if provider not in self.config["providers"]:
            self.config["providers"][provider] = {}
        self.config["providers"][provider]["api_key"] = api_key
        self.save_config()

    def get_theme(self) -> str:
        return self.config.get("theme", "fantasy")
    
    def set_theme(self, theme: str):
        self.config["theme"] = theme
        self.save_config()

class AIService(ABC):
    def __init__(self):
        self.config = AIConfig()

    @abstractmethod
    def generate_npc_description(self, npc_data: dict[str, str]) -> str:
        pass

    def _get_theme_prompt(self) -> str:
        theme_prompts = {
            "fantasy": "in a high fantasy setting with magic and medieval technology",
            "scifi": "in a sci-fi setting with advanced technology and space travel",
        }
        return theme_prompts.get(self.config.get_theme(), theme_prompts["fantasy"])
    
    
        
