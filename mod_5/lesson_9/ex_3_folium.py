import random

import folium

GDANSK_CENTER_POSITION = [54.346320, 18.649246]
MAP_FILE_LOCATION = "map.html"


def random_point():
    return random.uniform(54.1, 54.5), random.uniform(18.4, 18.8)


def generate_example_map():
    generated_map = folium.Map(location=GDANSK_CENTER_POSITION, zoom_start=13)

    for number in range(20):
        generated_map.add_child(
            folium.CircleMarker(
                location=random_point(),
                fill="true",
                radius=8,
                popup=str(number),
                fill_color="blue",
                color="clear",
                fill_opacity=1,
            )
        )
    folium.PolyLine([random_point(), random_point()], color="red", weight=3.5, opacity=1,).add_to(
        generated_map
    )
    generated_map.save(MAP_FILE_LOCATION)


def run_example():
    generate_example_map()


if __name__ == '__main__':
    run_example()
