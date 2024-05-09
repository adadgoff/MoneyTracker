from typing import Callable

import inquirer

from app.core.language_manager import LanguageManager
from app.entry.entry import Entry, Category
from app.utils.validate_utils import validate_month, validate_day, validate_year, validate_amount


def amount_text(language_manager: LanguageManager, default=None) -> int:
    return int(inquirer.text(
        message=language_manager.get_translation("entry-amount-input"),
        validate=lambda _, amount: validate_amount(amount, language_manager),
        default=default))


def category_list(language_manager: LanguageManager, default=None) -> Category:
    category_choice = inquirer.list_input(
        message=language_manager.get_translation("entry-category-list"),
        choices=[language_manager.get_translation("income"),
                 language_manager.get_translation("expense")],
        default=language_manager.get_translation("income")
        if default is None or default == language_manager.get_translation("income")
        else language_manager.get_translation("expense"))

    if category_choice == language_manager.get_translation("income"):
        return Category.income
    elif category_choice == language_manager.get_translation("expense"):
        return Category.expense
    else:
        raise ValueError("Unknown category")


def description_text(language_manager: LanguageManager, default=None) -> str:
    return (f'{default if default else ""}' +
            input(f'[?] {language_manager.get_translation("entry-description-input")}: {default if default else ""}'))


def year_text(language_manager: LanguageManager, default=None) -> int:
    return int(inquirer.text(
        message=language_manager.get_translation("entry-date-year-input"),
        validate=lambda _, year: validate_year(year, language_manager),
        default=default))


def month_text(language_manager: LanguageManager, default=None) -> int:
    return int(inquirer.text(
        message=language_manager.get_translation("entry-date-month-input"),
        validate=lambda _, month: validate_month(month, language_manager),
        default=default))


def day_text(date_year: int, date_month: int, language_manager: LanguageManager, default=None) -> int:
    return int(inquirer.text(
        message=language_manager.get_translation("entry-date-day-input"),
        validate=lambda _, day: validate_day(date_year, date_month, day, language_manager),
        default=default))


def updating_entry_list(user_entries: list[Entry], language_manager: LanguageManager,
                        get_pretty_entry_str: Callable, default=None) -> Entry:
    pretty_str_entries = [get_pretty_entry_str(entry) for entry in user_entries]
    pretty_str_updating_entry = inquirer.list_input(
        message=language_manager.get_translation("entry-update-list"),
        choices=pretty_str_entries,
        default=default)
    return user_entries[pretty_str_entries.index(pretty_str_updating_entry)]


def deleting_entries_list(user_entries: list[Entry], language_manager: LanguageManager,
                          get_pretty_entry_str: Callable) -> list[Entry]:
    pretty_str_entries = [get_pretty_entry_str(entry) for entry in user_entries]
    pretty_str_deleting_entries = inquirer.checkbox(
        message=language_manager.get_translation("entries-delete"),
        choices=pretty_str_entries)
    deleting_entries = [user_entries[pretty_str_entries.index(pretty_str_deleting_entry)]
                        for pretty_str_deleting_entry in pretty_str_deleting_entries]
    return deleting_entries
