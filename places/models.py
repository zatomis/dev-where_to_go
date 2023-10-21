from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название места', null=True)
    description_short = models.CharField(max_length=400, verbose_name='Описание места - кратко')
    description_long = models.TextField(verbose_name='Подробное описание места')
    lon = models.FloatField(blank=False, verbose_name='долгота')
    lat = models.FloatField(blank=False, verbose_name='широта')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
