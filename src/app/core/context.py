from app.user.user import User


class Context:
    CURRENT_USER: User | None = None
    ERROR_CONTEXT: str | None = None
    LANGUAGE_CONTEXT: dict | None = None
    NOTIFICATION_CONTEXT: str | None = None
    START: bool = True
