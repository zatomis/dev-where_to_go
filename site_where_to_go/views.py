from django.shortcuts import render, get_object_or_404
from places.models import Place, Pictures
from django.http import Http404, JsonResponse


def show_main(request):
    features = []
    places = Place.objects.prefetch_related('images').all()
    for place in places:
        pictures = []
        for pic in place.images.all():
            pictures.append(pic.picture.url)
        place_details = {
            "title": place.title,
            "description_short": place.description_short,
            "description_long": place.description_long,
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
                "detailsUrl": place_details,
            }
        }
        features.append(place_geodata)

    places_geojson = {
      "type": "FeatureCollection",
      "features": features,
    }

    return render(request, 'index.html', context={'data': places_geojson})

def place_details(request, place_id):
    try:
        place = Place.objects.prefetch_related('images').get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404("Нет таких мест.")
    pics = []
    for image in place.images.all():
        pics.append(image.picture.url)
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
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})