import datetime

import requests
from configs.celery import app
from rest_framework.authentication import get_user_model

from .email_service import EmailService

UserModel = get_user_model()


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

    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, "spam.html", {}, "SPAM")


# not working
