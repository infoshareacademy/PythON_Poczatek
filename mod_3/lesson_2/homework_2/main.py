
# Do klasy Order dodaj property typu setter, które będzie ustawiać listę pozycji w zamówieniu
# oraz aktualizować łączną wartość zamówienia (obliczaną na podstawie nowej listy pozycji).
# W setterze sprawdź również czy nowa lista elementów nie przekracza dopuszczalnej dla zamówienia ilości.
# Jeżeli przekracza, to przypisz do zamówienia tylko tyle pierwszych elementów z nowej listy
# ile wynosi maksymalna dopuszczalna wartość w zamówieniu.

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


if __name__ == '__main__':
    run_homework()
