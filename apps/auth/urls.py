from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ActivateUserView,
    MeView,
    RecoverPasswordRequestView,
    RecoverPasswordView,
)

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("/me", MeView.as_view(), name="show_me"),
    path(
        "/recover/request",
        RecoverPasswordRequestView.as_view(),
        name="password_recover_request",
    ),
    path(
        "/recover/<str:token>", RecoverPasswordView.as_view(), name="password_recover"
    ),
    path("/activate/<str:token>", ActivateUserView.as_view(), name="user_activate"),
]
