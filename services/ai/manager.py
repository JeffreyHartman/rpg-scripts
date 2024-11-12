from config.settings import Settings
from services.ai.base import AIService
from services.ai.openai_service import OpenAIService
from services.ai.anthropic_service import AnthropicService

class AIServiceManager:
    def __init__(self):
        self._current_service = None
        self.settings = Settings()

    def get_service(self) -> AIService:
        """Get or create AI service based on settings."""
        active_model = self.settings.get_active_model()
        provider = self.settings.get_provider_from_model(active_model)

        if self._current_service is None or self._current_service.provider != provider:
            if provider == "openai":
                self._current_service = OpenAIService()
            elif provider == "anthropic":
                self._current_service = AnthropicService()
            else:
                raise ValueError(f"Invalid provider: {provider}")
        return self._current_service