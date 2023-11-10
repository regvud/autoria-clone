from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "price",
            "currency",
            "body",
            "created_at",
        )
