
# Zrefaktoryzuj rozwiązanie zadania drugiego z lekcji ósmej (funkcja jako obiekt)
# z modułu Programowanie Obiektowe I (zadanie w którym dodawaliśmy polityki rabatowe):
#  - Utwórz nowy moduł data_generator i przenieś do niego z pliku main funkcję generującą elementy zamówienia
#  - Ulepsz tę funkcję dodając do niej parametr liczby produktów w zamówieniu z domyślną wartością None
#     (jeżeli nie przekazano oczekiwanej liczby produktów to wylosuj ją z zakresu
#     od 1 do maksymalnej liczby pozycji w zamówieniu)
#  - Zastąp graniczne wartości, z których generowana jest liczba produktów w pozycji zamówienia oraz cena
#     jednostkowa produktu stałymi - zmiennymi globalnymi na poziomie nowo utworzonego modułu data_generator
#  - Usuń nieużywaną metodę klasy Order: generate_order


from shop.data_generator import generate_order_elements
from shop.order import Order


def run_homework():
    first_name = "Mikołaj"
    last_name = "Lewandowski"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)

    print(normal_order)


if __name__ == '__main__':
    run_homework()
