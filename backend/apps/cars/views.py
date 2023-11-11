import math
from datetime import datetime

from django.db.models import Avg, Q
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from core.permissions import IsAdmin, IsPremium


class CarListView(generics.ListAPIView):
    """
    GET:
        Get all cars
    """

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by ID
    put:
        Update Car by ID
    patch:
        Partial update Car by ID
    delete:
        Delete Car by ID
    """

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class AvgPriceByRequestedCarView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    """
    GET:
        Get avg_price of requested car
    """

    def get(self, *args, **kwargs):
        data = self.request.data

        if not data:
            return Response(
                "{brand: search_brand, model:search_model} must be provided"
            )

        queryset = CarModel.objects.filter(brand=data["brand"], model=data["model"])

        average_price = math.ceil(
            queryset.aggregate(avg_value=Avg("price"))["avg_value"]
        )

        # print(datetime.date())
        # print(datetime.date())
        # print(datetime.date())
        # print(datetime.date())

        return Response(
            f"average price for this car is  {average_price}", status.HTTP_200_OK
        )
