from urllib.parse import urljoin

from django.shortcuts import render
from django.urls import reverse

from places.models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

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
                "title": place.short_description,
                "unique_location": place.slug,
                "detailsUrl": urljoin(main_url, path_url),
            }
        }
        features.append(place_geodata)

    places_geojson = {
      "type": "FeatureCollection",
      "features": features,
    }
    return render(request, 'index.html', context={'data': places_geojson})

def get_place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)
    pics = [pic.image.url for pic in place.images.all()]
    place_details = {
        "title": place.title,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat,
        },
        "imgs": pics,
        }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 8})