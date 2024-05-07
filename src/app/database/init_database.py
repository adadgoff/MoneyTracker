import os

from app.database.config import ENTRY_DATABASE_PATH

from app.database.config import DELIMITER, USER_DATABASE_PATH
from app.entry.entry import Entry
from app.user.user import User


def init_database():
    if not os.path.exists(ENTRY_DATABASE_PATH):
        with open(ENTRY_DATABASE_PATH, 'w', encoding="utf-8") as f_entry:
            print(DELIMITER.join(Entry.__slots__), file=f_entry)

    if not os.path.exists(USER_DATABASE_PATH):
        with open(USER_DATABASE_PATH, 'w', encoding="utf-8") as f_user:
            print(DELIMITER.join(User.__slots__), file=f_user)
