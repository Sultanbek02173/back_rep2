# from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.cars.models import Car

from apps.cars.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['license_plate', ]


class CarCreatAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
