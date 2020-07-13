
# Wykorzystaj metodę super do odwołania się z poziomu klasy ExpressOrder do bazowej implementacji
# metody total_price i zastąp powtórzony w klasie potomnej algorytm wynikiem z tego odwołania
# (łączna wartość zamówienia ekspresowego to łączna wartość zamówienia
# policzona według bazowej metody + opłata za ekspresową dostawę).
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

