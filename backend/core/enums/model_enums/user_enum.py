from ast import pattern
from enum import Enum


class UserEnum(Enum):
    PASSWORD = (
        r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$",
        [
            "Has minimum 8 characters in length.",
            "At least one uppercase English letter.",
            "At least one lowercase English letter.",
            "At least one digit.",
            "At least one special character",
        ],
    )

    NAME = (
        r"^[A-Z][a-z]{1,30}$",
        "First letter uppercase",
    )

    def __init__(self, pattern: str, msg: str | list[str]) -> None:
        self.pattern = pattern
        self.msg = msg
