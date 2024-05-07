from rich.console import Console

from app.core.language_manager import LanguageManager


class EntryManager:
    def __init__(self, language_manager: LanguageManager):
        self.console = Console()
        self.language_manager = language_manager

    def run(self):
        pass