import csv
import json

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import ProductCategory, Product
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


def save_order(order, file_name="orders.json"):
    new_order_data = {
        "client_first_name": order.client_first_name,
        "client_last_name": order.client_last_name,
        "order_elements": [
            {
                "product": {
                    "name": order_element.product.name,
                    "category": order_element.product.category.name,
                    "unit_price": order_element.product.unit_price,
                    "identifier": order_element.product.identifier,
                },
                "quantity": order_element.quantity,
            }
            for order_element in order.order_elements
        ],
    }
    try:
        with open(file_name, "r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders", {})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{order.client_first_name}-{order.client_last_name}"
    if client_id not in orders_by_clients_data:
        orders_by_clients_data[client_id] = []
    orders_by_clients_data[client_id].append(new_order_data)

    with open(file_name, "w") as orders_file:
        json.dump({"orders": orders_by_clients_data}, orders_file, indent=4)


def load_orders(client_first_name, client_last_name, file_name="orders.json"):
    try:
        with open(file_name, "r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders", {})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{client_first_name}-{client_last_name}"
    if client_id not in orders_by_clients_data:
        return []
    orders = orders_by_clients_data[client_id]
    return [
        Order(
            client_first_name=order["client_first_name"],
            client_last_name=order["client_last_name"],
            order_elements=[OrderElement(
                quantity=order_element["quantity"],
                product=Product(
                    name=order_element["product"]["name"],
                    category=ProductCategory[order_element["product"]["category"]],
                    unit_price=order_element["product"]["unit_price"],
                    identifier=order_element["product"]["identifier"],
                )
            ) for order_element in order["order_elements"]],
        ) for order in orders
    ]
