from datetime import date
from enum import Enum
from uuid import uuid4, UUID



class Category(Enum):
    expense = "Расход"
    income = "Доход"


class Entry:
    __slots__ = ("uuid", "user_uuid", "amount", "category", "date", "description")

    def __init__(self, amount: int, category: Category, date: date, description: str):
        self.uuid: UUID = uuid4()
        self.user_uuid: UUID = CURRENT_USER.uuid
        self.amount: int = amount
        self.category: Category = category
        self.date: date = date
        self.description: str = description

    def __repr__(self):
        return DELIMITER.join([str(self.uuid),
                               str(self.user_uuid),
                               str(self.amount),
                               self.category.value,
                               str(self.date),
                               self.description])
