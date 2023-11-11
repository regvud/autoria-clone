from datetime import datetime

from django.urls import path

from apps.currencies.views import CurrencyFetchApiView, CurrencyListView

urlpatterns = [
    path("", CurrencyListView.as_view(), name="currency_list"),
    path("/fetch", CurrencyFetchApiView.as_view(), name="currency_fetch"),
]
