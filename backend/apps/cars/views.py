import math

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import (
    BrandSerializer,
    CarBrandModelCurrencyFieldsSerializer,
    CarSerializer,
)
from core.permissions import IsAdmin, IsManager, IsPremium
from core.services.email_service import EmailService
from django.db.models import Avg
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CarListView(generics.ListAPIView):
    """
    GET:
        Get all cars
    """

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


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
    permission_classes = (IsManager | IsAdmin,)


class AvgPriceByRequestedCarView(generics.GenericAPIView):
    """
    GET:
        Get avg_price of requested car
    """

    serializer_class = CarBrandModelCurrencyFieldsSerializer
    permission_classes = (IsPremium | IsManager | IsAdmin,)

    """
    not converted into currency
    """

    def get(self, *args, **kwargs):
        data = self.request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            queryset = CarModel.objects.filter(
                brand=serializer.data["brand"], model=serializer.data["model"]
            )

            average_price = math.ceil(
                queryset.aggregate(avg_value=Avg("price"))["avg_value"]
            )
        except Exception:
            return Response({f"Car table is empty"})

        return Response(
            f"average price for this car is  {average_price}", status.HTTP_200_OK
        )

    # def get(self, *args, **kwargs):
    #     data = self.request.data

    #     serializer = self.serializer_class(data=data)
    #     serializer.is_valid(raise_exception=True)

    #     try:
    #         queryset = CarModel.objects.filter(
    #             brand=serializer.data["brand"], model=serializer.data["model"]
    #         )

    #         # currency = get_object_or_404(CurrencyModel, currency=queryset[0].currency)
    #         # saleRate = currency.saleRate

    #         print(queryset)

    #         average_price = math.ceil(
    #             queryset.aggregate(avg_value=Avg("price"))["avg_value"]
    #         )
    #     except Exception:
    #         return Response({f"Car table is empty"})

    #     return Response(f"average price for this car is  ", status.HTTP_200_OK)


class AddBrandToListRequestView(generics.GenericAPIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = BrandSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        brand = serializer.data["brand"]
        EmailService.send_brand_request(brand)

        return Response("ok", status.HTTP_200_OK)
