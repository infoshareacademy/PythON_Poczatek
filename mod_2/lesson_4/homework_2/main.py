
# Napisz metodę obliczającą łączną cenę jabłek, dla konkretnego obiektu
# Apple oraz łączną cenę ziemniaków dla konkretnego obiektu Potato
# na podstawie przekazanej w argumencie informacji o liczbie kilogramów.

from shop.apple import Apple
from shop.potato import Potato


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price=3.5)
    red_apple = Apple(species_name="Red", size="S", price=2.8)

    print(f"10kg zielonego jabłka kosztuje: {green_apple.calculate_price(10)}")
    print(f"5kg czerwonego jabłka kosztuje: {red_apple.calculate_price(5)}")

    old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    print(f"8kg starych ziemniaków kosztuje: {old_potato.calculate_price(8)}")


if __name__ == '__main__':
    run_homework()
