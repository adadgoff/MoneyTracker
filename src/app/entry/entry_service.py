from datetime import date
from uuid import UUID



class EntryService:
    repository = EntryRepository

    @classmethod
    def create_entry(cls, amount: int, category: Category, date: date, description: str) -> Entry:
        return cls.repository.create_entry(amount, category, date, description)

    @classmethod
    def read_current_user_entries(cls) -> list[Entry]:
        return cls.repository.read_current_user_entries()

    @classmethod
    def read_user_balance(cls) -> int:
        user_entries = cls.read_current_user_entries()

    @classmethod
    def read_user_incomes(cls) -> list[Entry]:
        pass

    @classmethod
    def read_user_expenses(cls) -> list[Entry]:
        pass

    @classmethod
    def update_entry(cls, uuid: UUID) -> Entry:
        pass

    @classmethod
    def delete_entry(cls, uuid: UUID) -> Entry:
        pass

    @classmethod
    def find_by_category(cls, category: Category) -> list[Entry]:
        pass

    @classmethod
    def find_by_date(cls, date: date) -> list[Entry]:
        pass

    @classmethod
    def find_by_amount(cls, amount: int) -> list[Entry]:
        pass

