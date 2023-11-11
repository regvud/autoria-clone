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
            "city",
            "price",
            "currency",
            "body",
            "created_at",
            "updated_at",
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("brand",)
