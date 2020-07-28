import csv
import os

from shop.product import ProductCategory
from shop.store import AvailableProduct


def save_store(available_products, file_name="store.csv"):
    with open(file_name, mode="w", newline="") as store_file:
        csv_writer = csv.writer(store_file)
        csv_writer.writerow(["name", "category", "unit_price", "identifier", "quantity"])
        for available_product in available_products:
            product = available_product.product
            csv_writer.writerow(
                [product.name, product.category.name, product.unit_price, product.identifier, available_product.quantity,]
            )


def load_store(file_name="store.csv"):
    with open(file_name, newline="") as store_file:
        csv_reader = csv.reader(store_file)
        next(csv_reader)
        return [
            AvailableProduct(
                name=row[0],
                category=ProductCategory[row[1]],
                unit_price=float(row[2]),
                identifier=int(row[3]),
                quantity=int(row[4]),
            )
            for row in csv_reader
        ]


def save_order(order):
    path_to_file = os.path.join("data", "orders.txt")
    with open(path_to_file, mode="a") as orders_file:
        orders_file.write(str(order))
        orders_file.write("\n")


def load_orders():
    path_to_file = os.path.join("data", "orders.txt")
    with open(path_to_file, mode="r") as orders_file:
        return orders_file.read()
