from rest_framework import generics, status
from rest_framework.response import Response

from apps.carshops.models import CarShopModel
from apps.carshops.serializers import CarShopSerializer, StaffSerializer


# Carshop list
class CarShopListView(generics.ListAPIView):
    """
    GET:
        Get all carshops
    """

    queryset = CarShopModel.objects.all()
    serializer_class = CarShopSerializer


class CarShopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Get carshop by ID
    put:
        Update carshop by ID
    patch:
        Partial update carshop by ID
    delete:
        Delete carshop by ID
    """

    queryset = CarShopModel.objects.all()
    serializer_class = CarShopSerializer


# Add staff to carshop
class CarShopAddStaffView(generics.GenericAPIView):
    """
    POST:
        Add staff to carshop
    """

    serializer_class = CarShopSerializer

    def get_queryset(self):
        return CarShopModel.objects.filter(pk=self.kwargs.get("pk"))

    def post(self, *args, **kwargs):
        data = self.request.data
        carshop = self.get_object()
        serializer = StaffSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(carshop=carshop)

        return Response(self.serializer_class(carshop).data, status.HTTP_201_CREATED)
