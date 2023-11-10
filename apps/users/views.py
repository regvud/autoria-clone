from operator import ge

from rest_framework import generics, status
from rest_framework.authentication import get_user_model
from rest_framework.response import Response

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel
    serializer_class = UserSerializer


class UserToAdminView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return UserModel.objects.filter(pk=self.kwargs.get("pk"))

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff:
            return Response("User is admin")

        user.is_staff = True
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return UserModel.objects.filter(pk=self.kwargs.get("pk"))

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            return Response("User is not admin")

        user.is_staff = False
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserBlockView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return UserModel.objects.filter(pk=self.kwargs.get("pk"))

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            return Response("User is blocked")

        user.is_active = False
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnblockView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return UserModel.objects.filter(pk=self.kwargs.get("pk"))

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            return Response("User is unblocked")

        user.is_active = True
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToPremiumView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return UserModel.objects.filter(pk=self.kwargs.get("pk"))

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_premium:
            return Response("User is premium")

        user.is_premium = True
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToNonPremiumView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return UserModel.objects.filter(pk=self.kwargs.get("pk"))

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_premium:
            return Response("User is not premium")

        user.is_premium = False
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
