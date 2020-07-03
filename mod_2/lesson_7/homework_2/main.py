
# Zamień funkcję generate_order na metodę klasy Order.

from shop.order import Order
from shop.product import Product


def run_homework():
    order_over_limit = Order.generate_order(10)
    print(order_over_limit)

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    order_below_limit = Order.generate_order(4)
    order_below_limit.add_product_to_order(cookie, quantity=10)
    print(order_below_limit)
    order_over_limit.add_product_to_order(cookie, quantity=10)
    print(order_over_limit)


if __name__ == '__main__':
    run_homework()
