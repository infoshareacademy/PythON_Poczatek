
# Do klasy Product dodaj pole identifier, będące liczbą.
# Zaktualizuj generator pozycji zamówienia, aby generował produkty zawierające losowy identyfikator.
# Użyj dict comprehensions, aby zamienić listę pozycji zamówienia w słownik,
# gdzie kluczem będzie identyfikator produktu z danej pozycji a wartością dany obiekt klasy Product.
from shop import data_generator


def run_homework():
    order_elements = data_generator.generate_order_elements()
    identifier_to_product = {
        order_element.product.identifier: order_element.product
        for order_element in order_elements
    }

    print(identifier_to_product)


if __name__ == '__main__':
    run_homework()

