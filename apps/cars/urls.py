from django.urls import path

from apps.cars.views import CarAPIView

urlpatterns = [
    path("cars/", CarAPIView.as_view(), name="api_cars")
]
