import datetime

import requests
from configs.celery import app
    



class CurrencyService:
    @staticmethod
    @app.task
    def fetch_data():
        date = datetime.date.today().strftime("%d.%m.%Y")
        api_url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None


# not working
