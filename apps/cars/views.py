# from django.shortcuts import render

from rest_framework.generics import ListAPIView
from apps.cars.models import Car

from apps.cars.serializers import CarSerializer


class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
