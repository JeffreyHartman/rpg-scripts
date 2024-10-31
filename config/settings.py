# config/settings.py
class Settings:
    def __init__(self):
        self.engines = {
            "mythic2e": "Mythic 2e",
            "mythic1e": "Mythic 1e",
            "une": "UNE",
            "pum": "Plot Unfolding Machine"
        }
        self.current_engine = "mythic2e"