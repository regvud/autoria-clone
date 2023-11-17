import datetime
import logging

import requests
from apps.currencies.models import CurrencyModel
from apps.currencies.serializers import CurrencySerializer
from configs.celery import app

# class CurrencyService:
#     @staticmethod
#     @app.task
#     def fetch_data():
#         date = datetime.date.today() - datetime.timedelta(days=1)
#         date = date.strftime("%d.%m.%Y")
#         api_url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
#         try:
#             response = requests.get(api_url)
#             response.raise_for_status()


#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching data from API: {e}")
#             return None
class CurrencyService:
    @staticmethod
    def __fetch_data():
        date = datetime.date.today() - datetime.timedelta(days=1)
        date = date.strftime("%d.%m.%Y")
        api_url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()

            response = response.json()
            currencies = response["exchangeRate"]

            serializer = CurrencySerializer(data=currencies, many=True)
            serializer.is_valid(raise_exception=True)

            CurrencyModel.objects.all().delete()

            serializer.save()
            return {"currencies": serializer.data}
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None

    @staticmethod
    @app.task
    def execute_currencies():
        try:
            res = CurrencyService.__fetch_data()
            return res
        except Exception as e:
            logging.error(f"Error executing currencies task: {e}")
