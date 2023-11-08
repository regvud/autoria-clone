from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models
from django.db.models.fields import related

from apps.users.managers import UserManager
from core.models import BaseModel

# Create your models here.


class ProfileModel(BaseModel):
    class Meta:
        db_table = "profile"
        ordering = ("id",)

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[
            V.MinValueValidator(16),
            V.MaxValueValidator(100),
        ]
    )


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = "auth_user"
        ordering = ("id",)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_seller = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)
    profile = models.OneToOneField(
        ProfileModel, on_delete=models.CASCADE, related_name="user", null=True
    )

    USERNAME_FIELD = "email"

    objects = UserManager()
