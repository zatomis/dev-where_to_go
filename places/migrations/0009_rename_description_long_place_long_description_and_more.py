# Generated by Django 4.2.7 on 2024-02-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_picture_place_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
