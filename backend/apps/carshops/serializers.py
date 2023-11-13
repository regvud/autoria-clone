from apps.carshops.models import CarShopModel, StaffModel
from rest_framework import serializers
from rest_framework.authentication import get_user_model

UserModel = get_user_model()


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = (
            "id",
            "email",
            "role",
            "name",
            "surname",
            "age",
            "phone",
            "created_at",
            "updated_at",
        )


class CarShopSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = CarShopModel
        fields = ("id", "name", "staff", "created_at", "updated_at")
