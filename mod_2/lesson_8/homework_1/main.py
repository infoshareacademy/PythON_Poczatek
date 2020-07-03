
# Wygeneruj 5 losowych zamówień i posortuj je rosnąco po ich łącznej wartości.
# Zastosuj własną funkcję zwracającą odpowiednią wartość, która będzie używana do porównania przez funkcję sortującą

from shop.order import Order


def get_order_price(order):
    return order.total_price


def run_homework():
    orders = []
    for _ in range(5):
        orders.append(Order.generate_order())

    orders.sort(key=get_order_price)
    for order in orders:
        print(order)


if __name__ == '__main__':
    run_homework()
