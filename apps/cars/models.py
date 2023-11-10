import datetime
from datetime import datetime

from django.core import validators as v
from django.db import models

from apps.cars.managers import CarManager
from apps.users.models import UserModel
from core.enums.model_enums.car_enum import CarEnum
from core.models import BaseModel

from .choices import BodyChoices, CurrencyChoices


# Create your models here.
class CarModel(BaseModel):
    class Meta:
        db_table = "cars"

    brand = models.CharField(
        max_length=30, validators=[v.RegexValidator(*CarEnum.BRAND.value)]
    )
    model = models.CharField(
        max_length=30, validators=[v.RegexValidator(*CarEnum.MODEL.value)]
    )
    year = models.IntegerField(
        validators=[v.MinValueValidator(1970), v.MaxValueValidator(datetime.now().year)]
    )
    city = models.CharField(max_length=30)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[v.MinValueValidator(100), v.MaxValueValidator(999999999)],
    )
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices)
    body = models.CharField(max_length=11, choices=BodyChoices.choices)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="cars")

    objects = models.Manager()
    filter_objects = CarManager()
