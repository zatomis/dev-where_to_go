from uuid import uuid4

from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(blank=False, max_length=100, verbose_name='Название места', null=False, default='Локация', unique=True)
    short_description = models.TextField(verbose_name='Описание места - кратко', blank=True, null=False)
    long_description = HTMLField(verbose_name='Подробное описание места', blank=True, null=False)
    lon = models.FloatField(blank=False, verbose_name='долгота')
    lat = models.FloatField(blank=False, verbose_name='широта')
    slug = models.SlugField(max_length=150, verbose_name='Уникальный идентификатор локации', blank=True)
    place_order = models.SmallIntegerField(default=0, verbose_name='Порядок сортировки', db_index=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['place_order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self._create_slug()
        super().save(*args, **kwargs)
 
    def _create_slug(self):
        slug = slugify(self.title, allow_unicode=True)
        translate_string = slug.translate(str.maketrans(
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_I_EUY"))
        self.slug = f'{translate_string.capitalize()}-{uuid4().hex[:8]}'




class Picture(models.Model):
    place_pic = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(upload_to='place_pic', verbose_name='Картинки')
    pic_order = models.SmallIntegerField(default=0, verbose_name='Порядок сортировки', db_index=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['pic_order']

    def __str__(self):
        return f'{self.image}'
