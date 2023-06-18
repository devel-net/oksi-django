from django_filters import rest_framework as filters
from .models import Car


class CarFilter(filters.FilterSet):
    car_brand = filters.CharFilter(lookup_expr='contains')
    release_year = filters.NumberFilter(field_name="release_year", lookup_expr='gte')
    seats = filters.NumberFilter(field_name="seats", lookup_expr='lte')
    body_type = filters.CharFilter(lookup_expr='contains')
    engine_volume = filters.NumberFilter(field_name="engine_volume", lookup_expr='exact')

    class Meta:
        model = Car
        fields = ['car_brand', 'release_year', 'seats', 'body_type', 'engine_volume']