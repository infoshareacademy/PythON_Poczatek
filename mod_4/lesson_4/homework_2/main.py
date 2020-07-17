
# Zmodyfikuj rozwiązanie poprzedniego zadania. Skorzystaj z dict comprehensions
# aby na podstawie słownika z produktami stworzyć nowy, w którym każdy produkt będzie pod kluczem o 1 większym.
# I tak produkt, który znajdował się w oryginalnym słowniku pod kluczem 15 trafi w nowym pod klucz 16, itd.
# Następnie skorzystaj z metody update aby “połączyć” oba słowniki.
from shop import data_generator


def run_homework():
    order_elements = data_generator.generate_order_elements()
    identifier_to_product = {
        order_element.product.identifier: order_element.product
        for order_element in order_elements
    }
    moved_ids_to_product = {
        identifier + 1: product
        for identifier, product in identifier_to_product.items()
    }

    print(identifier_to_product)
    print(moved_ids_to_product)

    identifier_to_product.update(moved_ids_to_product)
    print(identifier_to_product)


if __name__ == '__main__':
    run_homework()

