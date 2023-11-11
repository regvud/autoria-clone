from django.urls import path

from .views import AvgPriceByRequestedCarView, CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path("", CarListView.as_view(), name="cars_list"),
    path(
        "/avg_price",
        AvgPriceByRequestedCarView.as_view(),
        name="avg_price_by_requested_car",
    ),
    path(
        "/<int:pk>",
        CarRetrieveUpdateDestroyView.as_view(),
        name="car_retrive_update_destroy",
    ),
]
