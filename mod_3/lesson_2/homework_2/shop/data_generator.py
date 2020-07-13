import random

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30


def generate_order_elements(products_to_generate=None):
    if products_to_generate is None:
        products_to_generate = random.randint(1, Order.MAX_ELEMENTS)

    order_elements = []
    for product_number in range(products_to_generate):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
