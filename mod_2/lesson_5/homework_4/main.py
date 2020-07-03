
# Zaimplementuj metodę __eq__ dla klasy Product, Order Element oraz Order
# Dwa produkty są równe jeżeli mają taką samą nazwę, kategorię i cenę jednostkową
# Dwie pozycje w zamówieniu są równe jeżeli ilość jest równa oraz ich produkty są równe
# Dwa zamówienia są równe jeżeli zostały złożone przez tego samego klienta, mają taką samą liczbę pozycji
# i są one sobie równe (nie muszą znajdować się na tych samych miejscach na liście)

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product


def run_homework():

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    # other_cookie = Product(name="Inne ciastko", category_name="Jedzenie", unit_price=4)
    juice = Product(name="Sok", category_name="Napoje", unit_price=3)
    first_order_elements = [
        OrderElement(product=cookie, quantity=3),
        # OrderElement(product=other_cookie, quantity=3),
        OrderElement(product=juice, quantity=4),
    ]
    # first_order_elements.append(OrderElement(product=juice, quantity=4))
    # first_order_elements[0].quantity = 10

    second_order_elements = [
        OrderElement(product=juice, quantity=4),
        OrderElement(product=cookie, quantity=3),
    ]

    first_order = Order(client_first_name="Kuba", client_last_name="Kowalski", order_elements=first_order_elements)
    second_order = Order(client_first_name="Kuba", client_last_name="Kowalski", order_elements=second_order_elements)
    # second_order.client_last_name = "Lewandowski"

    if first_order == second_order:
        print("Te zamówienia są takie same!")
    else:
        print("Te zamówienia są różne!")


if __name__ == '__main__':
    run_homework()
