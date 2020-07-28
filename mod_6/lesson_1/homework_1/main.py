
# Zmodyfikuj obsługę przekroczenia dopuszczalnej liczby elementów zamówienia w klasie Order.
# W sytuacji gdy przypisanie nowej listy elementów albo dodanie pozycji do zamówienia spowoduje
# przekroczenie limitu wyrzuć odpowiedni wyjątek. Przetestuj działanie programu w skrypcie main.
from shop import data_generator
from shop.order import Order
from shop.product import Product


def run_homework():
    # order_elements_on_limit = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    # order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)
    # print(order_on_limit)

    # product = data_generator.generate_product()
    # quantity = data_generator.generate_quantity()
    # order_on_limit.add_product_to_order(product, quantity)

    order_elements_over_limit = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS + 1)
    order_over_limit = Order("Bob", "Kowalski", order_elements=order_elements_over_limit)


if __name__ == '__main__':
    run_homework()
