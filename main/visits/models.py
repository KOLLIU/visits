from django.db import models


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=255, verbose_name="Номер", )

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.name


class SalePoint(models.Model):
    title = models.CharField(max_length=65535, verbose_name="Название")
    workers = models.ManyToManyField(Worker, null=False, blank=False, verbose_name="Работник",
                                     related_name="sale_points")

    class Meta:
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговые точки"

    def __str__(self):
        return self.title


class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время")
    sale_point = models.ForeignKey(SalePoint, on_delete=models.PROTECT, verbose_name="Торговая точка")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self):
        return f"{self.sale_point} {self.datetime.day}.{self.datetime.month}"

