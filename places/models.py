from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название места', null=True)
    description_short = models.CharField(max_length=400, verbose_name='Описание места - кратко')
    description_long = HTMLField(verbose_name='Подробное описание места')
    lon = models.FloatField(blank=False, verbose_name='долгота')
    lat = models.FloatField(blank=False, verbose_name='широта')
    placeID = models.SlugField(max_length=150, default='', verbose_name='ID места', blank=True)
    place_order = models.SmallIntegerField(default=0, verbose_name='Порядок сортировки')

    def _create_slug(self):
        slug = slugify(self.title, allow_unicode=True)

        translate_string = slug.translate(str.maketrans(
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_I_EUY"))
        slug = f'{translate_string.capitalize()}-{uuid4().hex[:8]}'
        self.placeID = slug

    def save(self, *args, **kwargs):
        if not self.pk:
            self._create_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['place_order']


class Picture(models.Model):
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name='images', verbose_name='Место')
    picture = models.ImageField(upload_to='place_pic', verbose_name='Картинки')
    pic_order = models.SmallIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['pic_order']

    def __str__(self):
        return f'{self.picture}'
