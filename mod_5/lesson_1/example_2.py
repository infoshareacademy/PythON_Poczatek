import geopy


def run_example():
    address = "aleja Grunwaldzka 472B, 80-309 Gdańsk"
    geolocator = geopy.Nominatim(user_agent="webinar-agent")
    address_code = geolocator.geocode(address)
    print(address_code.latitude)
    print(address_code.longitude)


if __name__ == '__main__':
    run_example()
