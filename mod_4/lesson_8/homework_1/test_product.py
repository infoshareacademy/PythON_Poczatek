
# Napisz test sprawdzając poprawność wykonanej w poprzednim module metody magicznej __eq__ w klasie Product
# - czyli porównywania produktów. Dla przypomnienia, dwa produkty są sobie równe,
# gdy mają taką samą nazwę, taką samą kategorię i taką samą cenę jednostkową.
# Wykorzystaj tuple do przygotowania różnych zestawów parametrów danych do algorytmu testującego.

from shop.product import Product


def test_product_comparision():
    parameters = [
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 4, True),
        ("Ciastka", "Jedzenie", 4, "Chleb", "Jedzenie", 4, False),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Słodycze", 4, False),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 8, False),
    ]

    for params in parameters:
        name, category, price, other_name, other_category, other_price, expected_result = params

        result = Product(name, category, price) == Product(other_name, other_category, other_price)
        if result == expected_result:
            print("OK")
        else:
            print(f"Błąd! Dla danych {params} wynik porównania jest {result} a powinien być {expected_result}")


def run_test():
    test_product_comparision()


if __name__ == '__main__':
    run_test()
