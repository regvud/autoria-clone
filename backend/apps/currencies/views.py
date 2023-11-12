import datetime

import requests
from apps.currencies.serializers import CurrencySerializer
from configs.celery import app
from core.services.currency_service import CurrencyService
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from rest_framework.response import Response

from .models import CurrencyModel


class CurrencyFetchApiView(View):
    def get(self, request):
        date = datetime.date.today().strftime("%d.%m.%Y")
        api_url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                currency_list = response.json()

                CurrencyModel.objects.all().delete()

                for currency in currency_list["exchangeRate"]:
                    CurrencyModel.objects.create(**currency)

                return JsonResponse({"currencies_update": currency_list})
            else:
                return JsonResponse(
                    {"error": f"Error: {response.status_code}"},
                    status=response.status_code,
                )
        except Exception as e:
            return JsonResponse({"error": f"Error: {e}"}, status=500)


class CurrencyUpdate(generics.GenericAPIView):
    serializer_class = CurrencySerializer

    def get(self, *args, **kwargs):
        pass

class CurrencyListView(generics.ListAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
