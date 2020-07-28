
# Rozbuduj poprzednie rozwiązanie o wypisanie informacji zawartych w obiekcie wyjątku
from shop import data_generator
from shop.errors import ElementsInOrderLimitError
from shop.order import Order


def run_homework():
    order_elements_on_limit = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)

    product = data_generator.generate_product()
    quantity = data_generator.generate_quantity()

    try:
        order_on_limit.add_product_to_order(product, quantity)
    except ElementsInOrderLimitError as error:
        print(f"Wystąpił błąd: {error}")
        print(f"Limit pozycji w zamówieniu wynosi: {error.allowed_limit}")


if __name__ == '__main__':
    run_homework()
