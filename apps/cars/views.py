from rest_framework import generics

from apps.cars.models import CarModel


class CarListView(generics.ListAPIView):
    queryset = CarModel.objects.all()
