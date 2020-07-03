
# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów
# a wartościami instancje klasy produkt.


class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == '__main__':
    green_apple = Apple()
    red_apple = Apple()
    fresh_apple = Apple()
    print("green apple type:", type(green_apple))
    print("red apple type:", type(red_apple))
    print("fresh apple type:", type(fresh_apple))

    old_potato = Potato()
    young_potato = Potato()
    print("old potato type:", type(old_potato))
    print("young potato type:", type(young_potato))

    # orders = [Order(), Order(), Order(), Order(), Order()]
    orders = []
    for _ in range(5):
        orders.append(Order())
    print(orders)

    products = {
        "Jabłko": Product(),
        "Ziemniak": Product(),
        "Marchew": Product(),
        "Ciastka": Product(),
    }
    print(products)
