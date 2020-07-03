class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.product.unit_price * self.quantity

    def print_self(self):
        self.product.print_self()
        print(f"\t\t x {self.quantity}")
