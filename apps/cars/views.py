from rest_framework import generics, status
from rest_framework.response import Response

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarByAvgPriceView(generics.GenericAPIView):
    serializer_class = CarSerializer

    def get(self, *args, **kwargs):
        data = self.request.data
        queryset = CarModel.filter_objects.avg_price(data["price"])

        return Response(self.serializer_class(queryset).data, status.HTTP_200_OK)
