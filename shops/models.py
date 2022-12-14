from django.db import models
from city.models import City
from street.models import Street


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название магазина')
    city = models.ForeignKey(City, verbose_name='id города', on_delete=models.CASCADE)
    street = models.ForeignKey(Street, verbose_name='id улицы', on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name='Время открытия', auto_now=False, auto_now_add=False)
    end_time = models.TimeField(verbose_name='Время закрытия', auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
