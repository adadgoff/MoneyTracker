from app.auth.auth_manager import AuthManager
from app.core.context import Context
from app.core.language_manager import Languages, LanguageManager
from app.database.init_database import init_database
from app.entry.entry_manager import EntryManager
from app.utils.console_utils import clear_console
from app.utils.text_colors import TextColors


class App:
    def __init__(self, init_language: Languages):
        self.language_manager: LanguageManager = LanguageManager(init_language)
        self.auth_manager = AuthManager(self.language_manager)
        self.entry_manager = EntryManager(self.language_manager)

    def run(self):
        init_database()

        while True:
            clear_console()

            if Context.START:
                print(f"{TextColors.OKGREEN}{self.language_manager.get_translation("app-info")}{TextColors.ENDC}",
                      end="\n\n")
                Context.START = False

            if Context.ERROR_CONTEXT:
                print(f"{TextColors.FAIL}{Context.ERROR_CONTEXT}{TextColors.ENDC}", end="\n\n")
                Context.ERROR_CONTEXT = None

            if Context.NOTIFICATION_CONTEXT:
                print(f"{TextColors.OKGREEN}{Context.NOTIFICATION_CONTEXT}{TextColors.ENDC}", end="\n\n")
                Context.NOTIFICATION_CONTEXT = None

            if Context.CURRENT_USER:
                self.entry_manager.start()
            else:
                self.auth_manager.start()
