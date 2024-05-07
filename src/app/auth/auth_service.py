class AuthService:
    @classmethod
    def register(cls, username, password) -> User:
        user = UserService.create_user(username, password)
        return User

    @classmethod
    def login(cls, username, password) -> User:
        user = UserService.read_user(username, password)
        if not user:
            raise UserNotFoundException
        CURRENT_USER = user
        return user

    @classmethod
    def logout(cls) -> None:
        CURRENT_USER = None
