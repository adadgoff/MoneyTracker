from csv import DictReader
from datetime import date, datetime
from uuid import UUID

import readchar

from app.core.context import Context
from app.database.config import ENTRY_DATABASE_PATH, DELIMITER
from app.entry.entry import Category, Entry


class EntryRepository:
    @classmethod
    def __create_entry(cls, entry: Entry) -> Entry:
        with open(ENTRY_DATABASE_PATH, 'a', encoding="utf-8") as f_entry:
            print(repr(entry), file=f_entry)
            return entry

    @classmethod
    def __read_entry(cls, uuid: UUID) -> Entry | None:
        entries = EntryRepository.read_user_entries()
        return next((entry for entry in entries if entry.uuid == uuid), None)

    @classmethod
    def __read_entries(cls) -> list[Entry]:
        with open(ENTRY_DATABASE_PATH, 'r', encoding="utf-8") as f_entry:
            entries = list(Entry(uuid=UUID(row["uuid"]),
                                 user_uuid=UUID(row["user_uuid"]),
                                 amount=int(row["amount"]),
                                 category=Category(int(row["category"])),
                                 date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
                                 description=row["description"])
                           for row in DictReader(f_entry, delimiter=DELIMITER))
            return entries

    @classmethod
    def __delete_all_entries(cls) -> None:
        with open(ENTRY_DATABASE_PATH, 'w', encoding="utf-8") as f_entry:
            print(DELIMITER.join(Entry.__slots__), file=f_entry)

    @classmethod
    def create_user_entry(cls, amount: int, category: Category, date: date, description: str) -> Entry:
        entry = Entry(amount, category, date, description)
        return cls.__create_entry(entry)

    @classmethod
    def read_user_entries(cls) -> list[Entry]:
        entries = cls.__read_entries()
        return [entry for entry in entries if entry.user_uuid == Context.CURRENT_USER.uuid]

    @classmethod
    def update_user_entry(cls, updating_entry: Entry) -> list[Entry]:
        updated_entries = list(entry if entry.uuid != updating_entry.uuid else updating_entry
                               for entry in EntryRepository.__read_entries())
        cls.__delete_all_entries()
        for updated_entry in updated_entries:
            cls.__create_entry(updated_entry)
        return updated_entries

    @classmethod
    def delete_user_entries(cls, deleting_entries_uuids: list[UUID]) -> list[Entry]:
        updated_entries = list(entry for entry in EntryRepository.__read_entries()
                               if entry.uuid not in deleting_entries_uuids)
        cls.__delete_all_entries()
        for updated_entry in updated_entries:
            cls.__create_entry(updated_entry)
        return updated_entries
