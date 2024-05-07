from app.auth.auth_manager import AuthManager
from app.core.contexts import CURRENT_USER
from app.core.language_manager import Languages, LanguageManager
from app.database.init_database import init_database
from app.entry.entry_manager import EntryManager


class App:
    def __init__(self, init_language: Languages):
        language_manager: LanguageManager = LanguageManager(init_language)
        self.auth_manager = AuthManager(language_manager)
        self.entry_manager = EntryManager(language_manager)

    def run(self):
        init_database()

        while True:
            self.auth_manager.run()
            if CURRENT_USER:
                self.entry_manager.run()
