
# Stwórz enuma reprezentującego kategorię produktu. Poszczególnym elementom nadaj odpowiednie nazwy
# (np. FOOD) zaś jako wartość podaj tekst, który ma być traktowany jako “wypisywalna” nazwa kategorii (np. “Jedzenie”).
# Zastąp nazwę kategorii w produkcie - kategorią (enumem).
# Dostosuj odpowiednio metodę generującą pozycje w zamówieniu i wypisującą produkt.
from shop import data_generator
from shop.order import Order


def run_homework():
    some_order_elements = data_generator.generate_order_elements()
    my_order = Order("Bob", "Kowalski", order_elements=some_order_elements)
    print(my_order)


if __name__ == '__main__':
    run_homework()
