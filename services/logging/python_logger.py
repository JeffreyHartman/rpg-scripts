import logging
from pathlib import Path
from .logger_interface import LoggerInterface

class PythonLogger(LoggerInterface):
    def __init__(self, logger_name: str):
        if not logging.getLogger().handlers:
            log_dir = Path("logs")
            log_dir.mkdir(exist_ok=True)

            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler(log_dir / "rpg-scripts.log"),
                    logging.StreamHandler()
                ]
            )

        self._logger = logging.getLogger(logger_name)

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str, exc_info=None) -> None:
        self._logger.error(message, exc_info=exc_info)