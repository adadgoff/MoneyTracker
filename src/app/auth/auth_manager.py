import inquirer

from app.auth.auth_service import AuthService
from app.auth.i_auth_manager import IAuthManager
from app.core.context import Context
from app.core.language_manager import LanguageManager, Languages
from app.user.user_exceptions import UserNotFoundException, UserIncorrectDataException, UsernameIsTakenException
from app.utils.console_utils import clear_console


class AuthManager(IAuthManager):
    def __init__(self, language_manager: LanguageManager):
        self.language_manager = language_manager

    def start(self):
        print(self.language_manager.get_translation("auth-menu"), end="\n\n")
        questions = [inquirer.List(name="cmd", message=self.language_manager.get_translation("auth-menu-input"),
                                   choices=[self.language_manager.get_translation("auth-menu-choice-login"),
                                            self.language_manager.get_translation("auth-menu-choice-register"),
                                            self.language_manager.get_translation("auth-menu-choice-change-language"),
                                            self.language_manager.get_translation("app-terminate")])]
        cmd = inquirer.prompt(questions)["cmd"]
        clear_console()
        if cmd == self.language_manager.get_translation("auth-menu-choice-login"):
            self.login()
        elif cmd == self.language_manager.get_translation("auth-menu-choice-register"):
            self.register()
        elif cmd == self.language_manager.get_translation("auth-menu-choice-change-language"):
            self.change_language()
        elif cmd == self.language_manager.get_translation("app-terminate"):
            self.terminate_app()
        else:
            raise ValueError("Unknown command")

    def login(self):
        print(self.language_manager.get_translation("auth-login"))
        try:
            username = inquirer.text(message=self.language_manager.get_translation("auth-login-username"))
            password = inquirer.password(message=self.language_manager.get_translation("auth-login-password"))
            AuthService.login(username=username, password=password)
        except (UserNotFoundException, UserIncorrectDataException):
            Context.ERROR_CONTEXT = self.language_manager.get_translation("auth-login-error")

    def register(self):
        print(self.language_manager.get_translation("auth-register"))
        try:
            username = inquirer.text(message=self.language_manager.get_translation("auth-register-username"))
            password = inquirer.password(message=self.language_manager.get_translation("auth-register-password"))
            AuthService.register(username=username, password=password)
            AuthService.login(username=username, password=password)
        except UsernameIsTakenException:
            Context.ERROR_CONTEXT = self.language_manager.get_translation("auth-register-error")

    def change_language(self):
        questions = [inquirer.List(name="lng", message=self.language_manager.get_translation("app-change-language"),
                                   choices=[self.language_manager.get_translation("app-change-language-english"),
                                            self.language_manager.get_translation("app-change-language-russian")])]
        lng = inquirer.prompt(questions)["lng"]
        Context.START = True
        if lng == self.language_manager.get_translation("app-change-language-english"):
            self.language_manager.language = Languages.en
        elif lng == self.language_manager.get_translation("app-change-language-russian"):
            self.language_manager.language = Languages.ru
        else:
            raise ValueError("Unknown language")

    def terminate_app(self):
        confirm = inquirer.confirm(message=self.language_manager.get_translation("app-terminate-confirm"))
        if confirm:
            print(self.language_manager.get_translation("app-terminated"), end="\n\n")
            exit()
