from app.user.user import User
from app.user.user_repository import UserRepository


class UserService:
    repository = UserRepository

    @classmethod
    def create_user(cls, username: str, password: str) -> User:
        return cls.repository.create_user(username, password)

    @classmethod
    def read_user(cls, username: str) -> User:
        return cls.repository.read_user(username)
