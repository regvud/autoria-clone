from rest_framework import generics

from apps.carshops.models import CarShopModel
from apps.carshops.serializers import CarShopSerializer


class CarShopListView(generics.ListAPIView):
    queryset = CarShopModel.objects.all()
    serializer_class = CarShopSerializer


class CarShopAddStaffView(generics.GenericAPIView):
    queryset = CarShopModel.objects.all()
    serializer_class = CarShopSerializer

    def post(self, *args, **kwargs):
        pass
