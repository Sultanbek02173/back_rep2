from django.db import models


class Car(models.Model):
    license_plate = models.CharField(verbose_name="Гос номер", max_length=10, unique=True, null=True)
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


class SpecialMark(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cars_special_marks")
    title = models.CharField(max_length=255, verbose_name="Отметка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Особая отметка"
        verbose_name_plural = "Особые отметки"


class PeriodOwnership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cars_periods_ownership")
    from_date = models.DateField(verbose_name="От", auto_now=True)
    before_date = models.DateField(verbose_name="До")
    actual = models.BooleanField(verbose_name="Актуальность", default=False)

    def __str__(self):
        return f"{self.from_date} - {self.before_date}"

    class Meta:
        verbose_name = "Период владения"
        verbose_name_plural = "Периоды владения"
