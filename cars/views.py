from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car
from .filters import CarFilter
from .serializer import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CarFilter
    ordering_fields = ['car_brand', 'release_year', 'seats', 'body_type', 'engine_volume']
