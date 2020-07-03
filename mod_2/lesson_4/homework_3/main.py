
# Napisz nową klasę: OrderElement, która będzie reprezentować pozycję w zamówieniu.
# Taka pozycja będzie zawierać informacje o produkcie i liczbie jego sztuk w zamówieniu.
# W klasie OrderElement zaimplementuj metodę wypisującą (info o liczbie elementó i produkcie)
# oraz obliczającą cenę danej pozycji w zamówieniu.
# W klasie Order zastąp listę produktów listą pozycji w zamówieniu
# (zmodyfikuj niezbędne funkcje, np. generowanie zamówienia).
# Napisz metodę obliczającą łączną wartość zamówienia jako sumę wartości wszystkich pozycji
# (wykorzystując wcześniej napisaną metodę z klasy OrderElement)
# i wykorzystaj ją w konstruktorze do inicjalizacji łącznej wartości zamówienia.

from shop.order import generate_order


def run_homework():
    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()


if __name__ == '__main__':
    run_homework()
