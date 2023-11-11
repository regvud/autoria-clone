from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.authentication import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.serializers import UserSerializer
from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JwtService, RecoveryToken

UserModel = get_user_model()


class MeView(generics.GenericAPIView):
    """
    GET:
        Get authorized user
    """

    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data, status.HTTP_200_OK)


class ActivateUserView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs["token"]
        user = JwtService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class RecoverPasswordRequestView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    # provide email method
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)

        EmailService.recover_password(user)
        return Response("check email", status.HTTP_202_ACCEPTED)

    # id method
    # def get_object(self, *args, **kwargs):
    #     return UserModel.objects.get(pk=self.kwargs["pk"])
    # def post(self, *args, **kwargs):
    #     EmailService.recover_password(self.get_object())
    #     return Response("check email")


class RecoverPasswordView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data

        if not data:
            raise ValueError("Provide {'password' : '...your_password'} ")

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        user = JwtService.validate_token(self.kwargs["token"], RecoveryToken)

        user.set_password(data["password"])
        user.save()

        return Response("password has been changed", status.HTTP_202_ACCEPTED)
