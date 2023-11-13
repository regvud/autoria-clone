import math

from apps.currencies.models import CurrencyModel
from django.shortcuts import get_object_or_404


class AveragePriceService:
    def avg_price(queryset):
        usd = get_object_or_404(CurrencyModel, currency="USD")
        usd = usd.saleRate

        eur = get_object_or_404(CurrencyModel, currency="EUR")
        eur = eur.saleRate

        result = 0

        for car in queryset:
            match car.currency:
                case "USD":
                    result += car.price * usd
                case "EUR":
                    result += car.price * eur
                case "UAH":
                    result += car.price

        result = math.ceil(result / len(queryset))
        return result
