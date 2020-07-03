
# Dodaj do klasy Order maksymalną dopuszczalną liczbę elementów w zamówieniu.
# Upewnij się, że nie zostaje ona przekroczona podczas tworzenia obiektu klasy Order
# (w konstruktorze - gdy przekracza stwórz zamówienie tylko z pierwszymi X elementami)
# i podczas dodawania nowego produktu do zamówienia
# (gdy przekracza nie dodawaj produktu do zamówienia tylko wypisz informacje o przekroczeniu limitu)
# Żeby kontrolować liczbę pozycji w generowanym zamówieniu zastąp
# losową liczbę pozycji argumentem przekazanym do generate_order

from shop.order import generate_order
from shop.product import Product


def run_homework():
    order_over_limit = generate_order(10)
    print(order_over_limit)

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    order_below_limit = generate_order(2)
    order_below_limit.add_product_to_order(cookie, quantity=10)
    print(order_below_limit)
    order_over_limit.add_product_to_order(cookie, quantity=10)
    print(order_over_limit)


if __name__ == '__main__':
    run_homework()
