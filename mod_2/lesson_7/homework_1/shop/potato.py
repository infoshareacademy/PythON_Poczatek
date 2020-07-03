class Potato:

    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def calculate_price(self, quantity):
        return quantity * self.price

    def __repr__(self):
        return f"<Potato species_name='{self.species_name}', size={self.size}, price={self.price}>"
