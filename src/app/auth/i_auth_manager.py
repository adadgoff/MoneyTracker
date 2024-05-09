from abc import ABC, abstractmethod


class IAuthManager(ABC):
    """
    Interface for AuthManager.
    """
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def change_language(self):
        pass

    @abstractmethod
    def terminate_app(self):
        pass
