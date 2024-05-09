from abc import ABC, abstractmethod


class IEntryManager(ABC):
    """
    Interface for EntryManager.
    """

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def incomes(self):
        pass

    @abstractmethod
    def expenses(self):
        pass

    @abstractmethod
    def create_user_entry(self):
        pass

    @abstractmethod
    def update_user_entry(self):
        pass

    @abstractmethod
    def delete_user_entries(self):
        pass

    @abstractmethod
    def find_user_entries_by_category(self):
        pass

    @abstractmethod
    def find_user_entries_by_date(self):
        pass

    @abstractmethod
    def find_user_entries_by_amount(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def terminate_app(self):
        pass
