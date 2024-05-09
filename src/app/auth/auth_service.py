from app.auth.hasher import verify_password
from app.core.context import Context
from app.user.user import User
from app.user.user_exceptions import UserNotFoundException, UserIncorrectDataException
from app.user.user_service import UserService


class AuthService:
    @classmethod
    def register(cls, username, password) -> User:
        user = UserService.create_user(username, password)
        return user

    @classmethod
    def login(cls, username, password) -> User:
        user = UserService.read_user(username)
        if not user:
            raise UserNotFoundException
        if not verify_password(password, user.password):
            raise UserIncorrectDataException
        Context.CURRENT_USER = user
        return user

    @classmethod
    def logout(cls) -> None:
        Context.CURRENT_USER = None
