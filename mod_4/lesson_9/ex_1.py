
from collections import namedtuple

Location = namedtuple("Location", ["latitude", "longitude"])


def run_example():
    # location = (54.34, 16.64)
    location = Location(54.34, 16.64)
    print(location.latitude)
    print(location.longitude)
    print(type(location))

    location = Location(latitude=54.34, longitude=16.64)

    print(location[0])
    for coordinate in location:
        print(coordinate)


if __name__ == '__main__':
    run_example()