import random

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product, ProductCategory

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_quantity():
    return random.randint(MIN_QUANTITY, MAX_QUANTITY)


def generate_product(name=None):

    category = ProductCategory.FOOD
    unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
    identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)

    if name is None:
        name = f"Produkt-{identifier}"

    return Product(name, category, unit_price, identifier)


def generate_order_elements(products_to_generate=None):
    if products_to_generate is None:
        products_to_generate = random.randint(1, Order.MAX_ELEMENTS)

    order_elements = []
    for product_number in range(products_to_generate):
        product_name = f"Produkt-{product_number}"
        product = generate_product(product_name)
        quantity = generate_quantity()
        order_elements.append(OrderElement(product, quantity))

    return order_elements
