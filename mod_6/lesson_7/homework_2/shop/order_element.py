from dataclasses import dataclass

from shop.product import Product


@dataclass
class OrderElement:
    product: Product
    quantity: int

    def calculate_price(self):
        return self.product.unit_price * self.quantity

    def __str__(self):
        return f"{self.product} x {self.quantity}"
