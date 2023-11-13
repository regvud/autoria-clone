from apps.cars.models import CarModel
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "city",
            "price",
            "currency",
            "body",
            "created_at",
            "updated_at",
        )


class CarBrandModelCurrencyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            "brand",
            "model",
        )
