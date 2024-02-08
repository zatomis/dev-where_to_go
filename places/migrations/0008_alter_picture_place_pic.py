# Generated by Django 4.2.7 on 2024-02-07 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_picture_pic_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='place_pic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место'),
        ),
    ]
