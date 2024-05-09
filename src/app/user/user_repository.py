from csv import DictReader
from uuid import UUID

from app.auth.hasher import get_password_hash
from app.database.config import USER_DATABASE_PATH, DELIMITER
from app.user.user import User
from app.user.user_exceptions import UsernameIsTakenException


class UserRepository:
    @classmethod
    def create_user(cls, username: str, password: str) -> User:
        with open(USER_DATABASE_PATH, 'a', encoding="utf-8") as f_user:
            if cls.read_user(username):
                raise UsernameIsTakenException

            user = User(username, get_password_hash(password))
            print(repr(user), file=f_user)
            return user

    @classmethod
    def read_user(cls, username: str) -> User | None:
        with open(USER_DATABASE_PATH, 'r', encoding="utf-8") as f_user:
            users = (User(uuid=UUID(row["uuid"]),
                          username=row["username"],
                          password=row["password"]) for row in DictReader(f_user, delimiter=DELIMITER))
            return next((user for user in users if user.username == username), None)
