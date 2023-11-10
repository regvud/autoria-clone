from django.urls import path

from .views import CarByAvgPriceView, CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path("", CarListView.as_view(), name="cars_list"),
    path("/avg_price", CarByAvgPriceView.as_view(), name="car_by_avg_price"),
    path(
        "/<int:pk>",
        CarRetrieveUpdateDestroyView.as_view(),
        name="car_retrive_update_destroy",
    ),
]
