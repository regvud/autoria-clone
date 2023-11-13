from apps.currencies.serializers import CurrencySerializer
from configs.celery import app
from core.permissions import IsAdmin, IsManager
from core.services.currency_service import CurrencyService
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CurrencyModel


class CurrencyFetchApiView(generics.GenericAPIView):
    """
    GET:
      manually fetch currencies from privat-bank api and save them to db
    """

    permission_classes = (IsAdmin | IsManager,)

    def get(self, request):
        try:
            response = CurrencyService.__fetch_data()
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e})


class CurrencyListView(generics.ListAPIView):
    """
    GET:
        get currency list
    """

    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
