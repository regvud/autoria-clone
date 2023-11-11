from enum import Enum


class CarEnum(Enum):
    BRAND = (
        r"^[A-Z][a-zA-Z\D]{1,20}$",
        "Brand first letter must be uppercase,  min 2 max 30 characters, no digits",
    )

    MODEL = (
        r"^[A-Z][a-zA-Z\d]{1,20}$",
        "Model first letter must be uppercase,  min 1 max 30 characters, digits allowed",
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
