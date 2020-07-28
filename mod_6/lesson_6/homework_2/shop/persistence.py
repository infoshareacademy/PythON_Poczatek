
import os


def save_order(order):
    path_to_file = os.path.join("data", "orders.txt")
    with open(path_to_file, mode="a") as orders_file:
        orders_file.write(str(order))
        orders_file.write("\n")


def load_orders():
    path_to_file = os.path.join("data", "orders.txt")
    with open(path_to_file, mode="r") as orders_file:
        return orders_file.read()
