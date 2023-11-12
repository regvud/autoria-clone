from apps.currencies.views import CurrencyFetchApiView, CurrencyListView
from django.urls import path

urlpatterns = [
    path("", CurrencyListView.as_view(), name="currency_list"),
    path("/fetch", CurrencyFetchApiView.as_view(), name="currency_fetch"),
]
