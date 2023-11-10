from enum import Enum


class CarEnum(Enum):
    BRAND = (
        r"^[A-Z][a-zA-Z\d]{1,20}$",
        "First letter must be uppercase,  min 2 max 30 characters",
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
