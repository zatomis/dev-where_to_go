import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Pictures


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'place_url',
            type=str,
            help='Ссылка на локации',
        )

    def handle(self, *args, **options):
        url = options['place_url']
        response = requests.get(url)
        response.raise_for_status()
        place = response.json()
        new_place, _ = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'description_short': place['description_short'],
                'description_long': place['description_long'],
                'lat': place['coordinates']['lat'],
                'lon': place['coordinates']['lng'],
            },
        )

        image_urls = place['imgs']
        for image_url in image_urls:
            response = requests.get(image_url)
            response.raise_for_status()
            image_content = ContentFile(response.content, name=os.path.split(image_url)[1])
            Pictures.objects.create(place=new_place, picture=image_content)
