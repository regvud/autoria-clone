from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.authentication import get_user_model

from apps.cars.serializers import CarSerializer
from apps.carshops.serializers import CarShopSerializer
from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            "id",
            "name",
            "surname",
            "age",
            "created_at",
            "updated_at",
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    carshop = CarShopSerializer(many=True, read_only=True)
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            "id",
            "email",
            "password",
            "is_seller",
            "is_premium",
            "is_carshop",
            "is_active",
            "is_staff",
            "is_superuser",
            "profile",
            "cars",
            "carshop",
            "last_login",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "is_seller",
            "is_premium",
            "is_carshop",
            "is_active",
            "is_staff",
            "is_superuser",
            "carshop",
            "cars",
            "profile",
            "last_login",
            "created_at",
            "updated_at",
        )

        extra_kwargs = {
            "password": {"write_only": True},
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop("profile")
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        return user
