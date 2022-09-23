from django.db import models
from city.models import City
from street.models import Street


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название магазина')
    city_id = models.ForeignKey(City, verbose_name='id города', on_delete=models.CASCADE)
    street_id = models.ForeignKey(Street, verbose_name='id улицы', on_delete=models.CASCADE)
    start_time = models.CharField(verbose_name='Время открытия', max_length=5)
    end_time = models.CharField(verbose_name='Время закрытия', max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
