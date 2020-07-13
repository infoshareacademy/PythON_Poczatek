
# Stwórz klasę ExpressOrder, która dziedziczy po klasie Order.
# Klasa ta będzie reprezentować zamówienie z ekspresowym terminem dostawy.
# Względem klasy Order powinna dodatkowo przyjmować informacje o terminie dostawy
# (jako data w postaci napisu) oraz naliczać dodatkową opłatę za ekspresową dostawę
# w ramach obliczania łącznego kosztu zamówienia.
# Zaktualizuj również metodę __str__ dodając do niej informacje o terminie dostawy.
# W skrypcie main stwórz obiekt klasy ExpressOrder i wypisz informacje o nim.
from shop import data_generator
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = data_generator.generate_order_elements()
    express_order = ExpressOrder(
        delivery_date="10-05-2020",
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements
    )
    print(express_order)


if __name__ == '__main__':
    run_homework()
