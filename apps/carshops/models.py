from django.core import validators as V
from django.db import models
from rest_framework.authentication import get_user_model

from core.enums.model_enums.carshop_enum import CarShopEnum
from core.enums.model_enums.user_enum import UserEnum
from core.models import BaseModel

from .choices import RoleChoices

UserModel = get_user_model()


class CarShopModel(BaseModel):
    class Meta:
        db_table = "carshops"

    name = models.CharField(
        max_length=30, validators=[V.RegexValidator(*CarShopEnum.NAME.value)]
    )
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="carshop"
    )


class StaffModel(BaseModel):
    class Meta:
        db_table = "staff"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=8, choices=RoleChoices.choices)
    name = models.CharField(max_length=30, validators=[V.RegexValidator(*UserEnum.NAME.value)])
    surname = models.CharField(max_length=30, validators=[V.RegexValidator(*UserEnum.NAME.value)])
    age = models.IntegerField(
        validators=[V.MinValueValidator(18), V.MaxValueValidator(65)]
    )
    phone = models.CharField(max_length=13)
    carshop = models.ForeignKey(
        CarShopModel, on_delete=models.CASCADE, related_name="staff"
    )
