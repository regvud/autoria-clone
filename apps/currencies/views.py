import datetime

import requests
from django.http import JsonResponse
from django.views import View
from rest_framework import generics

from apps.currencies.serializers import CurrencySerializer

from .models import CurrencyModel


class CurrencyFetchApiView(View):
    def get(self, request):
        date = datetime.date.today().strftime("%d.%m.%Y")
        api_url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                data_list = response.json()

                CurrencyModel.objects.all().delete()

                for data in data_list["exchangeRate"]:
                    CurrencyModel.objects.create(**data)

                return JsonResponse({"data": data_list["exchangeRate"]})
            else:
                return JsonResponse(
                    {"error": f"Error: {response.status_code}"},
                    status=response.status_code,
                )
        except Exception as e:
            return JsonResponse({"error": f"Error: {e}"}, status=500)


class CurrencyListView(generics.ListAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
