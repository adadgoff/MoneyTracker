from datetime import date

import inquirer
import readchar

from app.auth.auth_service import AuthService
from app.core.context import Context
from app.core.language_manager import LanguageManager
from app.entry.entry import Entry, Category
from app.entry.entry_service import EntryService
from app.entry.i_entry_manager import IEntryManager
from app.utils.components_utils import amount_text, category_list, description_text, year_text, month_text, day_text, \
    updating_entry_list, deleting_entries_list
from app.utils.console_utils import clear_console


class EntryManager(IEntryManager):
    def __init__(self, language_manager: LanguageManager):
        self.language_manager = language_manager

    def get_pretty_entry_str(self, entry: Entry) -> str:
        return entry.to_language_str(lng_date=self.language_manager.get_translation("date"),
                                     lng_category=self.language_manager.get_translation("category"),
                                     lng_amount=self.language_manager.get_translation("amount"),
                                     lng_description=self.language_manager.get_translation("description"),
                                     lng_income=self.language_manager.get_translation("income"),
                                     lng_expense=self.language_manager.get_translation("expense"))

    def start(self):
        print(self.language_manager.get_translation("entry-menu"), end="\n\n")
        questions = [inquirer.List(name="cmd", message=self.language_manager.get_translation("entry-menu-input"),
                                   choices=[self.language_manager.get_translation("entry-menu-choice-balance"),
                                            self.language_manager.get_translation("entry-menu-choice-incomes"),
                                            self.language_manager.get_translation("entry-menu-choice-expenses"),
                                            self.language_manager.get_translation("entry-menu-choice-create"),
                                            self.language_manager.get_translation("entry-menu-choice-update"),
                                            self.language_manager.get_translation("entry-menu-choice-delete"),
                                            self.language_manager.get_translation("entry-menu-choice-find-by-category"),
                                            self.language_manager.get_translation("entry-menu-choice-find-by-date"),
                                            self.language_manager.get_translation("entry-menu-choice-find-by-amount"),
                                            self.language_manager.get_translation("entry-menu-choice-logout"),
                                            self.language_manager.get_translation("app-terminate")])]
        cmd = inquirer.prompt(questions)["cmd"]
        clear_console()
        if cmd == self.language_manager.get_translation("entry-menu-choice-balance"):
            self.balance()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-incomes"):
            self.incomes()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-expenses"):
            self.expenses()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-create"):
            self.create_user_entry()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-update"):
            self.update_user_entry()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-delete"):
            self.delete_user_entries()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-find-by-category"):
            self.find_user_entries_by_category()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-find-by-date"):
            self.find_user_entries_by_date()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-find-by-amount"):
            self.find_user_entries_by_amount()
        elif cmd == self.language_manager.get_translation("entry-menu-choice-logout"):
            self.logout()
        elif cmd == self.language_manager.get_translation("app-terminate"):
            self.terminate_app()
        else:
            raise ValueError("Unknown command")

    def balance(self):
        user_balance = EntryService.read_user_balance()
        print(self.language_manager.get_translation("entry-balance") + str(user_balance), end="\n")
        print(self.language_manager.get_translation("app-menu-back"))
        readchar.readchar()

    def incomes(self):
        user_incomes = EntryService.read_user_incomes()
        print(self.language_manager.get_translation("entry-incomes"))
        if not user_incomes:
            print(self.language_manager.get_translation("no-incomes"))
        for user_income in user_incomes:
            print(self.get_pretty_entry_str(user_income))
        print('\n' + self.language_manager.get_translation("app-menu-back"))
        readchar.readchar()

    def expenses(self):
        user_expenses = EntryService.read_user_expenses()
        print(self.language_manager.get_translation("entry-expenses"))
        if not user_expenses:
            print(self.language_manager.get_translation("no-expenses"))
        for user_expense in user_expenses:
            print(self.get_pretty_entry_str(user_expense))
        print('\n' + self.language_manager.get_translation("app-menu-back"))
        readchar.readchar()

    def create_user_entry(self):
        print(self.language_manager.get_translation("entry-create"))
        amount: int = amount_text(self.language_manager)
        category: Category = category_list(self.language_manager)
        description: str = description_text(self.language_manager)
        date_year: int = year_text(self.language_manager)
        date_month: int = month_text(self.language_manager)
        date_day: int = day_text(date_year, date_month, self.language_manager)
        EntryService.create_user_entry(amount=amount,
                                       category=category,
                                       date=date(year=date_year, month=date_month, day=date_day),
                                       description=description)
        Context.NOTIFICATION_CONTEXT = self.language_manager.get_translation("entry-created-successfully")

    def update_user_entry(self):
        print(self.language_manager.get_translation("entry-update"))
        user_entries = EntryService.read_user_entries()

        if not user_entries:
            print(self.language_manager.get_translation("no-entries"))
            print(self.language_manager.get_translation("app-menu-back"))
            readchar.readchar()
            return

        updating_entry: Entry = updating_entry_list(user_entries=user_entries,
                                                    language_manager=self.language_manager,
                                                    get_pretty_entry_str=self.get_pretty_entry_str)

        amount: int = amount_text(self.language_manager, default=updating_entry.amount)
        category: Category = category_list(self.language_manager, default=updating_entry.category)
        description: str = description_text(self.language_manager, default=updating_entry.description)
        date_year: int = year_text(self.language_manager, default=updating_entry.date.year)
        date_month: int = month_text(self.language_manager, default=updating_entry.date.month)
        date_day: int = day_text(date_year, date_month, self.language_manager, default=updating_entry.date.day)

        updating_entry.amount = amount
        updating_entry.category = category
        updating_entry.description = description
        updating_entry.date = date(year=date_year, month=date_month, day=date_day)
        EntryService.update_user_entry(updating_entry=updating_entry)
        Context.NOTIFICATION_CONTEXT = self.language_manager.get_translation("entry-updated-successfully")

    def delete_user_entries(self):
        print(self.language_manager.get_translation("entries-delete"))
        user_entries = EntryService.read_user_entries()

        if not user_entries:
            print(self.language_manager.get_translation("no-entries"))
            print(self.language_manager.get_translation("app-menu-back"))
            readchar.readchar()
            return

        deleting_entries: list[Entry] = deleting_entries_list(user_entries=user_entries,
                                                              language_manager=self.language_manager,
                                                              get_pretty_entry_str=self.get_pretty_entry_str)
        EntryService.delete_user_entries(deleting_entries=deleting_entries)
        confirm = inquirer.confirm(message=self.language_manager.get_translation("entry-delete-confirm"))
        if confirm:
            Context.NOTIFICATION_CONTEXT = self.language_manager.get_translation("entry-deleted-successfully")

    def find_user_entries_by_category(self):
        print(self.language_manager.get_translation("entry-find-by-category"))
        category: Category = category_list(self.language_manager)
        clear_console()
        if category == category.income:
            self.incomes()
        elif category == category.expense:
            self.expenses()
        else:
            raise ValueError("Unknown category")

    def find_user_entries_by_date(self):
        print(self.language_manager.get_translation("entry-find-by-date"))
        date_year: int = year_text(self.language_manager)
        date_month: int = month_text(self.language_manager)
        date_day: int = day_text(date_year, date_month, self.language_manager)

        print('\n' + self.language_manager.get_translation("entries-found"))
        user_entries_by_date = EntryService.find_user_entries_by_date(
            date=date(year=date_year, month=date_month, day=date_day))
        if not user_entries_by_date:
            print(self.language_manager.get_translation("no-entries"))
        for user_entry in user_entries_by_date:
            print(self.get_pretty_entry_str(user_entry))

        print('\n' + self.language_manager.get_translation("app-menu-back"))
        readchar.readchar()

    def find_user_entries_by_amount(self):
        print(self.language_manager.get_translation("entry-find-by-amount"))
        amount: int = amount_text(self.language_manager)

        print('\n' + self.language_manager.get_translation("entries-found"))
        user_entries_by_amount = EntryService.find_user_entries_by_amount(amount=amount)
        if not user_entries_by_amount:
            print(self.language_manager.get_translation("no-entries"))
        for user_entry in user_entries_by_amount:
            print(self.get_pretty_entry_str(user_entry))

        print('\n' + self.language_manager.get_translation("app-menu-back"))
        readchar.readchar()

    def logout(self):
        confirm = inquirer.confirm(message=self.language_manager.get_translation("auth-logout-confirm"))
        if confirm:
            AuthService.logout()

    def terminate_app(self):
        confirm = inquirer.confirm(message=self.language_manager.get_translation("app-terminate-confirm"))
        if confirm:
            print(self.language_manager.get_translation("app-terminated"), end="\n\n")
            exit()
