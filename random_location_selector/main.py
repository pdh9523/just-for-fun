from geopy.geocoders import Nominatim
import random


def select_random_location():
    '''
        무작위로 장소를 선정합니다
        장소는 구글 api와 연동되어 주소와 위,경도를 보여줍니다. 
    '''
    lot = random.uniform(34.5, 38)
    lat = random.uniform(126.5, 128.3)
    geolocator = Nominatim(user_agent="my_geolocation_app")

    target = f"{lot:.04f}, {lat:.04f}"
    location = geolocator.reverse(target)

    print(target)
    print(location.address)

select_random_location()