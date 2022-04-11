import geopy

def geolocate(geocoder, place):
    return geocoder.geocode(place, exactly_one=False)[0][1]

ville = 'Montreal'  # Montreal, Quebec, Magog, Sherbrooke
geocoder = geopy.geocoders.Nominatim(user_agent="couverture-vegetale")
location = geolocate(geocoder, ville)
print(location)

# ------ AFFICHER IMAGE ------
# lancer a partir du terminal 
import geopy
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import imageio

def geolocate(geocoder, place):
    return geocoder.geocode(place, exactly_one=False)[0][1]

def request_map_at(lat, long, satellite=True, zoom=9, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size=str(size[0]) + "," + str(size[1]),
        ll=str(long) + "," + str(lat),
        l="sat" if satellite else "map",
        lang="en_US"
    )

    return requests.get(base, params=params)


def map_at(*args, **kwargs):
    return request_map_at(*args, **kwargs).content

def display_image(im):
    pixels = imageio.imread(BytesIO(im))
    plt.figure()
    plt.imshow(pixels)
    plt.show()


ville = 'Montreal'  # Montreal, Quebec, Magog, Sherbrooke
geocoder = geopy.geocoders.Nominatim(user_agent="couverture-vegetale")
location = geolocate(geocoder, ville)

map_png = map_at(*location)

display_image(map_png)

# ------ CALCULER POURCENTAGE VEGETALE ------- 

import geopy
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import imageio

def geolocate(geocoder, place):
    return geocoder.geocode(place, exactly_one=False)[0][1]

def request_map_at(lat, long, satellite=True, zoom=9, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size=str(size[0]) + "," + str(size[1]),
        ll=str(long) + "," + str(lat),
        l="sat" if satellite else "map",
        lang="en_US"
    )

    return requests.get(base, params=params)


def map_at(*args, **kwargs):
    return request_map_at(*args, **kwargs).content

def display_image(im):
    pixels = imageio.imread(BytesIO(im))
    plt.figure()
    plt.imshow(pixels)
    plt.show()

def pourcentage_vegetal(im):
    pixels = imageio.imread(BytesIO(im))
    pass

ville = 'Montreal'  # Montreal, Quebec, Magog, Sherbrooke
geocoder = geopy.geocoders.Nominatim(user_agent="couverture-vegetale")
location = geolocate(geocoder, ville)

map_png = map_at(*location)

#display_image(map_png)
pourcentage_vegetal(map_png)


# YANDEX POUR DES IMAGES SATELLITAIRES 