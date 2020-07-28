import csv
import os

from shop.product import ProductCategory
from shop.store import AvailableProduct


def save_store(available_products, file_name="store.csv"):
    with open(file_name, mode="w", newline="") as store_file:
        headers = ["name", "category", "unit_price", "identifier", "quantity"]
        csv_writer = csv.DictWriter(store_file, fieldnames=headers)
        csv_writer.writeheader()
        for available_product in available_products:
            product = available_product.product
            csv_writer.writerow(
                {
                    "name": product.name,
                    "category": product.category.name,
                    "unit_price": product.unit_price,
                    "identifier": product.identifier,
                    "quantity": available_product.quantity,
                }
            )


def load_store(file_name="store.csv"):
    with open(file_name, newline="") as store_file:
        csv_reader = csv.DictReader(store_file)
        return [
            AvailableProduct(
                name=row["name"],
                category=ProductCategory[row["category"]],
                unit_price=float(row["unit_price"]),
                identifier=int(row["identifier"]),
                quantity=int(row["quantity"]),
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
