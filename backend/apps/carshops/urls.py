from django.urls import path

from .views import (
    CarShopAddStaffView,
    CarShopListView,
    CarShopRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("", CarShopListView.as_view(), name="carshop_list"),
    path(
        "/<int:pk>",
        CarShopRetrieveUpdateDestroyView.as_view(),
        name="carshop_retrieve_update_destroy",
    ),
    path(
        "/<int:pk>/add_staff", CarShopAddStaffView.as_view(), name="carshop_add_staff"
    ),
]
