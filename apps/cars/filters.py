from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    order = filters.OrderingFilter(
        fields=(
            "id",
            "brand",
            "model",
            "year",
            "price",
            "currency",
            "body",
            "created_at",
            "updated_at",
        )
    )

    class Meta:
        model = CarModel
        fields = {
            "year": ("lt", "lte", "gt", "gte"),
            "price": ("lt", "lte", "gt", "gte"),
            "currency": ("istartswith", "iendswith", "icontains"),
            "body": ("istartswith", "iendswith", "icontains"),
            "model": ("istartswith", "iendswith", "icontains"),
            "brand": ("istartswith", "iendswith", "icontains"),
        }
