from django.db import models


class Pictures(models.Model):
    picture = models.ImageField(blank=True, verbose_name='Изображение')


    def __str__(self):
        return f'{self.picture}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название места', null=True)
    description_short = models.CharField(max_length=400, verbose_name='Описание места - кратко')
    description_long = models.TextField(verbose_name='Подробное описание места')
    lon = models.FloatField(blank=False, verbose_name='долгота')
    lat = models.FloatField(blank=False, verbose_name='широта')
    # imgs = models.ManyToManyField(Pictures, verbose_name="картинки", on_delete=models.CASCADE, null=True, symmetrical=False)
    imgs = models.ManyToManyField(Pictures, verbose_name="картинки", null=True, blank=True, symmetrical=False)
    # imgs = models.ForeignKey(Pictures, verbose_name="картинки", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

