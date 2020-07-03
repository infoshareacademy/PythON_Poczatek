import random

from shop.order_element import OrderElement
from shop.product import Product


class Order:

    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.calculate_price()
        return total_price

    def print_self(self):
        print("=" * 20)
        print(f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}")
        print(f"O łącznej wartości: {self.total_price} PLN")
        print("Zamówione produkty:")
        for element in self.order_elements:
            print("\t", end="")
            element.print_self()
        print("=" * 20)
        print()


def generate_order():
    number_of_product = random.randint(1, 10)
    order_elements = []
    for product_number in range(number_of_product):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))

    order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski", order_elements=order_elements)
    return order
