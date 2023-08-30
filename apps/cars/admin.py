from django.contrib import admin

from apps.cars.models import Car, SpecialMark, PeriodOwnership

admin.site.register(Car)

admin.site.register(SpecialMark)

admin.site.register(PeriodOwnership)
