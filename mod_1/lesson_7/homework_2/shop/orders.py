from .products_store import products, update_product_quantity

orders = [
    {
        "product": "chleb",
        "quantity": 10,
        "total_price": 35
    }
]


def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("Nie mamy tyle towaru!")
        return None

    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    orders.append(new_order)
    update_product_quantity(product_name, quantity)
    return new_order
