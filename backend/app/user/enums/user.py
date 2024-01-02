from enum import Enum

class UserStatus(str, Enum):
    blocked: str = "blocked"
    deleted: str = "deleted"
    inactive: str = "inactive"
    active: str = "active"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))