from datetime import date

from app.entry.entry import Entry, Category
from app.entry.entry_repository import EntryRepository


class EntryService:
    repository = EntryRepository

    @classmethod
    def create_user_entry(cls, amount: int, category: Category, date: date, description: str) -> Entry:
        return cls.repository.create_user_entry(amount, category, date, description)

    @classmethod
    def read_user_entries(cls) -> list[Entry]:
        return cls.repository.read_user_entries()

    @classmethod
    def read_user_balance(cls) -> int:
        user_entries = cls.read_user_entries()
        balance = sum(map(lambda user_entry: user_entry.amount * user_entry.category.value, user_entries))
        return balance

    @classmethod
    def read_user_incomes(cls) -> list[Entry]:
        user_entries = cls.read_user_entries()
        return [user_entry for user_entry in user_entries if user_entry.category == Category.income]

    @classmethod
    def read_user_expenses(cls) -> list[Entry]:
        user_entries = cls.read_user_entries()
        return [user_entry for user_entry in user_entries if user_entry.category == Category.expense]

    @classmethod
    def update_user_entry(cls, updating_entry: Entry) -> list[Entry]:
        return cls.repository.update_user_entry(updating_entry)

    @classmethod
    def delete_user_entries(cls, deleting_entries: list[Entry]) -> list[Entry]:
        deleting_entries_uuids = [entry.uuid for entry in deleting_entries]
        return cls.repository.delete_user_entries(deleting_entries_uuids)

    @classmethod
    def find_user_entries_by_date(cls, date: date) -> list[Entry]:
        user_entries = cls.read_user_entries()
        return [user_entry for user_entry in user_entries if user_entry.date == date]

    @classmethod
    def find_user_entries_by_amount(cls, amount: int) -> list[Entry]:
        user_entries = cls.read_user_entries()
        return [user_entry for user_entry in user_entries if user_entry.amount == amount]
