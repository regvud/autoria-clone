from rest_framework import generics
from rest_framework.authentication import get_user_model

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


# Create your views here.
class UserListCreateView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
