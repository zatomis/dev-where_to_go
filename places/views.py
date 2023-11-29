from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse
from urllib.parse import urljoin

def show_main(request):
    features = []
    places = Place.objects.prefetch_related('images').all()
    for place in places:
        main_url = request.build_absolute_uri()
        path_url = reverse("places", args=(place.pk,))
        pictures = [pic.picture.url for pic in place.images.all()]
        place_details = {
            "title": place.title,
            "short_description": place.description_short,
            "long_description": place.description_long,
            "coordinates": {
                "lng": place.lon,
                "lat": place.lat,
            },
            "imgs": pictures,
        }
        place_geodata = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title":place.description_short,
                "placeId": place.placeID,
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
    pics = [image.picture.url for image in place.images.all()]
    place_details = {
        "title": place.title,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat,
        },
        "imgs": pics,
        }
    return JsonResponse(get_place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 8})