from rest_framework import generics, status
from rest_framework.authentication import get_user_model
from rest_framework.response import Response

from apps.users.serializers import UserSerializer


class MeView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data, status.HTTP_200_OK)
