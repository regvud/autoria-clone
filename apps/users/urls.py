from django.urls import path

from .views import (
    AdminToUserView,
    UserBlockView,
    UserCarCreateView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserToAdminView,
    UserToCarshop,
    UserToNonCarshop,
    UserToNonPremiumView,
    UserToPremiumView,
    UserUnblockView,
)

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user_list"),
    path("/<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="user_retrieve"),
    path("/<int:pk>/create_car", UserCarCreateView.as_view(), name="user_create_car"),
    path(
        "/<int:pk>/user_to_admin",
        UserToAdminView.as_view(),
        name="user_to_admin",
    ),
    path(
        "/<int:pk>/admin_to_user",
        AdminToUserView.as_view(),
        name="admin_to_user",
    ),
    path(
        "/<int:pk>/block",
        UserBlockView.as_view(),
        name="user_block",
    ),
    path(
        "/<int:pk>/unblock",
        UserUnblockView.as_view(),
        name="user_unblock",
    ),
    path(
        "/<int:pk>/user_to_premium",
        UserToPremiumView.as_view(),
        name="user_to_premium",
    ),
    path(
        "/<int:pk>/user_to_nonpremium",
        UserToNonPremiumView.as_view(),
        name="user_to_nonpremium",
    ),
    path(
        "/<int:pk>/user_to_carshop",
        UserToCarshop.as_view(),
        name="user_to_carshop",
    ),
    path(
        "/<int:pk>/user_to_noncarshop",
        UserToNonCarshop.as_view(),
        name="user_to_noncarshop",
    ),
]
