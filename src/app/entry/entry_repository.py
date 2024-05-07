from csv import DictReader
from datetime import date



class EntryRepository:
    @classmethod
    def create_entry(cls, amount: int, category: Category, date: date, description: str) -> Entry:
        with open(ENTRY_DATABASE_PATH, 'a', encoding="utf-8") as f_entry:
            entry = Entry(amount, category, date, description)
            print(repr(entry), file=f_entry)
            return entry

    @classmethod
    def read_current_user_entries(cls) -> list[Entry]:
        with open(ENTRY_DATABASE_PATH, 'r', encoding="utf-8") as f_entry:
            entries = (Entry(**d) for d in DictReader(f_entry, delimiter=DELIMITER))
            return [entry for entry in entries if entry.user_uuid == CURRENT_USER.uuid]
