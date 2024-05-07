from csv import DictReader



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
            users = (User(**d) for d in DictReader(f_user, delimiter=DELIMITER))
            return next((user for user in users if user.username == username), None)
