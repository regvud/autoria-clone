from enum import Enum


class CarShopEnum(Enum):
    NAME = (
        r"[A-ZА-ЯЇІЄҐ][ А-Яа-яa-zA-ZЇїІіЄєҐґ\d]{2,20}$"
        "Name first letter must be uppercase,  min 2 max 30 characters",
    )
