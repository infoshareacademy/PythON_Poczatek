import random


def products_delivery():
    available_products = [
        "chleb",
        "ciastka",
        "jabłka",
        "dżem",
        "pomarańcze",
        "marchew",
        "bułki",
        "ziemniaki",
        "ser",
        "mleko"
    ]
    return [available_products[random.randint(0, 9)] for _ in range(5)]

