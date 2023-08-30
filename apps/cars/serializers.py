from rest_framework import serializers

from apps.cars.models import Car, SpecialMark, PeriodOwnership


class SpecialMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialMark
        fields = "__all__"


class PeriodOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodOwnership
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    cars_special_marks = SpecialMarkSerializer(read_only=True, many=True)
    cars_periods_ownership = PeriodOwnershipSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = ("id", "license_plate", "brand", "model", "year", "color", "rudely_location", "engine_volume",
                  "cars_special_marks", "cars_periods_ownership")
