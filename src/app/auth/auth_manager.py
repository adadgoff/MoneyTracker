from pprint import pprint

import inquirer
from app.core.language_manager import LanguageManager
from rich.console import Console


class AuthManager:
    def __init__(self, language_manager: LanguageManager):
        self.console = Console()
        self.language_manager = language_manager

    def run(self):
        questions = [
            inquirer.List(
                "cmd",
                message=self.language_manager.get_translation("auth-info-message"),
                choices=[self.language_manager.get_translation("auth-choice-1"),
                         self.language_manager.get_translation("auth-choice-2"),
                         self.language_manager.get_translation("auth-choice-3"),
                         self.language_manager.get_translation("auth-choice-4")],
            ),
        ]

        answers = inquirer.prompt(questions)
        pprint(answers)

