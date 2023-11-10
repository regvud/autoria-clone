from django.core import validators as v
from django.db import models
from rest_framework.authentication import get_user_model
from rest_framework.fields import RegexValidator

from core.enums.carshop_enum import CarShopEnum
from core.models import BaseModel

from .choices import RoleChoices


class CarShopModel(BaseModel):
    class Meta:
        db_table = "carshops"

    name = models.CharField(
        max_length=30, validators=[RegexValidator(*CarShopEnum.NAME.value)]
    )


class StaffModel(BaseModel):
    class Meta:
        db_table = "staff"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=8, choices=RoleChoices.choices)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    carshop = models.ForeignKey(
        CarShopModel, on_delete=models.CASCADE, related_name="staff"
    )
