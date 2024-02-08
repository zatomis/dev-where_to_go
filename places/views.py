from urllib.parse import urljoin

from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def show_main(request):
    features = []
    places = Place.objects.prefetch_related('images').all()
    for place in places:
        main_url = request.build_absolute_uri()
        path_url = reverse("places", args=(place.pk,))
        pictures = [pic.image.url for pic in place.images.all()]
        place_geodata = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title": place.description_short,
                "unique_location": place.unique_location,
                "detailsUrl": urljoin(main_url, path_url),
            }
        }
        features.append(place_geodata)

    places_geojson = {
      "type": "FeatureCollection",
      "features": features,
    }
    return render(request, 'index.html', context={'data': places_geojson})
