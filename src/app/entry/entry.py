from datetime import date
from enum import Enum
from uuid import uuid4, UUID

from app.core.context import Context
from app.database.config import DELIMITER


class Category(Enum):
    expense = -1
    income = 1


class Entry:
    __slots__ = ("uuid", "user_uuid", "amount", "category", "date", "description")

    def __init__(self, amount: int, category: Category, date: date, description: str,
                 uuid: UUID = uuid4(), user_uuid: UUID | None = None):  # noqa. For creating instance.
        self.uuid: UUID = uuid
        self.user_uuid: UUID = user_uuid if user_uuid else Context.CURRENT_USER.uuid
        self.amount: int = amount
        self.category: Category = category
        self.date: date = date
        self.description: str = description

    def __repr__(self):
        return DELIMITER.join(map(str, [self.uuid,
                                        self.user_uuid,
                                        self.amount,
                                        self.category.value,
                                        self.date,
                                        self.description]))

    def to_language_str(self,
                        lng_date: str,
                        lng_category: str,
                        lng_amount: str,
                        lng_description: str,
                        lng_expense: str,
                        lng_income: str) -> str:
        """
        Get pretty str for printing in selected language.
        :param lng_date: writing the word "date" in the selected language.
        :param lng_category: writing the word "category" in the selected language.
        :param lng_amount: writing the word "amount" in the selected language.
        :param lng_description: writing the word "description" in the selected language.
        :param lng_expense: writing the word "expense" in the selected language.
        :param lng_income: writing the word "income" in the selected language.
        :return: pretty str for printing in selected language.
        """
        return " | ".join([f"{lng_date}: {self.date}",
                           f"{lng_category}: {lng_income if self.category.value > 0 else lng_expense}",
                           f"{lng_amount}: {self.amount}",
                           f"{lng_description}: {self.description}"])
