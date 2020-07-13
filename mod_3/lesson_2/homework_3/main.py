
# W klasie Order zastąp pole z łączną wartością zamówienia property typu getter,
# ramach którego ta wartość będzie dynamicznie obliczana.
# Pozwoli to usunąć z konstruktora oraz napisanego w poprzednim zadaniu settera
# ponowne przeliczanie łącznej wartości zamówienia.

from shop.data_generator import generate_order_elements
from shop.order import Order


def run_homework():
    first_name = "Mikołaj"
    last_name = "Lewandowski"

    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    print(normal_order)

    new_elements = generate_order_elements(3)
    normal_order.order_elements = new_elements
    print(normal_order)

    too_many_elements = generate_order_elements(1000)
    normal_order.order_elements = too_many_elements
    print(normal_order)

    print(normal_order.total_price)


if __name__ == '__main__':
    run_homework()
