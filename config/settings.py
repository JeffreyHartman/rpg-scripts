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
            "openai/gpt-4o-mini": "Best for most users. $0.15/$0.60 per 1M I/O tokens",
            "openai/gpt-4o": "More capable than GPT-4o-mini. $2.50/$10.00 per 1M I/O tokens",
            "openai/gpt-3.5-turbo": "Legacy model. 4o is cheaper and more capable. $3.00/$6.00 per 1M I/O tokens",
            "anthropic/claude-3-5-sonnet-latest": "Most capable model, best for complex tasks. $3.00/$15.00 per 1M I/O tokens",
            "anthropic/claude-3-5-haiku-latest": "Balanced performance and cost. $1.00/$5.00 per 1M I/O tokens",
            "anthropic/claude-3-haiku-20240307": "Fastest, most cost-effective model. $0.25/$1.25 per 1M I/O tokens",
        }
        
        # Load or create config
        self.config = self.load_config()

    def load_config(self) -> Dict:
        """Load or create default configuration."""
        if not self.config_file.exists():
            default_config = {
                "current_engine": "mythic2e",
                "theme": "fantasy",
                "ai": {
                    "active_provider": "",
                    "active_model": "",
                    "api_keys": {
                        "openai": "",
                        "anthropic": ""
                    }
                }
            }
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            self.config_file.write_text(json.dumps(default_config, indent=2))
            return default_config
        return json.loads(self.config_file.read_text())

    def save_config(self):
        """Save current configuration to file."""
        self.config_file.write_text(json.dumps(self.config, indent=2))

    # AI methods
    def get_available_models(self) -> Dict[str, str]:
        """Get all available models with their descriptions."""
        return self.available_models

    def get_provider_from_model(self, model: str) -> str:
        """Extract provider from model string."""
        return model.split('/')[0] if '/' in model else ""

    def get_model_name_from_full(self, model: str) -> str:
        """Extract model name from full model string."""
        return model.split('/')[1] if '/' in model else model

    def get_active_model(self) -> str:
        """Get the currently selected model."""
        return self.config["ai"]["active_model"]

    def set_active_model(self, model: str):
        """Set the AI model and automatically set the provider."""
        if model in self.available_models:
            self.config["ai"]["active_model"] = model
            self.config["ai"]["active_provider"] = self.get_provider_from_model(model)
            self.save_config()

    def get_api_key(self, provider: str) -> str:
        """Get the API key for specified provider."""
        return self.config["ai"]["api_keys"].get(provider, "")
    
    def set_api_key(self, provider: str, api_key: str):
        """Set the API key for specified provider."""
        if provider in ["openai", "anthropic"]:  # safelist of valid providers
            if "ai" not in self.config:
                self.config["ai"] = {"api_keys": {}}
            if "api_keys" not in self.config["ai"]:
                self.config["ai"]["api_keys"] = {}
                
            self.config["ai"]["api_keys"][provider] = api_key
            self.save_config()
    
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
