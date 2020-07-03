
# Zaimplementuj metodę __repr__ dla klas Apple oraz Potato

from shop.apple import Apple
from shop.potato import Potato


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price=3.5)
    red_apple = Apple(species_name="Red", size="S", price=2.8)
    old_potato = Potato(species_name="Potato Old", size="S", price=1.55)

    print(green_apple)
    print(red_apple)
    print(old_potato)

if __name__ == '__main__':
    run_homework()
