from dataclasses import dataclass
from enum import Enum


class ProductCategory(Enum):
    FOOD = "Jedzonko"
    OTHER = "Inne"
    TOOLS = "Narzędzia"


@dataclass
class Product:
    name: str
    category: ProductCategory
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category.value} | Cena: {self.unit_price} PLN/szt"


@dataclass
class ExpiringProduct(Product):
    production_year: int
    validity_years: int

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years
