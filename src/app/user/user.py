from uuid import uuid4, UUID



class User:
    __slots__ = ("uuid", "username", "password")

    def __init__(self, username: str, password: str, uuid=uuid4()):
        self.uuid: UUID = uuid
        self.username: str = username
        self.password: str = password

    def __repr__(self):
        return DELIMITER.join([str(self.uuid),
                               self.username,
                               self.password])
