from django.shortcuts import render
from places.models import Place, Pictures


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

