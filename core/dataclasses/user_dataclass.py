from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataclass:
    name: str
    surname: str
    age: int


@dataclass
class UserDataclass:
    id: int
    emai: str
    password: str
    is_seller: bool
    is_premium: bool
    is_carshop: bool
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: str
    created_at: datetime
    updated_at: datetime
    profile: ProfileDataclass
