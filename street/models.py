from django.db import models
from city.models import City
# Create your models here.

class Street(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название улицы')
    city_id = models.ForeignKey(City, verbose_name='id города', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
