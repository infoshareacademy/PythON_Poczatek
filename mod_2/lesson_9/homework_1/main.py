
# Zmodyfikuj rozwiązanie zadania pierwszego z poprzedniej lekcji
# zamieniając funkcję wykorzystywaną przez metodę sortującą na lambdę

from shop.order import Order


def run_homework():
    orders = []
    for _ in range(5):
        orders.append(Order.generate_order())

    orders.sort(key=lambda order: order.total_price)
    for order in orders:
        print(order)


if __name__ == '__main__':
    run_homework()
