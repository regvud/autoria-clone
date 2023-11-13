from django.urls import path

from .views import (
    AddBrandToListRequestView,
    AvgPriceByRequestedCarView,
    CarListView,
    CarRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("", CarListView.as_view(), name="cars_list"),
    path(
        "/<int:pk>",
        CarRetrieveUpdateDestroyView.as_view(),
        name="car_retrive_update_destroy",
    ),
    path(
        "/avg_price",
        AvgPriceByRequestedCarView.as_view(),
        name="avg_price_by_requested_car",
    ),
    path(
        "/add_brand",
        AddBrandToListRequestView.as_view(),
        name="add_brand_to_list",
    ),
]
