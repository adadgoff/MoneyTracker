from uuid import uuid4, UUID

from app.database.config import DELIMITER


class User:
    __slots__ = ("uuid", "username", "password")

    def __init__(self, username: str, password: str, uuid: UUID = uuid4()):
        self.uuid: UUID = uuid
        self.username: str = username
        self.password: str = password

    def __repr__(self):
        return DELIMITER.join([str(self.uuid),
                               self.username,
                               self.password])
