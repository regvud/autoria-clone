from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MeView, RecoverPasswordRequestView, RecoverPasswordView

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("/me", MeView.as_view(), name="show_me"),
    path("/recover/request", RecoverPasswordRequestView.as_view()),
    path("/recover/<str:token>", RecoverPasswordView.as_view()),
]
