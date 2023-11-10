
from rest_framework import generics

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
