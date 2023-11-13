from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import (
    BrandSerializer,
    CarBrandModelSerializer,
    CarSerializer,
)
from core.permissions import IsAdmin, IsManager, IsPremium
from core.services.avg_price_service import AveragePriceService
from core.services.email_service import EmailService
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

    serializer_class = CarBrandModelSerializer
    permission_classes = (IsPremium | IsManager | IsAdmin,)

    def get(self, *args, **kwargs):
        data = self.request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            queryset = CarModel.objects.filter(
                brand=serializer.data["brand"], model=serializer.data["model"]
            )
            avg_price = AveragePriceService.avg_price(queryset)

        except Exception:
            return Response({"detail": "Car table is empty, add cars for users"})

        return Response(
            f"Average price for this car is {avg_price} UAH", status.HTTP_200_OK
        )


class AddBrandToListRequestView(generics.GenericAPIView):
    """
    POST:
        send email to admin adout adding new brand
    """

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = BrandSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        brand = serializer.data["brand"]
        EmailService.send_brand_request(brand)

        return Response(
            "Your request has been sended to administation.", status.HTTP_200_OK
        )
