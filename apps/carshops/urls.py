from django.urls import path

from .views import CarShopListView

urlpatterns = [
    path("", CarShopListView.as_view(), name="carshop_list"),
]
