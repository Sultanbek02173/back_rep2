from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255, verbose_name="Марка")
    model = models.CharField(max_length=255, verbose_name="Модель")
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")
    color = models.CharField(max_length=100, verbose_name="Цвет")
    rudely_location = models.CharField(max_length=100, verbose_name="Расположения руля")
    engine_volume = models.PositiveSmallIntegerField(verbose_name="Объем двигателя")

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
