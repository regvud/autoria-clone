from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.authentication import get_user_model

from apps.carshops.models import CarShopModel, StaffModel

UserModel = get_user_model()


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = ("id", "email", "role", "name", "surname", "age", "phone")


class CarShopSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = CarShopModel
        fields = ("id", "name", "staff")
