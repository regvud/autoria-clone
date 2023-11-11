from django.db import models

from core.models import BaseModel


# Create your models here.
class CurrencyModel(BaseModel):
    class Meta:
        db_table = "currencies"

    baseCurrency = models.CharField(max_length=3)
    currency = models.CharField(max_length=3)
    saleRateNB = models.DecimalField(
        max_digits=20,
        decimal_places=7,
    )
    purchaseRateNB = models.DecimalField(
        max_digits=20,
        decimal_places=7,
    )
    saleRate = models.DecimalField(max_digits=20, decimal_places=7, null=True)
    purchaseRate = models.DecimalField(max_digits=20, decimal_places=7, null=True)
