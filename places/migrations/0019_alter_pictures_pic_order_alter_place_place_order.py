# Generated by Django 4.2.7 on 2023-11-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0018_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='pic_order',
            field=models.SmallIntegerField(default=0, verbose_name='Порядок сортировки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_order',
            field=models.SmallIntegerField(default=0, verbose_name='Порядок сортировки'),
        ),
    ]
