from django.urls import path

from apps.cars.views import CarAPIView, CarCreatAPIView, CarUpdateAPIView, CarDeleteAPIView

urlpatterns = [
    path("cars/", CarAPIView.as_view(), name="api_cars"),
    path("cars/creat/", CarCreatAPIView.as_view(), name="api_cars_create"),
    path("cars/update/<int:pk>/", CarUpdateAPIView.as_view(), name="api_upgate_create"),
    path("cars/delete/<int:pk>/", CarDeleteAPIView.as_view(), name="api_delete_create"),
]
