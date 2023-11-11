from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from apps.users.managers import UserManager
from core.enums.model_enums.user_enum import UserEnum
from core.models import BaseModel

# Create your models here.


class ProfileModel(BaseModel):
    class Meta:
        db_table = "profile"

    name = models.CharField(
        max_length=30, validators=[V.RegexValidator(*UserEnum.NAME.value)]
    )
    surname = models.CharField(
        max_length=30, validators=[V.RegexValidator(*UserEnum.NAME.value)]
    )
    age = models.IntegerField(
        validators=[
            V.MinValueValidator(16),
            V.MaxValueValidator(100),
        ]
    )


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = "auth_user"

    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=128, validators=[V.RegexValidator(*UserEnum.PASSWORD.value)]
    )
    is_seller = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_carshop = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile = models.OneToOneField(
        ProfileModel, on_delete=models.CASCADE, related_name="user", null=True
    )

    USERNAME_FIELD = "email"

    objects = UserManager()
