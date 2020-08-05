import geocoder
import requests

API_BASE_URL = 'https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/'

destinations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"
]

for point in destinations:
    location = geocoder.arcgis(point)

    full_api_url = API_BASE_URL + str(location.latlng[0]) + ',' + str(location.latlng[1])
    result = requests.request('GET', full_api_url).json()

    print (f'{point} is located at {location.latlng} \n at {point} right now it is {result["currently"]["temperature"]}')