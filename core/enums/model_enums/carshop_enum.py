from enum import Enum


class CarShopEnum(Enum):
    NAME = (
        r"^[A-ZА-ЯЇІЄҐ][ А-Яа-яa-zA-ZЇїІіЄєҐґ\d]{2,20}$",
        "Name first letter must be uppercase,  min 2 max 30 characters",
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
