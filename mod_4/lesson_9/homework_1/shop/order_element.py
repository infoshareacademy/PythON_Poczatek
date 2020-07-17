class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.product.unit_price * self.quantity

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.quantity == other.quantity and self.product == other.product

    def __str__(self):
        return f"{self.product} x {self.quantity}"
